"""
A minesweeper board
"""

import common
import generation_settings

class MinesweeperBoard(object):
    def __init__(self, dimensions):
        """
        Creates a new empty 2nd array representing a minesweeper board.
        :param dimensions:
        """
        self.dimensions = dimensions
        self.content = [dimensions.x * [None]] * dimensions.y

    def __str__(self):
        for row in self.content:
            for cell in row:
                printed_char = cell or '-'
                print(f"{printed_char:5}", end='')


class MinesweeperBoardFactory(object):
    def generate(self, settings: generation_settings.MinesweeperGenerationSettings):
        board = MinesweeperBoard(settings.dimensions)
        # TODO randomly generate a new minesweeper game
        return board

