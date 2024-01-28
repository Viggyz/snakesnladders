from enum import Enum, auto
import logging
from typing import List

from .board import Board
from .player import Player
from .dice_strategy.base import BaseDiceStrategy

logger = logging.getLogger('Main')

class GameState(Enum):
    NOT_STARTED = auto()
    ONGOING = auto()
    ENDED = auto()

class Game:
    def __init__(self, board: Board, dice_roll_strategy: BaseDiceStrategy, players: List[Player]):
        self.board = board
        self.dice_strategy = dice_roll_strategy
        self.players = players
        self._game_state = GameState.NOT_STARTED

    def start_game(self):
        assert self._game_state is GameState.NOT_STARTED
        logger.info('Starting game...')
        self._game_state = GameState.ONGOING
        self.rounds = 0

    def end_game(self):
        assert self._game_state is GameState.ONGOING
        self._game_state = GameState.ENDED
        # Some kind of log to say game is done

    def play_round(self):
        if self._game_state == GameState.NOT_STARTED:
            print('Start game before playing a round')
            return
        if self._game_state == GameState.ENDED:
            print('Game has ended, try starting a new game')
            return
        self.rounds += 1
        logger.info("-- Starting Round %d --", self.rounds)
        for player in self.players:
            assert self.board.is_player_on_board(player)
            pos_delta, msg = self.dice_strategy.roll_dice()
            logger.info(f"{player}"+msg)
            has_won = self.board.move_player(player, pos_delta)
            if has_won: # Could refactor to diff rule where we wait till all but last player completes
                logger.info('-x-x- %s has won the game -x-x-', str(player))
                self.end_game()
                break
                # Should be logging the tile message too

    @property
    def is_ongoing(self):
        return self._game_state == GameState.ONGOING
