# Author: Thomas
from global_variables import get_dollars, get_rounds


# This bot persists to win with get_dollars()*2+1. It's economical and tricky amount cause the opponents
# need to charge 3 turns to beat this bid.
# In the final round bot stops being persistent and bids all the money.
class PersistentBot:
    def __init__(self):
        self.dollar = 0
        self.win_with_this = get_dollars()*2+1
        self.round = 0

    def play_round(self, winner, win_amount):
        self.round += 1
        self.dollar += get_dollars()
        if winner == 0:
            self.dollar -= win_amount
        if self.round == get_rounds():
            self.win_with_this = self.dollar
        return self.win_with_this if self.dollar >= self.win_with_this else 0
