from app.sudoku import Sudoku
from app.board import Board

def main():
    # sudoku = Sudoku()
    # sudoku.run()
    board = Board()
    x = board.generate_sudoku()
    print(x)


if __name__ == '__main__':
    main()
