import ast
import os
from unittest import TestCase

from days.day18 import part1, part2
from test.utils import read_lines

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day18Tests(TestCase):
    def test_part1_test2(self):
        data = read_lines('inputs/day18_test1.txt', '\n')
        lines = Day18Tests.preprocess(data)
        self.assertEqual(3488, part1(lines))

    def test_part1(self):
        data = read_lines('inputs/day18.txt', '\n')
        lines = Day18Tests.preprocess(data)
        self.assertEqual(3359, part1(lines))

    def test_part2_test1(self):
        data = read_lines('inputs/day18_test2.txt', '\n')
        lines = Day18Tests.preprocess(data)
        self.assertEqual(3993, part2(lines))

    def test_part2(self):
        data = read_lines('inputs/day18.txt', '\n')
        lines = Day18Tests.preprocess(data)
        self.assertEqual(4616, part2(lines))

    @staticmethod
    def preprocess(data):
        result = []
        for line in data:
            result.append(ast.literal_eval(line))
        return result
