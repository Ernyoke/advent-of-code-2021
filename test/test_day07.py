from unittest import TestCase

from days.day07 import part1, part2
from test.utils import read_lines

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day7Tests(TestCase):
    def test_part1_test1(self):
        crabs = [int(x) for x in read_lines('inputs/day07_test.txt')[0].split(',')]
        result = part1(crabs)
        self.assertEqual(37, result)

    def test_part1(self):
        crabs = [int(x) for x in read_lines('inputs/day07.txt')[0].split(',')]
        result = part1(crabs)
        self.assertEqual(37, result)

    def test_part2_test1(self):
        crabs = [int(x) for x in read_lines('inputs/day07_test.txt')[0].split(',')]
        result = part2(crabs)
        self.assertEqual(168, result)

    def test_part2(self):
        crabs = [int(x) for x in read_lines('inputs/day07.txt')[0].split(',')]
        result = part2(crabs)
        self.assertEqual(101268110, result)
