from heapq import heappush, heappop
import sys


def part1(risks):
    return compute_min_path(risks)


def part2(risks):
    bigger_risks = []
    for i in range(0, 5 * len(risks)):
        bigger_risks.append([])
        for j in range(0, 5 * len(risks[0])):
            risk = (risks[i % len(risks)][j % len(risks[0])] + (i // len(risks)) + (j // len(risks[0]))) % 9
            bigger_risks[i].append(9 if risk == 0 else risk)
    return compute_min_path(bigger_risks)


def compute_min_path(risks):
    min_risks = {}
    for i, line in enumerate(risks):
        for j, _ in enumerate(line):
            min_risks[(i, j)] = sys.maxsize
    min_risks[(0, 0)] = risks[0][0]
    heap = []
    heappush(heap, (0, 0, 0))
    while heap:
        current_risk, x, y = heappop(heap)
        neighbours = get_neighbours(x, y, risks)
        for n_x, n_y in neighbours:
            new_risk = risks[n_x][n_y] + current_risk
            if new_risk < min_risks[(n_x, n_y)]:
                min_risks[(n_x, n_y)] = new_risk
                heappush(heap, (risks[n_x][n_y] + current_risk, n_x, n_y))
    return min_risks[(len(risks) - 1, len(risks[0]) - 1)]


def get_neighbours(x, y, risks):
    neighbours = []

    if x - 1 >= 0:
        neighbours.append(tuple([x - 1, y]))

    if y + 1 < len(risks[0]):
        neighbours.append(tuple([x, y + 1]))

    if x + 1 < len(risks):
        neighbours.append(tuple([x + 1, y]))

    if y - 1 >= 0:
        neighbours.append(tuple([x, y - 1]))

    return neighbours


def print_risks(risks):
    for risk in risks:
        print(risk)