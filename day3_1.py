with open('input/day3_1.txt') as f:
    lines = [list(map(int, list(line.split('\n')[0])))
             for line in f.readlines()]

joltage = 0

for line in lines:
    first_maximum_idx = line[:-1].index(max(line[:-1]))
    second_maximum_idx = line[first_maximum_idx+1:] \
        .index(max(line[first_maximum_idx+1:]))

    value1 = line[first_maximum_idx]
    value2 = line[first_maximum_idx + 1 + second_maximum_idx]

    final = int(str(value1) + str(value2))
    joltage += final

print(joltage)
