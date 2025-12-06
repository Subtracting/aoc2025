with open('input/day6_1.txt') as f:
    numbers = []
    operators = []
    lines = []
    for line in f.readlines():
        new_line = []
        linec = line.strip().split(' ')
        for el in linec:
            if el != '':
                new_line.append(el)
        if '+' in linec:
            operators.append(new_line)
        else:
            numbers.append(new_line)
            lines.append(line.replace('\n', ' '))

cols = len(numbers[0])
padding = [max([len(nums[col]) for nums in numbers])
           for col in range(cols)]

total = 0
i = -1
j = 0

while i < len(lines[0]) - padding[-1]:
    for pad in padding:
        operator = operators[0][j]
        calc = 1 if operator == '*' else 0
        i += pad + 1
        j += 1
        for num_col in range(i, i - pad - 1, -1):
            num = ''
            for line in lines:
                num += line[num_col]
            if set(num) != {' '}:
                if operator == '+':
                    calc += int(num)
                elif operator == '*':
                    calc *= int(num)
        total += calc

print(total)
