from random import shuffle

import numpy as np
from app.player import AI

BOARD_SIZE = 9, 9

def test_for_dupes(arr: np.array):
    arr = arr[arr != 0]
    return len(arr) != len(set(arr))


class Board:
    def __init__(self, initial_board_state: np.array = np.zeros(BOARD_SIZE, dtype='int')):
        self.board_state = initial_board_state

    @classmethod
    def __test_rows(cls, board_state: np.array):
        return all(not test_for_dupes(board_state[:, i]) for i in range(9))

    @classmethod
    def __test_columns(cls, board_state: np.array):
        return all((not test_for_dupes(col) for col in board_state))

    @classmethod
    def __test_big_squares(cls, board_state: np.array):
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                big_square = board_state[x:x + 3, y:y + 3]
                if test_for_dupes(big_square.flatten()):
                    return False
        return True

    def update(self, co_ords: (int, int), value: int) -> bool:
        try:
            x, y = co_ords
            if not value in range(1, 10) or self.board_state[x][y] != 0:
                return False
            board_copy = self.board_state.copy()
            board_copy[x][y] = value
            if not all((
                    self.__test_rows(board_copy),
                    self.__test_columns(board_copy),
                    self.__test_big_squares(board_copy)
            )):
                return False
        except IndexError:
            return False
        else:
            self.board_state[x][y] = value
            return True

    def is_square_empty(self, co_ords: (int, int)) -> bool:
        x, y = co_ords
        return self.board_state[x][y] == 0

    def is_board_full(self) -> bool:
        return not np.any(self.board_state == 0)

    def draw_board(self):
        for row in self.board_state.T.tolist().__reversed__():
            for val in row:
                print(val if val != 0 else ' ', end='', sep='')
            print()
        print()

    def get_corresponding_row(self, co_ords: (int, int)) -> np.array:
        _, y = co_ords
        return self.board_state[:][y]

    def get_corresponding_col(self, co_ords: (int, int)) -> np.array:
        x, _ = co_ords
        return self.board_state[x][:]

    def get_corresponding_big_square(self, co_ords: (int, int)) -> np.array:
        def get_i(a):
            if a < 3:
                return 0
            if a < 6:
                return 1
            if a < 9:
                return 2

        x, y = co_ords
        i = get_i(x)
        j = get_i(y)
        return self.board_state[i:i+3][j:j+3]

    def get_fill_percentage(self) -> int:
        flat_board = self.board_state.flatten()
        return int((len(flat_board[flat_board != 0]) / BOARD_SIZE[0]**2) * 100)

    @staticmethod
    def generate_end_game_boards(board_count=1):
        new_boards = []
        player = AI()
        while len(new_boards) < board_count:
            new_board = Board(np.zeros(BOARD_SIZE, dtype='int'))
            i = 0
            while True:
                if i == 1000:
                    break

                player.make_move(new_board)
                fill_percent = new_board.get_fill_percentage()
                if fill_percent >= 10:
                    print(new_board.board_state)

                if new_board.is_board_full():
                    new_boards.append(new_board)

                i += 1

    def is_valid(self, grid, row, col, num):
        # Check if num is not in current row, column and 3x3 subgrid
        for x in range(9):
            if grid[row][x] == num or grid[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    # Recursive function to fill the board
    def fill_board(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.fill_board(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    # Generate a Sudoku board
    def generate_sudoku(self):
        grid = [[0] * 9 for _ in range(9)]
        self.fill_board(grid)
        return grid
