with open('input/day5_1.txt') as f:
    ranges = []
    ids = []
    current = "ranges"
    for line in f.readlines():
        linec = line.strip()
        if linec == "":
            current = "ids"

        if current == "ranges":
            begin, end = map(int, linec.split("-"))
            ranges.append((begin, end))
        else:
            if linec != "":
                ids.append(int(linec))

count = 0

for id in ids:
    fresh = False
    for rng in ranges:
        begin, end = rng
        if id in range(begin, end + 1):
            fresh = True

    if fresh:
        count += 1

print(count)
