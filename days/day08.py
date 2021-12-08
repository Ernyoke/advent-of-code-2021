def part1(data):
    count = 0
    for notes, signals in data:
        count += len([signal for signal in signals if len(signal) in [2, 3, 4, 7]])
    return count


def part2(data):
    count = 0
    for notes, signals in data:
        numbers = compute_numbers(notes)
        display = ""
        for signal in signals:
            s = set(list(signal))
            for i in range(0, 10):
                if s.issubset(numbers[i]) and numbers[i].issubset(s):
                    display += str(i)
        count += int(display)
    return count


def compute_numbers(notes):
    note_lengths = {}
    for note in notes:
        length = len(note)
        if length not in note_lengths:
            note_lengths[length] = []
        note_lengths[len(note)].append(set(list(note)))

    numbers = {1: note_lengths[2][0], 7: note_lengths[3][0], 4: note_lengths[4][0], 8: note_lengths[7][0]}

    # compute number 3
    numbers[3] = [s for s in note_lengths[5] if not numbers[7] - s][0]
    note_lengths[5].remove(numbers[3])

    # compute number 9
    numbers[9] = [s for s in note_lengths[6] if numbers[4].issubset(s)][0]
    note_lengths[6].remove(numbers[9])

    # compute number 0 and 6
    numbers[0] = [s for s in note_lengths[6] if not (numbers[4] - numbers[1]).issubset(s)][0]
    note_lengths[6].remove(numbers[0])
    numbers[6] = note_lengths[6][0]

    # compute number 5 and 2
    numbers[5] = [s for s in note_lengths[5] if (numbers[9] - numbers[1]).issubset(s)][0]
    note_lengths[5].remove(numbers[5])
    numbers[2] = note_lengths[5][0]

    return numbers
