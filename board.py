"""
A minesweeper board
"""

import common

DEFAULT_DIMENSIONS = common.Position(12, 12)

class Board(object):
    def __init__(self, dimensions = DEFAULT_DIMENSIONS):
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


class BoardFactory(object):
    def generate(self, dimensions = DEFAULT_DIMENSIONS):
        board = Board(dimensions)
        # TODO randomly generate a new minesweeper game
        return board

