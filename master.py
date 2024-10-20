"""
A game master, controlling the entire game.
"""
from common import Position
from minesweeper_board import MinesweeperBoardFactory
from generation_settings import MinesweeperGenerationSettings
from enum import Enum, auto
import IO

class MinesweeperGameStates(Enum):
    PREPARING = auto()
    IN_PROGRESS = auto()
    FINISHED_WIN = auto()
    FINISHED_LOSS = auto()


class MinesweeperGame(object):
    def __init__(self, board = None):
        self.board = board
        self.state = MinesweeperGameStates.PREPARING

    def start(self):
        print("Started the game! have fun (:")
        self.state = MinesweeperGameStates.IN_PROGRESS
        print(self.board)
        self.turn()

    def turn(self):
        """
        Takes input from user, updates game state.
        """
        IO.write(f"Enter your move: <x>, <y>")
        x, y = IO.readf("%d, %d")
        print(Position(x, y))

class MinesweeperGameFactory(object):
    def generate(self, _generation_settings: MinesweeperGenerationSettings):
        # Create the minesweeper game
        game = MinesweeperGame()

        # Create a new board
        board_factory = MinesweeperBoardFactory()
        board = board_factory.generate(_generation_settings)

        # Transfer ownership
        game.board = board
        return game

