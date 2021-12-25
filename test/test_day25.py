import os
from unittest import TestCase

from days.day25 import part1
from test.utils import read_lines

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day25Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day25_test1.txt')
        sea = []
        for line in data:
            sea.append(list(line))
        self.assertEqual(58, part1(sea))

    def test_part1(self):
        data = read_lines('inputs/day25.txt')
        sea = []
        for line in data:
            sea.append(list(line))
        self.assertEqual(58, part1(sea))
