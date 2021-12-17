import os
from unittest import TestCase

from days.day17 import part1, part2
from test.utils import read_lines

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day17Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day17_test1.txt')
        coordinates = Day17Tests.preprocess(data)
        self.assertEqual(45, part1(coordinates))

    def test_part1(self):
        data = read_lines('inputs/day17.txt')
        coordinates = Day17Tests.preprocess(data)
        self.assertEqual(5886, part1(coordinates))

    def test_part2_test1(self):
        data = read_lines('inputs/day17_test1.txt')
        coordinates = Day17Tests.preprocess(data)
        self.assertEqual(112, part2(coordinates))

    def test_part2(self):
        data = read_lines('inputs/day17.txt')
        coordinates = Day17Tests.preprocess(data)
        self.assertEqual(1806, part2(coordinates))

    @staticmethod
    def preprocess(parts):
        x = parts[2].replace('x=', '')
        y = parts[3].replace('y=', '')
        x1, x2 = x.split('..')
        y1, y2 = y.split('..')
        return (int(x1), int(x2.replace(',', ''))), (int(y1), int(y2))
