"""
A minesweeper board
"""

import common
import generation_settings
import random

from common import Position


class MinesweeperBoard(object):
    def __init__(self, dimensions):
        """
        Creates a new empty 2nd array representing a minesweeper board.
        :param dimensions:
        """
        self.dimensions = dimensions
        self.content = [[None for _ in range(dimensions.x)] for _ in range(dimensions.y)]

    def __str__(self):
        s = ""
        for row in self.content:
            for cell in row:
                printed_char = cell or '?'
                s += f"{printed_char:3}"
            s += "\n"

        return s

    def __getitem__(self, position):
        return self.content[position.y][position.x]

    def __setitem__(self, position, value):
        self.content[position.y][position.x] = value


class MinesweeperBoardFactory(object):
    def __init__(self):
        self.board = None
        self._generation_settings = None

    def generate(self, settings: generation_settings.MinesweeperGenerationSettings):
        self._generation_settings = settings
        self.board = MinesweeperBoard(settings.dimensions)
        self.fill_board()
        return self.board

    def fill_board(self):
        all_positions = [Position(row, col)
                         for row in range(self._generation_settings.dimensions.y)
                         for col in range(self._generation_settings.dimensions.x)
                         ]

        mine_positions = random.sample(all_positions, self._generation_settings.mines_amount)

        for position in all_positions:
            self.board[position] = common.UNREVEALED_MINE if position in mine_positions else common.UNREVEALED_EMPTY_SQUARE