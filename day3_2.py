with open('input/day3_1.txt') as f:
    lines = [list(map(int, list(line.split('\n')[0])))
             for line in f.readlines()]


def find_max_num(number, length):
    maximum = 0
    max_idx = 0
    for i in range(0, len(number) - length + 1):
        if number[i] > maximum:
            maximum = number[i]
            max_idx = i
            if number[i] == 9:
                break
    new_number = number[max_idx+1:]
    return new_number, maximum


joltage = 0

for number in lines:
    final_number = ''
    remain_length = 12
    while remain_length != 0:
        number, value = find_max_num(number,  remain_length)
        remain_length -= 1
        final_number += str(value)
    joltage += int(final_number)

print(joltage)
