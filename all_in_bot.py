class AllInBot:
    def __init__(self): self.dollar = 0

    def play_round(self, winner, win_amount):
        self.dollar += 500
        if winner == 0:
            self.dollar -= win_amount
        return self.dollar
