import os
from unittest import TestCase

from days.day15 import part1, part2
from test.utils import read_lines

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day15Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day15_test1.txt')
        risks = []
        for line in data:
            risks.append([int(c) for c in list(line)])
        self.assertEqual(40, part1(risks))

    def test_part1(self):
        data = read_lines('inputs/day15.txt')
        risks = []
        for line in data:
            risks.append([int(c) for c in list(line)])
        self.assertEqual(40, part1(risks))

    def test_part2_test1(self):
        data = read_lines('inputs/day15_test1.txt')
        risks = []
        for line in data:
            risks.append([int(c) for c in list(line)])
        self.assertEqual(315, part2(risks))

    def test_part2(self):
        data = read_lines('inputs/day15.txt')
        risks = []
        for line in data:
            risks.append([int(c) for c in list(line)])
        self.assertEqual(2842, part2(risks))

