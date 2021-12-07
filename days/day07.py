def part1(crabs):
    end = max(crabs)
    steps = [0 for _ in range(0, end + 1)]
    for crab in crabs:
        for i in range(0, len(steps)):
            steps[i] += abs(crab - i)
    return min(steps)


def part2(crabs):
    end = max(crabs)
    steps = [0 for _ in range(0, end + 1)]
    for crab in crabs:
        for i in range(0, len(steps)):
            steps[i] += gauss_sum(abs(crab - i))
    return min(steps)


def gauss_sum(n):
    return n * (n + 1) // 2
