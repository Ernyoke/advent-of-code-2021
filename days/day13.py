def part1(coordinates, directions):
    return count_dots(fold(get_page(coordinates, *get_size(coordinates)), *directions[0]))


def part2(coordinates, directions):
    page = get_page(coordinates, *get_size(coordinates))
    for direction in directions:
        page = fold(page, *direction)
    print_page(page)


def get_size(coordinates):
    max_y, max_x = 0, 0
    for y, x in coordinates:
        if max_y < y:
            max_y = y
        if max_x < x:
            max_x = x
    return max_x, max_y


def get_page(coordinates, m, n):
    page = []
    for i in range(0, m + 1):
        page.append(['.' for _ in range(0, n + 1)])
    for y, x in coordinates:
        page[x][y] = '#'
    return page


def fold(page, direction, index):
    if direction == 'x':
        return fold_x(page, index)
    else:
        return fold_y(page, index)


def fold_y(page, y):
    new_page = [[dot for dot in page[i]] for i in range(0, y)]

    for i, line in enumerate(page[y + 1:]):
        for j, char in enumerate(line):
            if char == '#':
                new_page[y - i - 1][j] = '#'
    return new_page


def fold_x(page, x):
    new_page = [list(line[0:x]) for line in page]

    for i, line in enumerate(page):
        for j, char in enumerate(line[x + 1:]):
            if char == '#':
                new_page[i][x - j - 1] = '#'
    return new_page


def print_page(page):
    for line in page:
        print(''.join(map(str, line)))


def count_dots(page):
    count = 0
    for line in page:
        for char in line:
            if char == '#':
                count += 1
    return count
