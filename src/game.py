from enum import Enum, auto
from typing import List

from board import Board
from player import Player
from dice_strategy.base import BaseDiceStrategy

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
        self._game_state = GameState.ONGOING

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
        for player in self.players:
            assert self.board.is_player_on_board(player)
            pos_delta = self.dice_strategy.roll_dice()
            has_won = self.board.move_player(pos_delta)
            if has_won: # Could refactor to diff rule where we wait till all but last player completes
                self.end_game()
                break
                # Should be logging the tile message too

    @property
    def is_ongoing(self):
        return self._game_state == GameState.ONGOING
