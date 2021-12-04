from unittest import TestCase

from days.day01 import part1, part2
from test.utils import read_integers

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day1Tests(TestCase):
    def test_part1(self):
        depths = read_integers(os.path.join(dir_path, 'inputs/day01.txt'))
        result = part1(depths)
        self.assertEqual(1759, result)

    def test_part2(self):
        depths = read_integers(os.path.join(dir_path, 'inputs/day01.txt'))
        result = part2(depths)
        self.assertEqual(1805, result)
