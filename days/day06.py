def part1(fish, iterations):
    children = []
    for i in range(0, iterations):
        for j in range(0, len(fish)):
            if fish[j] == 0:
                children.append(8)
                fish[j] = 6
            else:
                fish[j] -= 1
        fish += children
        children = []
    return len(fish)


def part2(fish, iterations):
    res = 0
    cache = {}
    for f in fish:
        if f not in cache:
            children = [0 for _ in range(0, iterations)]
            for i in range(f, iterations, 7):
                children[i] = 1
            for i in range(f, iterations):
                if children[i] > 0:
                    for j in range(i + 9, iterations, 7):
                        children[j] += children[i]
            cache[f] = sum(children) + 1
        res += cache[f]
    return res
