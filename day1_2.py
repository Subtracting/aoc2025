with open('input/day1_1.txt') as f:
    lines = [line.split('\n')[0] for line in f.readlines()]

value = 50
password = 0

for line in lines:
    prev = value
    times = 0
    num = int(line[1:])
    direction = line[0]
    if direction == 'L':
        value = (prev - num) % 100
        if num >= prev:
            times = 1 + (num - prev) // 100
        if prev == 0:
            times -= 1
    else:
        value = (prev + num) % 100
        if prev + num >= 100:
            times = 1 + (num - (100 - prev)) // 100

    print(line, value, times)
    password += times

print(password)
