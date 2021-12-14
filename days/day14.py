from collections import Counter
from math import ceil


def part1(template, pairs, steps):
    temp = template
    for i in range(0, steps):
        temp = next_template(temp, pairs)
    min_char, max_char = get_min_max(temp)
    return max_char - min_char


def part2(template, pairs, steps):
    pair_counts = Counter()
    for i in range(0, len(template) - 1):
        pair_counts[template[i:i + 2]] += 1
    for i in range(0, steps):
        next_pair_counts = Counter()
        for pair_count_key in pair_counts:
            pair_count_value = pair_counts[pair_count_key]
            pair = pairs[pair_count_key]
            new_pair_1 = pair_count_key[0] + pair
            new_pair_2 = pair + pair_count_key[1]
            next_pair_counts[new_pair_1] += pair_count_value
            next_pair_counts[new_pair_2] += pair_count_value
        pair_counts = next_pair_counts

    min_char, max_char = get_min_max_pairs(pair_counts)
    return max_char - min_char


def next_template(template, pairs):
    new_template = ''
    i = 0
    while i < len(template) - 1:
        pair = template[i:i + 2]
        if pair in pairs:
            pair = pair[0] + pairs[pair] + pair[1]
        new_template = new_template[:len(new_template) - 1] + pair
        i += 1
    return new_template


def get_min_max(template):
    counter = Counter()
    for char in template:
        counter[char] += 1
    return get_min_max_counter(counter)


def get_min_max_pairs(pairs):
    counter = Counter()
    for key in pairs:
        counter[key[0]] += pairs[key]
        counter[key[1]] += pairs[key]
    min, max = get_min_max_counter(counter)
    return ceil(min / 2), ceil(max / 2)


def get_min_max_counter(counter):
    first_key = next(iter(counter))
    min, max = counter[first_key], counter[first_key]
    for key in counter:
        if counter[key] < min:
            min = counter[key]
        if counter[key] > max:
            max = counter[key]
    return min, max
