class AllInHalfBot:
    def __init__(self):
        self.dollar = 0
        self.time_to_bid = True

    def play_round(self, winner, win_amount):
        self.dollar += 500
        if winner == 0:
            self.dollar -= win_amount

        if self.time_to_bid:
            bid = self.dollar
        else:
            bid = 0
        self.time_to_bid = not self.time_to_bid
        return bid
