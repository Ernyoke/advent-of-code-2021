from unittest import TestCase

from days.day05 import part1, part2
from test.utils import read_lines_to_tuples

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day5Tests(TestCase):
    def test_part1(self):
        positions = Day5Tests.preprocess('inputs/day05.txt')
        result = part1(positions)
        self.assertEqual(7473, result)

    def test_part1_test1(self):
        positions = Day5Tests.preprocess('inputs/day05_test.txt')
        result = part1(positions)
        self.assertEqual(5, result)

    def test_part2(self):
        positions = Day5Tests.preprocess('inputs/day05.txt')
        result = part2(positions)
        self.assertEqual(24164, result)

    def test_part2_test1(self):
        positions = Day5Tests.preprocess('inputs/day05_test.txt')
        result = part2(positions)
        self.assertEqual(12, result)

    @staticmethod
    def preprocess(path):
        data = read_lines_to_tuples(os.path.join(dir_path, path))
        str_positions = [(tuple(x.split(',')), tuple(y.split(','))) for x, sep, y in data]
        return [(tuple(int(i) for i in a), tuple(int(i) for i in b)) for a, b in str_positions]
