def part1(enhancement, image, it):
    padded = pad(image, '.', 2)

    for i in range(0, it):
        padded = pad(padded, padded[0][0], 1)
        new_image = []
        for x in range(1, len(padded) - 1):
            new_image.append([])
            for y in range(1, len(padded[0]) - 1):
                new_image[x - 1].append(get_new_pixel(padded, x, y, enhancement))
        padded = pad(new_image, new_image[0][0], 1)

    return count_char(padded, '#')


def pad(image, char, border_size):
    n = len(image)
    m = len(image[0])

    padded = []
    for i in range(0, n + 2 * border_size):
        padded.append([])
        for j in range(0, m + 2 * border_size):
            if i < border_size or j < border_size or i >= n + border_size or j >= m + border_size:
                padded[i].append(char)
            else:
                padded[i].append(image[i - border_size][j - border_size])

    return padded


def get_new_pixel(image, x, y, enhancement):
    pixels = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            pixels.append('1' if image[i][j] == '#' else '0')
    return enhancement[int("".join(pixels), 2)]


def count_char(image, char):
    count = 0
    for line in image:
        for c in line:
            if c == char:
                count += 1
    return count


def pretty_print(image):
    for line in image:
        print("".join(line))
