import os
from unittest import TestCase

from days.day13 import part1, part2
from test.utils import read_lines

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day13Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day13_test1.txt', separator='\n')
        coordinates, fold = Day13Tests.preprocess(data)

        self.assertEqual(17, part1(coordinates, fold))

    def test_part1(self):
        data = read_lines('inputs/day13.txt', separator='\n')
        coordinates, fold = Day13Tests.preprocess(data)

        self.assertEqual(775, part1(coordinates, fold))

    def test_part2(self):
        data = read_lines('inputs/day13.txt', separator='\n')
        coordinates, fold = Day13Tests.preprocess(data)
        self.assertEqual(None, part2(coordinates, fold))

    @staticmethod
    def preprocess(data):
        coordinates = []
        fold = []
        for line in data:
            if line.startswith('fold'):
                parts = line.split(' ')
                folding = parts[2].split('=')
                fold.append((folding[0], int(folding[1])))
            elif line.strip():
                parts = line.split(',')
                coordinates.append((int(parts[0]), int(parts[1])))
        return coordinates, fold
