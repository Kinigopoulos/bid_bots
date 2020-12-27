# author thomas

# this bot persists to win with 1001. It's a tricky amount cause the opponents need to charge
# 3 turns to beat this bid. Also, it's very economical instead of biding 1250 and 1500.
# In the final round bot stops being persistent and bids all the money.
class PersistentBot:
    def __init__(self):
        self.dollar = 0
        self.win_with_this=1001
        self.round=0

    def play_round(self, winner, win_amount):
        self.round+=1
        self.dollar += 500
        if winner == 0:
            self.dollar -= win_amount
        if self.round==10:
            self.win_with_this=self.dollar
        return self.win_with_this if self.dollar>=self.win_with_this else 0