import os
from unittest import TestCase

from days.day20 import part1
from test.utils import read_lines

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day20Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day20_test1.txt', '\n')
        enhancement, image = Day20Tests.preprocess(data)
        self.assertEqual(35, part1(enhancement, image, 2))

    def test_part1(self):
        data = read_lines('inputs/day20.txt', '\n')
        enhancement, image = Day20Tests.preprocess(data)
        self.assertEqual(5573, part1(enhancement, image, 2))

    def test_part2(self):
        data = read_lines('inputs/day20.txt', '\n')
        enhancement, image = Day20Tests.preprocess(data)
        self.assertEqual(20097, part1(enhancement, image, 50))

    @staticmethod
    def preprocess(data):
        enhancement = data[0]
        image = []
        for line in data[2:]:
            image.append(list(line))
        return enhancement, image
