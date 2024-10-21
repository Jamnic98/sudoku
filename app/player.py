import random
from enum import Enum

from random import sample

import numpy as np
from numpy.random import randint



class ComputerIntelligence(Enum):
    DUMB = "low"
    SMART = "high"


class Player:
    def __init__(self):
        pass

    def make_move(self, board: np.array):
        try:
            print('Enter co-ords:')
            player_input = input()
            x, y = map(int, player_input.split(','))

            print('Enter value:')
            val = int(input().strip())
            board.update((x, y), val)

        except (ValueError, IndexError):
            print('Error, try again')


class AI(Player):
    def __init__(self, ai_intelligence=ComputerIntelligence.DUMB):
        super().__init__()
        self.ai_intelligence = ai_intelligence

    def make_move(self, board):
        if self.ai_intelligence == ComputerIntelligence.DUMB:
            x, y, val = self.__random_move(board)
            board.update((x, y), val)

        elif self.ai_intelligence == ComputerIntelligence.SMART:
            pass

    @staticmethod
    def __random_move(board):
        while True:
            available_co_ords = []
            for x in range(9):
                for y in range(9):
                    if board.is_square_empty((x,y)):
                        available_co_ords.append((x,y))

            co_ords = random.choice(available_co_ords)
            existing_values = []
            if board.is_square_empty(co_ords):
                existing_values.extend(board.get_corresponding_row(co_ords))
                existing_values.extend(board.get_corresponding_col(co_ords))
                existing_values.extend(board.get_corresponding_big_square(co_ords).flatten())
                a = [x for x in existing_values if x != 0]
                s = [x for x in range(1, 10) if x not in set(a)]

                if len(s) != 0:
                    break

        return co_ords[0], co_ords[1], random.choice(s)
