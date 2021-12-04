from unittest import TestCase

from days.day02 import part1, part2
from test.utils import read_lines_to_tuples

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day2Tests(TestCase):
    def test_part1(self):
        instructions = read_lines_to_tuples(os.path.join(dir_path, 'inputs/day02.txt'))
        result = part1(instructions)
        self.assertEqual(1855814, result)

    def test_part2(self):
        instructions = read_lines_to_tuples(os.path.join(dir_path, 'inputs/day02.txt'))
        result = part2(instructions)
        self.assertEqual(1845455714, result)
