from unittest import TestCase

from days.day06 import part1, part2
from test.utils import read_lines

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day6Tests(TestCase):
    def test_part1(self):
        fish = [int(x) for x in read_lines('inputs/day06.txt')[0].split(',')]
        result = part1(fish, 80)
        self.assertEqual(365131, result)

    def test_part1_test1(self):
        fish = [int(x) for x in read_lines('inputs/day06_test.txt')[0].split(',')]
        result = part1(fish, 80)
        self.assertEqual(5934, result)

    def test_part2_test2(self):
        fish = [int(x) for x in read_lines('inputs/day06_test.txt')[0].split(',')]
        result = part2(fish, 256)
        self.assertEqual(26984457539, result)

    def test_part2(self):
        fish = [int(x) for x in read_lines('inputs/day06.txt')[0].split(',')]
        result = part2(fish, 256)
        self.assertEqual(1650309278600, result)

