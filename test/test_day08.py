from unittest import TestCase

from days.day08 import part1, part2
from test.utils import read_lines_to_tuples

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day8Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines_to_tuples('inputs/day08_test.txt', '|')
        processed_data = [(signals.strip().split(' '), output.strip().split(' ')) for (signals, output) in data]

        result = part1(processed_data)
        self.assertEqual(26, result)

    def test_part1(self):
        data = read_lines_to_tuples('inputs/day08.txt', '|')
        processed_data = [(signals.strip().split(' '), output.strip().split(' ')) for (signals, output) in data]

        result = part1(processed_data)
        self.assertEqual(321, result)

    def test_part2_test1(self):
        data = read_lines_to_tuples('inputs/day08_test.txt', '|')
        d = [(signals.strip().split(' '), output.strip().split(' ')) for (signals, output) in data]

        result = part2(d)
        self.assertEqual(61229, result)

    def test_part2_test2(self):
        data = read_lines_to_tuples('inputs/day08_test2.txt', '|')
        processed_data = [(signals.strip().split(' '), output.strip().split(' ')) for (signals, output) in data]

        result = part2(processed_data)
        self.assertEqual(9361, result)

    def test_part2(self):
        data = read_lines_to_tuples('inputs/day08.txt', '|')
        processed_data = [(signals.strip().split(' '), output.strip().split(' ')) for (signals, output) in data]

        result = part2(processed_data)
        self.assertEqual(1028926, result)
