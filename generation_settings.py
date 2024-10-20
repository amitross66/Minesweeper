"""
Settings which impact the initial generation of the game.
"""

import common


class MinesweeperGenerationSettings(object):
    def __init__(self, dimensions, mines_amount):
        self.dimensions = dimensions
        self.mines_amount = mines_amount


# Named presets:
class MinesweeperGenerationPresets(object):
    EASY = MinesweeperGenerationSettings(
        common.Position(6, 6),
        5
    )

    MEDIUM = MinesweeperGenerationSettings(
        common.Position(10, 10),
        12
    )

    HARD = MinesweeperGenerationSettings(
        common.Position(15, 15),
        25
    )

    NAMES = {
        'Easy': EASY,
        'Medium': MEDIUM,
        'Hard': HARD
    }

    def __str__(self):
        return self.NAMES.keys().__str__()

class InvalidPresetException(Exception):
    pass

GAME_PRESETS = MinesweeperGenerationPresets()