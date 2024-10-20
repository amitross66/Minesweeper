"""
Handles user -> game
"""

from argparse import ArgumentParser

from common import Position
from generation_settings import GAME_PRESETS, MinesweeperGenerationSettings
from master import MinesweeperGame, MinesweeperGameFactory

def parse_program_args():
    parser = ArgumentParser(description='A classic minesweeper game.')
    subparsers = parser.add_subparsers(dest='mode', required=True)

    # Option 1 - use preset difficulty
    preset_subparser = subparsers.add_parser('preset', help=f"Use a preset difficulty")
    preset_subparser.add_argument(
        'difficulty',
        choices=GAME_PRESETS.NAMES.keys(),
        required=True,
        help="Pick a preset"
    )

    # Option 2 - use custom game settings
    custom_subparser = subparsers.add_parser('custom_game', help=f"Create a custom game")
    custom_subparser.add_argument(
        '--height',
        type=int,
        required=True,
        help="Height of the game board"
    )
    custom_subparser.add_argument(
        '--width',
        type=int,
        required=True,
        help="Width of the game board"
    )
    custom_subparser.add_argument(
        '--mines-amount',
        type=int,
        required=True,
        help="Amount of mines to create"
    )

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_program_args()

    if args.mode == 'preset':
        game_generation_settings = GAME_PRESETS.NAMES[args.difficulty]

    elif args.mode == 'custom_game':
        game_generation_settings = MinesweeperGenerationSettings(
            Position(args.height, args.width),
            args.mines_amount
        )

    else: exit()

    game_factory = MinesweeperGameFactory()
    game = game_factory.generate(game_generation_settings)
    game.start()