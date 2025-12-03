with open('input/day2_1.txt') as f:
    lines = [(int(line.split("-")[0]), int(line.split("-")[1]))
             for line in f.readline().strip().split(',')]
    lines = sorted(lines)

invalids = []
total = 0

for num in range(1, 100_000):
    invalid = 0
    n = 2
    while len(str(invalid)) <= 10:
        invalid = int(n*str(num))
        if invalid in invalids:
            break
        for start, end in lines:
            if invalid in range(start, end):
                total += invalid
                invalids.append(invalid)
                break
        n += 1

print(total)
