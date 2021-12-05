from collections import Counter


def part1(positions):
    counter = Counter()
    for a, b in positions:
        a_x, a_y = a
        b_x, b_y = b
        if a_x == b_x:
            start, end = min(a_y, b_y), max(a_y, b_y)
            for i in range(start, end + 1):
                counter[(a_x, i)] += 1
        elif a_y == b_y:
            start, end = min(a_x, b_x), max(a_x, b_x)
            for i in range(start, end + 1):
                counter[(i, a_y)] += 1
    return len([x for x in counter if counter[x] > 1])


def part2(positions):
    counter = Counter()
    for a, b in positions:
        a_x, a_y = a
        b_x, b_y = b
        x = 1 if a_x < b_x else 0 if a_x == b_x else -1
        y = 1 if a_y < b_y else 0 if a_y == b_y else -1
        c_x, c_y = a
        while (c_x, c_y) != b:
            counter[(c_x, c_y)] += 1
            c_x += x
            c_y += y
        counter[(c_x, c_y)] += 1
    return len([x for x in counter if counter[x] > 1])
