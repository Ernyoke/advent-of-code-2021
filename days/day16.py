map_to_binary = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def part1(hex_string):
    binary = list(''.join([map_to_binary[char] for char in hex_string]))
    version = []
    parse(binary, version)
    return sum(version)


def part2(hex_string):
    binary = list(''.join([map_to_binary[char] for char in hex_string]))
    return parse(binary, [])[0]


def parse(binary, version):
    literals = []
    while binary and is_valid(binary):
        packet_version = convert_to_decimal(binary[:3])
        version.append(packet_version)
        packet_type_id = convert_to_decimal(binary[3:6])
        del binary[:6]
        if packet_type_id != 4:
            length_type_id = binary[0]
            del binary[0]
            if length_type_id == '0':
                length = convert_to_decimal(binary[:15])
                del binary[:15]
                to_parse = binary[:length]
                del binary[:length]
                partial = []
                while to_parse:
                    partial += parse(to_parse, version)
                literals += compute(partial, packet_type_id)
                return literals
            else:
                if len(binary) >= 11:
                    number_sub_packets = convert_to_decimal(binary[:11])
                    del binary[:11]
                    partial = []
                    for i in range(0, number_sub_packets):
                        partial += parse(binary, version)
                    literals += compute(partial, packet_type_id)
                    return literals

        else:
            res = ""
            while True:
                first = binary[0]
                res += "".join(binary[1:5])
                del binary[:5]
                if first == '0':
                    break
            return [int(res, 2)]
    return literals


def is_valid(lst):
    for i in lst:
        if i != '0':
            return True
    return False


def convert_to_decimal(binary):
    return int("".join(binary), 2)


def compute(literals, type_id):
    match type_id:
        case 0: return [sum(literals)]
        case 1: return [multiply(literals)]
        case 2: return [min(literals)]
        case 3: return [max(literals)]
        case 5: return [1 if literals[0] > literals[1] else 0]
        case 6: return [1 if literals[0] < literals[1] else 0]
        case 7: return [1 if literals[0] == literals[1] else 0]


def multiply(lst):
    total = 1
    for i in range(0, len(lst)):
        total *= lst[i]
    return total

