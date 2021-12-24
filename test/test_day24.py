import os
from unittest import TestCase

from days.day24 import part1, part2
from test.utils import read_lines_to_tuples

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day22Tests(TestCase):

    def test_part1(self):
        instructions = read_lines_to_tuples('inputs/day24.txt')
        self.assertEqual(99429795993929, part1(instructions))

    def test_part2(self):
        instructions = read_lines_to_tuples('inputs/day24.txt')
        self.assertEqual(18113181571611, part2(instructions))
