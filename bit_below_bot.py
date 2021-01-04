# Author: Kynigopoulos
from my_rand import MyRand
from global_variables import get_dollars


class BitBelowBot:
    def __init__(self):
        self.dollar = 0
        self.random = MyRand(123)

    def play_round(self, winner, win_amount):
        self.dollar += get_dollars()
        if winner == 0:
            self.dollar -= win_amount
        return self.dollar - self.random.randint(0, min(20, get_dollars()))
