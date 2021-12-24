import functools

INSTRUCTIONS = []


def part1(instructions):
    global INSTRUCTIONS
    INSTRUCTIONS = instructions
    result = run(0, 0, 0, 0, 0, (9, 0, -1))
    return int(result[1])


def part2(instructions):
    global INSTRUCTIONS
    INSTRUCTIONS = instructions
    result = run(0, 0, 0, 0, 0, (1, 10, 1))
    return int(result[1])


cache = {}


@functools.cache
def run(step, x, y, w, z, interval):
    registers = {
        'x': x,
        'y': y,
        'w': w,
        'z': z
    }

    if z >= 10**7:
        return False, ''

    instructions = INSTRUCTIONS

    if step >= len(instructions):
        return z == 0, ''

    instruction = instructions[step]

    match (instruction[0]):
        case 'inp':
            for input_value in range(*interval):
                registers[instruction[1]] = input_value
                result = run(step + 1, registers['x'], registers['y'], registers['w'], registers['z'], interval)

                if result[0]:
                    return True, str(input_value) + result[1]

        case 'add':
            a = int(instruction[2]) if is_number(instruction[2]) else registers[instruction[2]]
            registers[instruction[1]] += a
        case 'mul':
            a = int(instruction[2]) if is_number(instruction[2]) else registers[instruction[2]]
            registers[instruction[1]] *= a
        case 'div':
            a = int(instruction[2]) if is_number(instruction[2]) else registers[instruction[2]]
            registers[instruction[1]] //= a
        case 'mod':
            a = int(instruction[2]) if is_number(instruction[2]) else registers[instruction[2]]
            registers[instruction[1]] %= a
        case 'eql':
            a = int(instruction[2]) if is_number(instruction[2]) else registers[instruction[2]]
            registers[instruction[1]] = 1 if a == registers[instruction[1]] else 0

    return run(step + 1, registers['x'], registers['y'], registers['w'], registers['z'], interval)


def get_input(value, index):
    str_value = str(value)
    return int(str_value[index])


def is_number(str_val):
    try:
        int(str_val)
        return True
    except ValueError:
        return False
