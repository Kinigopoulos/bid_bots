# Author: Kynigopoulos
from global_variables import get_dollars, get_rounds


# Returns its money divided by the round it is playing
class AverageBot:
    def __init__(self):
        self.dollar = 0
        self.round = get_rounds() + 1

    def play_round(self, winner, win_amount):
        self.dollar += get_dollars()
        self.round -= 1
        if winner == 0:
            self.dollar -= win_amount
        return self.dollar / self.round
