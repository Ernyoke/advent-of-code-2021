from unittest import TestCase

from days.day11 import part1, part2
from test.utils import read_lines

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day11Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day11_test2.txt')
        octopuses = []
        for line in data:
            octopuses.append([int(c) for c in list(line)])
        self.assertEqual(1656, part1(octopuses, 100))

    def test_part1(self):
        data = read_lines('inputs/day11.txt')
        octopuses = []
        for line in data:
            octopuses.append([int(c) for c in list(line)])
        self.assertEqual(1620, part1(octopuses, 100))

    def test_part2_test1(self):
        data = read_lines('inputs/day11_test2.txt')
        octopuses = []
        for line in data:
            octopuses.append([int(c) for c in list(line)])
        self.assertEqual(195, part2(octopuses))

    def test_part2(self):
        data = read_lines('inputs/day11.txt')
        octopuses = []
        for line in data:
            octopuses.append([int(c) for c in list(line)])
        self.assertEqual(371, part2(octopuses))
