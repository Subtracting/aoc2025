import ast

buttons = []
lights = []

binaries = []

with open('input/day10_1.txt') as f:
    coords = []
    for line in f.readlines():
        light, rest = line.split("] ")
        light = light[1:]
        lights.append(light)
        button, req = rest.split(" {")  # }
        button = button.split(" ")
        buttons.append(button)


def generate_binary(element, max_l):
    element = ast.literal_eval(element)
    element = [element] if isinstance(element, int) else element
    binary = ['0'] * max_l
    for pos in element:
        binary[pos] = '1'
    return ''.join(binary)


for i in range(len(buttons)):
    light = lights[i].replace('.', '0').replace('#', '1')
    max_l = len(light)

    button = buttons[i]
    binary = {light: []}
    for element in button:
        binary[light].append(generate_binary(element, max_l))
    binaries.append(binary)


def xor_match(new_values, min_count, buttons, seen):
    values = []

    for val2 in new_values:
        for val in buttons:
            xor = bin(int(val, 2) ^ int(val2[0], 2))
            new_count = 1 + val2[1]
            if xor not in seen or new_count < seen[xor]:
                values.append((xor, new_count))
                seen[xor] = new_count
            if xor == '0b0':
                return new_count, []

    return None, values


total = 0

for binary in binaries:
    for light, buttons in binary.items():
        min_count = None
        xors = []
        new_values = []
        seen = {}
        for val in buttons:
            xor = bin(int(val, 2) ^ int(light, 2))
            count = 1
            if xor == '0b0':
                min_count = 1
                break
            if xor not in seen or count < seen[xor]:
                new_values.append((xor, count))
                seen[xor] = count

        while not min_count:
            min_count, new_values = xor_match(new_values, min_count, buttons, seen)
        total += min_count

print(total)
