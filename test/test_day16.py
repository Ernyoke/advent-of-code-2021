import os
from unittest import TestCase

from days.day16 import part1, part2
from test.utils import read_lines

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day16Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day16_test1.txt')
        self.assertEqual(40, part1(data[0]))

    def test_part1_test2(self):
        data = read_lines('inputs/day16_test2.txt')
        self.assertEqual(14, part1(data[0]))

    def test_part1_test3(self):
        data = read_lines('inputs/day16_test3.txt')
        self.assertEqual(16, part1(data[0]))

    def test_part1_test4(self):
        data = read_lines('inputs/day16_test4.txt')
        self.assertEqual(12, part1(data[0]))

    def test_part1_test5(self):
        data = read_lines('inputs/day16_test5.txt')
        self.assertEqual(23, part1(data[0]))

    def test_part1_test6(self):
        data = read_lines('inputs/day16_test6.txt')
        self.assertEqual(31, part1(data[0]))

    def test_part1(self):
        data = read_lines('inputs/day16.txt')
        self.assertEqual(940, part1(data[0]))

    def test_part2_test1(self):
        data = read_lines('inputs/day16_test7.txt')
        self.assertEqual(1, part2(data[0]))

    def test_part2_test2(self):
        data = read_lines('inputs/day16_test8.txt')
        self.assertEqual(7, part2(data[0]))

    def test_part2_test3(self):
        data = read_lines('inputs/day16_test9.txt')
        self.assertEqual(9, part2(data[0]))

    def test_part2_test4(self):
        data = read_lines('inputs/day16_test10.txt')
        self.assertEqual(54, part2(data[0]))

    def test_part2_test5(self):
        data = read_lines('inputs/day16_test11.txt')
        self.assertEqual(3, part2(data[0]))

    def test_part2(self):
        data = read_lines('inputs/day16.txt')
        self.assertEqual(13476220616073, part2(data[0]))

