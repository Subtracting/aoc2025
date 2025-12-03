with open('input/day2_1.txt') as f:
    lines = [(int(line.split("-")[0]), int(line.split("-")[1]))
             for line in f.readline().strip().split(',')]
    lines = sorted(lines)

invalids = [int(str(num)+str(num)) for num in range(100000)]
total = 0

for num in range(100_000):
    invalid = int(str(num)+str(num))
    for start, end in lines:
        if invalid in range(start, end):
            total += invalid
            break

print(total)
