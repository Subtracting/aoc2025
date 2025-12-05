with open('input/day5_1.txt') as f:
    ranges = []
    ids = []
    current = "ranges"
    for line in f.readlines():
        linec = line.strip()
        if linec == "":
            break

        if current == "ranges":
            begin, end = map(int, linec.split("-"))
            ranges.append((begin, end))


def collapse_ranges(ranges):
    for i in range(0, len(ranges) - 1):
        begin1, end1 = ranges[i]
        begin2, end2 = ranges[i + 1]

        if end1 >= begin2 and end2 >= end1:
            ranges[i] = (begin1, end2)
            ranges[i + 1] = (0, 0)
        elif begin1 <= begin2 and end1 >= end2:
            ranges[i] = (begin1, end1)
            ranges[i + 1] = (0, 0)
    return ranges


for _ in range(5):
    ranges = collapse_ranges(sorted(ranges))

total = 0
for rng in ranges:
    begin, end = rng
    if (begin, end) != (0, 0):
        diff = end - begin + 1
        total += diff

print(total)
