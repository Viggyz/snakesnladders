import sys

from src.setupRules.json import JSONReader
from src.buildGame import GameBuilder


def main(file_name):
    reader = JSONReader(file_name)
    builder = GameBuilder(reader)
    game = builder.setup()
    game.start_game()
    while game.is_ongoing:
        game.play_round()


if __name__ == '__main__':
    main(sys.argv[0])
