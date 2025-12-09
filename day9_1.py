with open('input/day9_1.txt') as f:
    coords = []
    for line in f.readlines():
        x, y = map(int, line.strip().split(","))
        coords.append((x, y))


def calc_area(x1, x2, y1, y2):
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


coords = sorted(coords)
max_area = 0

for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        area = calc_area(x1, x2, y1, y2)
        if area > max_area:
            max_area = area

print(max_area)
