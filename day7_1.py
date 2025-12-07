with open('input/day7_1.txt') as f:
    grid = []
    for line in f.readlines():
        line = line.strip()
        if 'S' in line:
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
            activated.add((y, x))
            left_start = (y, x - 1)
            right_start = (y, x + 1)
            grid[y][x - 1] = '|'
            grid[y][x + 1] = '|'
            break

    return left_start, right_start


activated = set()

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '|':
            left_start, right_start = split_beam(y, x)
            while left_start != (0, 0) and right_start != (0, 0):
                left_start, _ = split_beam(left_start[0], left_start[1])
                _, right_start = split_beam(right_start[0], right_start[1])

print(len(activated))
