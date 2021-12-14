import os
from unittest import TestCase

from days.day14 import part1, part2
from test.utils import read_lines

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day14Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day14_test1.txt', separator='\n')
        template, pairs = Day14Tests.preprocess(data)

        self.assertEqual(1588, part1(template, pairs, 10))

    def test_part1(self):
        data = read_lines('inputs/day14.txt', separator='\n')
        template, pairs = Day14Tests.preprocess(data)

        self.assertEqual(2003, part1(template, pairs, 10))

    def test_part2_test1(self):
        data = read_lines('inputs/day14_test1.txt', separator='\n')
        template, pairs = Day14Tests.preprocess(data)

        self.assertEqual(2188189693529, part2(template, pairs, 40))

    def test_part2(self):
        data = read_lines('inputs/day14.txt', separator='\n')
        template, pairs = Day14Tests.preprocess(data)

        self.assertEqual(2276644000111, part2(template, pairs, 40))

    @staticmethod
    def preprocess(data):
        template = data[0]

        pairs = {}
        for line in data[2:]:
            parts = line.split(' -> ')
            pairs[parts[0]] = parts[1]

        return template, pairs

