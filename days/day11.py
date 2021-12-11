def part1(data, steps):
    total_flashes = 0
    for step in range(0, steps):
        increment(data)
        flashing = find_positions_equals(data, 10)
        total_flashes += len(flashing)
        for x, y in flashing:
            data[x][y] = 0
        while flashing:
            x, y = flashing.pop(0)
            neighbours = get_neighbours(x, y, data)
            for x_n, y_n in neighbours:
                if 0 < data[x_n][y_n] < 10:
                    data[x_n][y_n] += 1
                    if data[x_n][y_n] == 10:
                        data[x_n][y_n] = 0
                        flashing.append((x_n, y_n))
                        total_flashes += 1
    return total_flashes


def part2(data):
    step = 0
    while True:
        increment(data)
        flashing = find_positions_equals(data, 10)
        for x, y in flashing:
            data[x][y] = 0
        while flashing:
            x, y = flashing.pop(0)
            neighbours = get_neighbours(x, y, data)
            for x_n, y_n in neighbours:
                if 0 < data[x_n][y_n] < 10:
                    data[x_n][y_n] += 1
                    if data[x_n][y_n] == 10:
                        data[x_n][y_n] = 0
                        flashing.append((x_n, y_n))
        step += 1
        if all_zero(data):
            return step


def increment(data):
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if data[i][j] < 10:
                data[i][j] += 1


def find_positions_equals(data, number):
    positions = []
    for i, line in enumerate(data):
        for j, value in enumerate(line):
            if value == number:
                positions.append((i, j))
    return positions


def get_neighbours(x, y, data):
    neighbours = []

    if x - 1 >= 0:
        neighbours.append(tuple([x - 1, y]))

    if y + 1 < len(data[0]):
        neighbours.append(tuple([x, y + 1]))

    if x + 1 < len(data):
        neighbours.append(tuple([x + 1, y]))

    if y - 1 >= 0:
        neighbours.append(tuple([x, y - 1]))

    if x - 1 >= 0 and y - 1 >= 0:
        neighbours.append(tuple([x - 1, y - 1]))

    if x - 1 >= 0 and y + 1 < len(data[0]):
        neighbours.append(tuple([x - 1, y + 1]))

    if x + 1 < len(data) and y - 1 >= 0:
        neighbours.append(tuple([x + 1, y - 1]))

    if x + 1 < len(data) and y + 1 < len(data[0]):
        neighbours.append(tuple([x + 1, y + 1]))

    return neighbours


def all_zero(data):
    for line in data:
        for value in line:
            if value != 0:
                return False
    return True


def print_data(data):
    for line in data:
        print(line)

