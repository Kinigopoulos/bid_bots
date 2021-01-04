# Author: Kynigopoulos
from my_rand import MyRand
from global_variables import get_dollars


class RandomBot:
    def __init__(self):
        self.dollar = 0
        self.random = MyRand(1)

    def play_round(self, winner, win_amount):
        self.dollar += get_dollars()
        if winner == 0:
            self.dollar -= win_amount
        return self.random.randint(0, self.dollar)
