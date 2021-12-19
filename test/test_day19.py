import os
from unittest import TestCase

from days.day19 import part1, part2
from test.utils import read_lines

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day19Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines('inputs/day19_test1.txt', '\n')
        scanners = Day19Tests.preprocess(data)
        self.assertEqual(79, part1(scanners))

    def test_part1(self):
        data = read_lines('inputs/day19.txt', '\n')
        scanners = Day19Tests.preprocess(data)
        self.assertEqual(403, part1(scanners))

    def test_part1_test2(self):
        data = read_lines('inputs/day19_test1.txt', '\n')
        scanners = Day19Tests.preprocess(data)
        self.assertEqual(3621, part2(scanners))

    def test_part2(self):
        data = read_lines('inputs/day19.txt', '\n')
        scanners = Day19Tests.preprocess(data)
        self.assertEqual(10569, part2(scanners))

    @staticmethod
    def preprocess(data):
        scanners = []
        scanner = []
        for line in data:
            if not line:
                scanners.append(scanner)
                scanner = []
            else:
                if not line.startswith('---'):
                    scanner.append(tuple([int(part) for part in line.split(',')]))
        scanners.append(scanner)
        return scanners
