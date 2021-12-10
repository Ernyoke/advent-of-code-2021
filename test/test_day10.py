from unittest import TestCase

from days.day10 import part1, part2
from test.utils import read_lines

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day10Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day10_test.txt')
        self.assertEqual(26397, part1(data))

    def test_part1(self):
        data = read_lines('inputs/day10.txt')
        self.assertEqual(311949, part1(data))

    def test_part2_test1(self):
        data = read_lines('inputs/day10_test.txt')
        self.assertEqual(288957, part2(data))

    def test_part2(self):
        data = read_lines('inputs/day10.txt')
        self.assertEqual(3042730309, part2(data))
