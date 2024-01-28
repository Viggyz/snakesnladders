import sys
import logging

from src.setupRules.json import JSONReader
from src.buildGame import GameBuilder

logger = logging.getLogger('Main')
logger.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)

def main(file_name):
    reader = JSONReader(file_name)
    builder = GameBuilder(reader)
    game = builder.setup()
    game.start_game()
    while game.is_ongoing:
        game.play_round()


if __name__ == '__main__':
    main(sys.argv[1])

