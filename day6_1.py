with open('input/day6_1.txt') as f:
    numbers = []
    operators = []
    for line in f.readlines():
        new_line = []
        linec = line.strip().split()
        for el in linec:
            new_line.append(el)
        if '+' in linec:
            operators.append(new_line)
        else:
            numbers.append(list(map(int, new_line)))

total = 0
cols = len(numbers[0])
rows = len(numbers)

for col in range(cols):
    operator = operators[0][col]
    calc = 1 if operator == '*' else 0
    for nums in numbers:
        if operator == '+':
            calc += nums[col]
        elif operator == '*':
            calc *= nums[col]
    total += calc

print(total)
