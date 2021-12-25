def part1(sea):
    step = 0
    movement = True
    while movement:
        touched = []
        new_sea = [['.'] * len(sea[0]) for _ in sea]
        movement = False
        for x, line in enumerate(sea):
            for y, v in enumerate(line):
                if v == '>':
                    n_x, n_y = next_position(x, y, sea)
                    if sea[n_x][n_y] == '.':
                        new_sea[n_x][n_y] = v
                        touched.append((x, y))
                        movement = True
        for x, y in touched:
            sea[x][y] = '.'
        touched = []
        for x, line in enumerate(sea):
            for y, v in enumerate(line):
                if v == 'v':
                    n_x, n_y = next_position(x, y, sea)
                    if new_sea[n_x][n_y] == '.' and sea[n_x][n_y] == '.':
                        new_sea[n_x][n_y] = v
                        touched.append((x, y))
                        movement = True
        for x, y in touched:
            sea[x][y] = '.'
        for x, line in enumerate(sea):
            for y, v in enumerate(line):
                if v != '.':
                    if new_sea[x][y] == '.':
                        new_sea[x][y] = v
        step += 1
        sea = new_sea
    return step


def next_position(x, y, sea):
    if sea[x][y] == '>':
        if y >= len(sea[x]) - 1:
            return x, 0
        else:
            return x, y + 1
    if sea[x][y] == 'v':
        if x >= len(sea) - 1:
            return 0, y
        else:
            return x + 1, y


def pretty_print(sea):
    for line in sea:
        print("".join(line))
