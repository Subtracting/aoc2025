with open('input/day4_1.txt') as f:
    grid = [list(line.split('\n')[0])
            for line in f.readlines()]


def neighbour_count(grid, x, y):
    directions = [[-1, 0], [-1, -1], [0, -1], [-1, 1],
                  [1, 0], [1, 1], [0, 1], [1, -1]]
    count = 0
    for direction in directions:
        dir_y, dir_x = direction
        if 0 <= y + dir_y < len(grid) and 0 <= x + dir_x < len(grid[0]):
            if grid[y + dir_y][x + dir_x] == '@':
                count += 1
    return count


total = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '@' and neighbour_count(grid, x, y) < 4:
            total += 1

print(total)
