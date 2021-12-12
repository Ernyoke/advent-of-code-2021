from unittest import TestCase
from collections import defaultdict

from days.day12 import part1, part2
from test.utils import read_lines

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day12Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day12_test1.txt')
        graph = Day12Tests.preprocess(data)
        self.assertEqual(10, part1(graph))

    def test_part1_test2(self):
        data = read_lines('inputs/day12_test2.txt')
        graph = Day12Tests.preprocess(data)
        self.assertEqual(226, part1(graph))

    def test_part1(self):
        data = read_lines('inputs/day12.txt')
        graph = Day12Tests.preprocess(data)
        self.assertEqual(4912, part1(graph))

    def test_part2_test1(self):
        data = read_lines('inputs/day12_test1.txt')
        graph = Day12Tests.preprocess(data)
        self.assertEqual(36, part2(graph))

    def test_part2_test2(self):
        data = read_lines('inputs/day12_test2.txt')
        graph = Day12Tests.preprocess(data)
        self.assertEqual(3509, part2(graph))

    def test_part2(self):
        data = read_lines('inputs/day12.txt')
        graph = Day12Tests.preprocess(data)
        self.assertEqual(150004, part2(graph))

    @staticmethod
    def preprocess(data):
        graph = defaultdict(set)
        for line in data:
            source, destination = line.split('-')
            graph[source].add(destination)
            graph[destination].add(source)
        return graph


