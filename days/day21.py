from functools import lru_cache


def part1(player1, player2):
    score1, score2 = 0, 0
    die = 1
    while True:
        player1 = (player1 + (3 * die + 3)) % 10
        die += 3
        score1 += (10 if player1 == 0 else player1)
        if score1 >= 1000:
            return score2 * (die - 1)

        player2 = (player2 + (3 * die + 3)) % 10
        die += 3
        score2 += (10 if player2 == 0 else player2)
        if score2 >= 1000:
            return score1 * (die - 1)


def part2(player1, player2):
    return max(*count_universes(player1, 0, player2, 0))


@lru_cache(maxsize=None)
def count_universes(player1, score1, player2, score2):
    if score1 >= 21:
        return 1, 0
    elif score2 >= 21:
        return 0, 1

    result = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                new_player1 = (player1 + d1 + d2 + d3) % 10
                new_score_1 = score1 + (10 if new_player1 == 0 else new_player1)
                res1, res2 = count_universes(player2, score2, new_player1, new_score_1)
                result = (result[0] + res2, result[1] + res1)
    return result



