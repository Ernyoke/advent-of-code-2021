def get_common_bits(binaries):
    n = len(binaries[0])
    bits = []
    for i in range(0, n):
        bits.append(1 if sum(int(bit[i]) for bit in binaries) >= len(binaries) / 2 else 0)
    return bits


def part1(binaries):
    gamma, eps = 0, 0
    common_bits = get_common_bits(binaries)
    for bit in common_bits:
        gamma = (gamma << 1) | bit
        eps = (eps << 1) | (~bit & 1)
    return gamma * eps


def part2(binaries):
    common_bits = get_common_bits(binaries)
    oxygen_rating = binaries
    for i in range(0, len(binaries[0])):
        oxygen_rating = list(filter(lambda oxygen: int(oxygen[i]) == common_bits[i], oxygen_rating))
        common_bits = get_common_bits(oxygen_rating)
        if len(oxygen_rating) <= 1:
            break

    co2_rating = binaries
    common_bits = get_common_bits(binaries)
    for i in range(0, len(binaries[0])):
        co2_rating = list(filter(lambda co2: int(co2[i]) != common_bits[i], co2_rating))
        common_bits = get_common_bits(co2_rating)
        if len(co2_rating) <= 1:
            break

    return int(oxygen_rating[0], 2) * int(co2_rating[0], 2)
