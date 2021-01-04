# Author: Kynigopoulos
from global_variables import get_dollars


# This bod bids everything everytime.
class AllInBot:
    def __init__(self):
        self.dollar = 0

    def play_round(self, winner, win_amount):
        self.dollar += get_dollars()
        if winner == 0:
            self.dollar -= win_amount
        return self.dollar
