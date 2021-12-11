from statistics import median

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def part1(data):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    errors = 0
    for chunk in data:
        valid, last_char, _ = is_valid(chunk)
        if not valid:
            errors += points[last_char]
    return errors


def part2(data):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    scores = []
    for chunk in data:
        score = 0
        valid, _, remaining = is_valid(chunk)
        if valid and remaining:
            while remaining:
                score = 5 * score + points[pairs[remaining.pop()]]
            scores.append(score)
    return median(scores)


def is_valid(chunk):
    stack = []
    for char in chunk:
        if char in pairs.keys():
            stack.append(char)
        else:
            if pairs[stack.pop()] != char:
                return False, char, []
    return True, '', stack
