def find_positions(board, number):
    positions = []
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if number == board[i][j]:
                positions.append((i, j))
    return positions


def get_column(board, col):
    return map(lambda x: x[col], board)


def is_winner(board, position):
    i, j = position
    if not [value for value in board[i] if value != -1]:
        return True
    elif not [value for value in get_column(board, j) if value != -1]:
        return True
    return False


def is_winner_check_all(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if is_winner(board, (i, j)):
                return True
    return False


def sum_board(board):
    return sum(sum(filter(lambda value: value != -1, line)) for line in board)


def part1(numbers, boards):
    for number in numbers:
        for board in boards:
            for position in find_positions(board, number):
                i, j = position
                board[i][j] = -1
                if is_winner(board, position):
                    return sum_board(board) * number


def part2(numbers, boards):
    for number in numbers:
        for board in boards:
            for position in find_positions(board, number):
                i, j = position
                board[i][j] = -1
        for board in list(boards):
            if is_winner_check_all(board):
                if len(boards) <= 1:
                    return sum_board(boards[0]) * number
                else:
                    boards.remove(board)
