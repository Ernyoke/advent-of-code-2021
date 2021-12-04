def read_integers(path):
    """
    Read every line from a file into a list of integers
    :param path: path to the file
    :return: list with integers
    """
    with open(path, 'r') as f:
        data = f.read()
    return [int(i) for i in data.split()]


def read_lines_to_tuples(path):
    """
    Read every line from a file. Split every line to tuples and add every tuple to a list
    :param path: path to the file
    :return: list with tuples
    """
    with open(path, 'r') as f:
        data = f.read()
    return list(map(lambda line: tuple(line.split()), [word for word in data.split('\n')]))


def read_lines(path, separator=None):
    """
    Read every line to a list. Split the lines from a list if separator is not None
    :param path: path to the file
    :param separator: separator character or None
    :return: list with lines
    """
    with open(path, 'r') as f:
        data = f.read()
    return data.split(separator)
