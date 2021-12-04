def part1(depths):
    previous = depths[0]
    count = 0
    for depth in depths[1:]:
        count += 1 if depth > previous else 0
        previous = depth
    return count


def part2(depths):
    current_window = sum(depths[:3])
    count = 0
    for i in range(1, len(depths) - 2):
        window = sum(depths[i:i + 3])
        count += 1 if window > current_window else 0
        current_window = window
    return count
