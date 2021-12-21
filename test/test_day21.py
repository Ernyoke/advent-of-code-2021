import os
from unittest import TestCase

from days.day21 import part1, part2

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day21Tests(TestCase):
    def test_part1_test1(self):
        self.assertEqual(739785, part1(4, 8))

    def test_part1(self):
        self.assertEqual(707784, part1(9, 10))

    def test_part2_test1(self):
        self.assertEqual(444356092776315, part2(4, 8))

    def test_part2(self):
        self.assertEqual(157595953724471, part2(9, 10))
