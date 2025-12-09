from collections import defaultdict
from bisect import bisect_left, bisect_right

with open('input/day9_1.txt') as f:
    coords = []
    for line in f.readlines():
        x, y = map(int, line.strip().split(","))
        coords.append((x, y))


def calc_area(x1, x2, y1, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def is_valid(x1, x2, y1, y2):
    new_corners = [(x1, y2), (x2, y1)]
    edges_found = 0

    for corner in new_corners:
        x, y = corner

        # up
        ys = tiles_by_x[x]
        i = bisect_left(ys, y)
        if i > 0:
            edges_found += 1

        # down
        ys = tiles_by_x[x]
        i = bisect_right(ys, y)
        if i < len(ys):
            edges_found += 1

        # left
        xs = tiles_by_y[y]
        i = bisect_left(xs, x)
        if i > 0:
            edges_found += 1

        # right
        xs = tiles_by_y[y]
        i = bisect_right(xs, x)
        if i < len(xs):
            edges_found += 1

    if edges_found == 8:
        first_x = min([x1, x2])
        first_y = min([y1, y2])
        last_x = max([x1, x2])
        last_y = max([y1, y2])

        for cy in [first_y, last_y]:
            empty = 0
            total_empty = 0
            for cx in range(first_x, last_x + 1):
                if (cx, cy) not in tiles and empty == 0:
                    empty = 1
                    total_empty += 1
                elif (cx, cy) in tiles and empty == 1:
                    empty = 0
            if total_empty > 1:
                return False

        for cx in [first_x, last_x]:
            empty = 0
            total_empty = 0
            for cy in range(first_y, last_y + 1):
                if (cx, cy) not in tiles and empty == 0:
                    empty = 1
                    total_empty += 1
                elif (cx, cy) in tiles and empty == 1:
                    empty = 0
            if total_empty > 1:
                return False

    return edges_found == 8


tiles = set()

for i in range(len(coords)):
    start_x, start_y = coords[i]
    end_x, end_y = coords[(i + 1) % len(coords)]
    dist_y = abs(start_y - end_y)
    dist_x = abs(start_x - end_x)

    if start_y - end_y < 0:  # move down
        for edge_y in range(dist_y):
            edge_coord = (start_x, start_y + edge_y)
            tiles.add(edge_coord)
    elif start_y - end_y > 0:  # move up
        for edge_y in range(dist_y):
            edge_coord = (start_x, start_y - edge_y)
            tiles.add(edge_coord)
    elif start_x - end_x < 0:  # move right
        for edge_x in range(dist_x):
            edge_coord = (start_x + edge_x, start_y)
            tiles.add(edge_coord)
    elif start_x - end_x > 0:  # move left
        for edge_x in range(dist_x):
            edge_coord = (start_x - edge_x, start_y)
            tiles.add(edge_coord)


x_tiles = [coord[0] for coord in tiles]
y_tiles = [coord[1] for coord in tiles]

max_x = max(x_tiles)
max_y = max(y_tiles)
min_x = min(x_tiles)
min_y = min(y_tiles)

tiles_by_x = defaultdict(list)
tiles_by_y = defaultdict(list)

for x, y in tiles:
    tiles_by_x[x].append(y)
    tiles_by_y[y].append(x)

for k in tiles_by_x:
    tiles_by_x[k].sort()
for k in tiles_by_y:
    tiles_by_y[k].sort()

max_area = 0

for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        area = calc_area(x1, x2, y1, y2)
        if area > max_area and is_valid(x1, x2, y1, y2):
            max_area = area

print(max_area)
