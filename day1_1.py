with open('input/day1_1.txt') as f:
    lines = [line.split('\n')[0] for line in f.readlines()]

value = 50
password = 0

for line in lines:
    num = int(line[1:])
    if 'L' in line:
        value = (value - num) % 100
    else:
        value = (value + num) % 100
    if value == 0:
        password += 1

print(password)
