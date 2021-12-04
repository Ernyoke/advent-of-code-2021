from unittest import TestCase

from days.day04 import part1, part2
from test.utils import read_lines

import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class Day4Tests(TestCase):
    def test_part1_test1(self):
        data = read_lines(os.path.join(dir_path, 'inputs/day04_test.txt'), separator='\n')
        numbers, boards = self.preprocess(data)
        result = part1(numbers, boards)
        self.assertEqual(4512, result)

    def test_part1(self):
        data = read_lines(os.path.join(dir_path, 'inputs/day04.txt'), separator='\n')
        numbers, boards = self.preprocess(data)
        result = part1(numbers, boards)
        self.assertEqual(60368, result)

    def test_part2_test1(self):
        data = read_lines(os.path.join(dir_path, 'inputs/day04_test.txt'), separator='\n')
        numbers, boards = self.preprocess(data)
        result = part2(numbers, boards)
        self.assertEqual(1924, result)

    def test_part2(self):
        data = read_lines(os.path.join(dir_path, 'inputs/day04.txt'), separator='\n')
        numbers, boards = self.preprocess(data)
        result = part2(numbers, boards)
        self.assertEqual(17435, result)

    @staticmethod
    def preprocess(data):
        numbers = [int(i.strip()) for i in data[0].split(',')]
        boards = []
        board = []
        for line in data[2:]:
            if not line.strip():
                boards.append(board)
                board = []
            else:
                board.append([int(i) for i in line.split()])
        boards.append(board)
        return numbers, boards
