def part1(coordinates):
    x1, x2 = coordinates[0]
    y1, y2 = coordinates[1]
    max_y = -2000
    for i in range(500, 0, -1):
        for j in range(500, -500, -1):
            x, y = 0, 0
            velocity_x = i
            velocity_y = j
            current_max_y = y
            it = 0
            while True:
                x += max(0, velocity_x - it)
                y += velocity_y - it
                current_max_y = max(y, current_max_y)
                if is_inside(x, y, x1, x2, y1, y2):
                    max_y = max(max_y, current_max_y)
                    break
                else:
                    if x > max(x1, x2) or y < min(y1, y2):
                        break
                it += 1
    return max_y


def part2(coordinates):
    x1, x2 = coordinates[0]
    y1, y2 = coordinates[1]
    counter = 0
    for i in range(500, 0, -1):
        for j in range(500, -500, -1):
            x, y = 0, 0
            velocity_x = i
            velocity_y = j
            it = 0
            while True:
                x += max(0, velocity_x - it)
                y += velocity_y - it
                if is_inside(x, y, x1, x2, y1, y2):
                    counter += 1
                    break
                else:
                    if x > max(x1, x2) or y < min(y1, y2):
                        break
                it += 1
    return counter


def is_inside(x, y, x1, x2, y1, y2):
    return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)


