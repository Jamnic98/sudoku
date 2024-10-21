import numpy as np

from app.board import Board


class TestBoard:
    def test_board_is_full(self):
        test_board = Board(np.ones(Board.BOARD_SIZE, dtype='int'))
        assert test_board.is_board_full() is True
        test_board.board_state[0][0] = 0
        assert test_board.is_board_full() is False

    def test_update_board(self):
        test_board = Board()
        test_board.update((0, 0), 1)
        assert test_board.board_state[0][0] == 1
        test_board.update((0, 0), -1)
        assert test_board.board_state[0][0] == 1
