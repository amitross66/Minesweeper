"""
A game master, controlling the entire game.
"""

from minesweeper_board import MinesweeperBoardFactory
import common

class MinesweeperGame(object):
    def __init__(self, board = None):
        self.board = board

    def start(self):
        pass

class MinesweeperGameFactory(object):
    def generate(self, generation_settings):
        # Create the minesweeper game
        game = MinesweeperGame()

        # Create a new board
        board_factory = MinesweeperBoardFactory()
        board = board_factory.generate(generation_settings)

        # Transfer ownership
        game.board = board
        return game