# Author: Thomas
from global_variables import get_dollars


# It bids the average of every win_amount.
# Otherwise, it plays it all in if the average is too high or there are no wins.
class AverageBidingBot:
    def __init__(self):
        self.dollar = 0
        self.sum_of_win_amounts = 0
        self.general_wins = 0

    def play_round(self, winner, win_amount):
        self.dollar += get_dollars()
        if winner == 0:
            self.dollar -= win_amount
        if winner != -1:
            self.general_wins += 1
            self.sum_of_win_amounts += win_amount

        if self.general_wins == 0 or self.sum_of_win_amounts / self.general_wins > self.dollar:
            return self.dollar
        return self.sum_of_win_amounts / self.general_wins
