# author thomas

# bids the half of the existing money instead of last round that goes all in
class HalfInBot:
    def __init__(self):
        self.dollar = 0
        self.rounds=0

    def play_round(self, winner, win_amount):
        self.rounds+=1
        self.dollar += 500
        if winner == 0:
            self.dollar -= win_amount
        if self.rounds==10: return self.dollar
        return self.dollar/2