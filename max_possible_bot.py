# Author: Thomas
from global_variables import get_dollars


# Bids the largest win_amount from the previous turns that can afford else it plays it all in.
class MaxPossibleBot:
    def __init__(self):
        self.dollar = 0
        self.win_amounts = []
        self.round = 0

    def max_win_amount_bid(self):
        self.win_amounts.sort(reverse=True)  # sorting the win_amounts from the highest to lowest
        for win_amount in self.win_amounts:
            if win_amount <= self.dollar:  # if it's possible it bids this past win_amount
                return win_amount
        return self.dollar  # bot can't bid from the previous win_amounts so it goes all in

    def play_round(self, winner, win_amount):
        self.round += 1
        self.dollar += get_dollars()
        if winner != -1:
            self.win_amounts.append(win_amount)  # adding from the current winner his win_amount
            if winner == 0:
                self.dollar -= win_amount
        return self.max_win_amount_bid()
