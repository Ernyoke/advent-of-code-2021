import os
from unittest import TestCase

from days.day22 import part1, part2
from test.utils import read_lines

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day22Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day22_test1.txt', '\n')
        areas = Day22Tests.preprocess(data)
        self.assertEqual(590784, part1(areas))

    def test_part1(self):
        data = read_lines('inputs/day22.txt', '\n')
        areas = Day22Tests.preprocess(data)
        self.assertEqual(542711, part1(areas))

    def test_part2_test1(self):
        data = read_lines('inputs/day22_test2.txt', '\n')
        areas = Day22Tests.preprocess(data)
        self.assertEqual(2758514936282235, part2(areas))

    def test_part2(self):
        data = read_lines('inputs/day22.txt', '\n')
        areas = Day22Tests.preprocess(data)
        self.assertEqual(1160303042684776, part2(areas))

    @staticmethod
    def preprocess(data):
        areas = []
        for line in data:
            status, coords = line.split(' ')
            x, y, z = coords.split(',')
            areas.append((status, Day22Tests.extract_coords(x),
                          Day22Tests.extract_coords(y),
                          Day22Tests.extract_coords(z)))
        return areas

    @staticmethod
    def extract_coords(coord_str):
        x, y = coord_str[2:].split('..')
        return int(x), int(y)
