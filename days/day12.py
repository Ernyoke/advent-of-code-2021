def part1(graph):
    return traverse(graph, 'start', ['start'])


def part2(graph):
    touched = {}
    for key in graph:
        if key.islower():
            touched[key] = 0
    return traverse_twice(graph, 'start', ['start'], touched)


def traverse(graph, current, route):
    if current == 'end':
        return 1
    else:
        result = 0
        for next_cave in graph[current]:
            if next_cave.isupper() or (next_cave.islower() and next_cave not in route):
                result += traverse(graph, next_cave, route + [next_cave])
        return result


def traverse_twice(graph, current, route, touched):
    if current == 'end':
        return 1
    else:
        result = 0
        for next_cave in graph[current]:
            if next_cave.isupper():
                result += traverse_twice(graph, next_cave, route + [next_cave], touched)
            elif next_cave != 'start' and can_be_visited(next_cave, touched):
                touched[next_cave] += 1
                result += traverse_twice(graph, next_cave, route + [next_cave], touched)
                touched[next_cave] -= 1
        return result


def can_be_visited(cave, touched):
    visited_twice = None
    for key in touched:
        if touched[key] > 1:
            visited_twice = key
            break
    if visited_twice and touched[cave] > 0:
        return False
    return True

