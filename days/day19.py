from collections import Counter


def part1(scanners):
    beacons = set()
    for scanner, vec in normalize_scanner_positions(scanners):
        for coord in scanner:
            beacons.add(add(coord, vec))
    return len(beacons)


def part2(scanners):
    normalized = normalize_scanner_positions(scanners)
    max_distance = 0
    for _, scanner1 in normalized:
        for _, scanner2 in normalized:
            if scanner1 is not scanner2:
                dist = minus(scanner1, scanner2)
                max_distance = max(max_distance, abs(dist[0]) + abs(dist[1]) + abs(dist[2]))
    return max_distance


def normalize_scanner_positions(scanners):
    stack = [(scanners[0], (0, 0, 0))]
    normalized_scanners = [(scanners[0], (0, 0, 0))]
    touched = [False for _ in scanners]
    touched[0] = True
    while stack:
        current_scanner, current_orientation = stack.pop()
        for i, other_scanner in enumerate(scanners):
            if not touched[i]:
                overlap = get_overlap(current_scanner, other_scanner)
                if overlap is not None:
                    orientation, rotated_scanner = overlap
                    normalized_scanners.append((rotated_scanner, add(current_orientation, orientation)))
                    stack.append((rotated_scanner, add(current_orientation, orientation)))
                    touched[i] = True
    return normalized_scanners


transforms = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, y, -z),
    lambda x, y, z: (x, -y, z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (-x, y, z),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, -y, -z),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (z, x, -y),
    lambda x, y, z: (z, -x, y),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (-z, x, y),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (-z, -x, -y),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (y, z, -x),
    lambda x, y, z: (y, -z, x),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (-y, z, x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (-y, -z, -x),
    lambda x, y, z: (x, z, y),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (x, -z, -y),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-x, z, -y),
    lambda x, y, z: (-x, -z, y),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (y, x, z),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (y, -x, -z),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-y, x, -z),
    lambda x, y, z: (-y, -x, z),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (z, y, x),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (z, -y, -x),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-z, y, -x),
    lambda x, y, z: (-z, -y, x),
    lambda x, y, z: (-z, -y, -x)
]


def add(vec1, vec2):
    x1, y1, z1 = vec1
    x2, y2, z2 = vec2
    return x1 + x2, y1 + y2, z1 + z2


def minus(vec1, vec2):
    x1, y1, z1 = vec1
    x2, y2, z2 = vec2
    return x1 - x2, y1 - y2, z1 - z2


def get_overlap(scanner1, scanner2):
    for transform in transforms:
        counter = Counter()
        scanner2_rotated = apply_transform(scanner2, transform)
        for vec1 in scanner1:
            for vec2 in scanner2_rotated:
                counter[minus(vec1, vec2)] += 1
        vec, count = counter.most_common(1)[0]
        if count >= 12:
            return vec, scanner2_rotated
    return None


def apply_transform(scanner, transform):
    return [transform(*beacon) for beacon in scanner]


