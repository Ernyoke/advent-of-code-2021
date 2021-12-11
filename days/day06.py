def part1(fishes, iterations):
    children = []
    for i in range(0, iterations):
        for j, fish in enumerate(fishes):
            if fish == 0:
                children.append(8)
                fishes[j] = 6
            else:
                fishes[j] -= 1
        fishes += children
        children = []
    return len(fishes)


def part2(fishes, iterations):
    res = 0
    cache = {}
    for fish in fishes:
        if fish not in cache:
            children = [0 for _ in range(0, iterations)]
            for i in range(fish, iterations, 7):
                children[i] = 1
            for i in range(fish, iterations):
                if children[i] > 0:
                    for j in range(i + 9, iterations, 7):
                        children[j] += children[i]
            cache[fish] = sum(children) + 1
        res += cache[fish]
    return res
