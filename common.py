"""
Common definitions for the minesweeper game.
"""

class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

UNREVEALED_MINE = 'M'
UNREVEALED_EMPTY_SQUARE = 'E'
REVEALED_BLANK_SQUARE = 'B'
REVEALED_DIGIT = [None, '1', '2', '3', '4', '5', '6', '7', '8']
REVEALED_MINE = 'X'