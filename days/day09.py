def part1(cave):
    result = 0
    for i, j in get_low_points(cave):
        result += cave[i][j] + 1
    return result


def part2(cave):
    touched = []
    for i in range(0, len(cave)):
        touched.append([0 for _ in cave[i]])

    results = []
    for i, j in get_low_points(cave):
        results.append(get_basin(i, j, cave, touched))

    results.sort(reverse=True)
    return multiply(results[:3])


def get_low_points(cave):
    low_points = []
    for i, _ in enumerate(cave):
        for j, _ in enumerate(cave[0]):
            if is_minimum(i, j, get_neighbours(i, j, cave), cave):
                low_points.append((i, j))
    return low_points


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

    return neighbours


def is_minimum(x, y, positions, data):
    for cx, cy in positions:
        if data[x][y] >= data[cx][cy]:
            return False
    return True


def get_basin(x, y, cave, touched):
    stack = [(x, y)]
    touched[x][y] = 1
    count = 1
    while stack:
        cx, cy = stack.pop()
        ix = cx - 1
        while ix >= 0 and 9 > cave[ix][cy] > cave[ix + 1][cy] and touched[ix][cy] == 0:
            stack.append((ix, cy))
            count += 1
            touched[ix][cy] = 1
            ix -= 1

        ix = cx + 1
        while ix < len(cave) and 9 > cave[ix][cy] > cave[ix - 1][cy] and touched[ix][cy] == 0:
            stack.append((ix, cy))
            count += 1
            touched[ix][cy] = 1
            ix += 1

        iy = cy - 1
        while iy >= 0 and 9 > cave[cx][iy] > cave[cx][iy + 1] and touched[cx][iy] == 0:
            stack.append((cx, iy))
            count += 1
            touched[cx][iy] = 1
            iy -= 1

        iy = cy + 1
        while iy < len(cave[0]) and 9 > cave[cx][iy] > cave[cx][iy - 1] and touched[cx][iy] == 0:
            stack.append((cx, iy))
            count += 1
            touched[cx][iy] = 1
            iy += 1
    return count


def multiply(lst):
    total = 1
    for i in range(0, len(lst)):
        total *= lst[i]
    return total
