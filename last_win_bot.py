# Author: Dimos
from global_variables import get_dollars


# Bids the amount of the last win, if it has enough money
class LastWinBot:
    def __init__(self):
        self.money = 0

    def play_round(self, winner, win_amount):
        self.money += get_dollars()
        if winner == 0:
            self.money -= win_amount
        if self.money >= win_amount:
            return max(0, win_amount)
        return 0
