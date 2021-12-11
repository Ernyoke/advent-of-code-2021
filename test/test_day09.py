from unittest import TestCase

from days.day09 import part1, part2
from test.utils import read_lines

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day9Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day09_test.txt')
        cave = []
        for line in data:
            cave.append([int(c) for c in list(line)])
        self.assertEqual(15, part1(cave))

    def test_part1(self):
        data = read_lines('inputs/day09.txt')
        cave = []
        for line in data:
            cave.append([int(c) for c in list(line)])
        self.assertEqual(545, part1(cave))

    def test_part2_test1(self):
        data = read_lines('inputs/day09_test.txt')
        cave = []
        for line in data:
            cave.append([int(c) for c in list(line)])
        self.assertEqual(1134, part2(cave))

    def test_part2(self):
        data = read_lines('inputs/day09.txt')
        cave = []
        for line in data:
            cave.append([int(c) for c in list(line)])
        self.assertEqual(950600, part2(cave))
