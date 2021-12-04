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
    with open(path, 'r') as f:
        data = f.read()
    return list(map(lambda line: tuple(line.split()), [word for word in data.split('\n')]))


def read_lines(path, splitter=None):
    with open(path, 'r') as f:
        data = f.read()
    return data.split(splitter)
