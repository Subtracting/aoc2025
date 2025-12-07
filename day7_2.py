with open('input/day7_1.txt') as f:
    grid = []
    for line in f.readlines():
        line = line.strip()
        if 'S' in line:
            start_x = line.index('S')
            line = line.replace('S', '|')
        grid.append(list(line))


def split_beam(y, x):
    left_start = (0, 0)
    right_start = (0, 0)
    while y < len(grid):
        if grid[y][x] != '^':
            grid[y][x] = '|'
            y += 1
        else:
            nodes.add((y, x))
            left_start = (y, x - 1)
            right_start = (y, x + 1)
            grid[y][x - 1] = '|'
            grid[y][x + 1] = '|'
            break

    return left_start, right_start


nodes = set()

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '|':
            left_start, right_start = split_beam(y, x)
            while left_start != (0, 0) and right_start != (0, 0):
                left_start, _ = split_beam(left_start[0], left_start[1])
                _, right_start = split_beam(right_start[0], right_start[1])


next_node = [[None]*len(grid[0]) for _ in range(len(grid))]

for x in range(len(grid[0])):
    last = None
    for y in reversed(range(len(grid))):
        if (y, x) in nodes:
            last = y
        next_node[y][x] = last

memo = {}


def traverse_tree(y, x):
    node = (y, x)
    if node in memo:
        return memo[node]

    if y is None or y >= len(grid):
        return 1

    left = traverse_tree(next_node[y][x - 1], x - 1)
    right = traverse_tree(next_node[y][x + 1], x + 1)

    memo[node] = left + right

    return memo[node]


beam_paths = traverse_tree(0, start_x)
print(beam_paths)
