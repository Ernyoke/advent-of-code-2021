def preprocess(instructions):
    return map(lambda i: (i[0], int(i[1])), instructions)


def part1(instructions):
    x, y = 0, 0
    for direction, units in preprocess(instructions):
        match direction:
            case 'forward': x += units
            case 'down': y += units
            case 'up': y -= units
    return x * y


def part2(instructions):
    x, y, aim = 0, 0, 0
    for direction, units in preprocess(instructions):
        match direction:
            case 'forward':
                x += units
                y += aim * units
            case 'down': aim += units
            case 'up': aim -= units
    return x * y
