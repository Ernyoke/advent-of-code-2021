from unittest import TestCase

from days.day03 import part1, part2
from test.utils import read_lines

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day3Tests(TestCase):
    def test_part1(self):
        binaries = read_lines(os.path.join(dir_path, 'inputs/day03.txt'))
        result = part1(binaries)
        self.assertEqual(4118544, result)

    def test_part2_test1(self):
        instructions = read_lines(os.path.join(dir_path, 'inputs/day03_test.txt'))
        result = part2(instructions)
        self.assertEqual(230, result)

    def test_part2(self):
        instructions = read_lines(os.path.join(dir_path, 'inputs/day03.txt'))
        result = part2(instructions)
        self.assertEqual(3832770, result)
