from app.board import Board
from app.player import Player, AI

class Sudoku:
    def __init__(self, player_count=0):
        self.running = False
        self.board = Board()
        self.player = Player() if player_count == 1 else AI()

    def run(self):
        self.running = True
        self.board.draw_board()
        while self.running:
            self.player.make_move(self.board)
            self.board.draw_board()
            if self.is_game_over():
                self.game_over()

    def get_next_move(self):
        self.player.make_move(self.board)

    def is_game_over(self):
        return self.board.is_board_full()

    def game_over(self):
        self.running = False
        print('Game Over')
