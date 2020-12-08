class AverageBot:
    def __init__(self):
        self.dollar = 0
        self.round = 11

    def play_round(self, winner, win_amount):
        self.dollar += 500
        self.round -= 1
        if winner == 0:
            self.dollar -= win_amount
        return self.dollar / self.round
