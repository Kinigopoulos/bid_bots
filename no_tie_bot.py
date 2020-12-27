# author thomas


from my_rand import MyRand


# goes all in if noone of the opponents have the same amount of money
# or it bids something randomly a bit lower to avoid any ties.
class NoTieBot:
    def __init__(self):
        self.players_money = [0] * 4
        self.random=MyRand(123)

    def play_round(self, winner, win_amount):
        self.players_money = [d + 500 for d in self.players_money]
        if winner != -1:
            self.players_money[winner] -= win_amount
        return self.players_money[0]-self.random.randint(1,10) if (self.players_money[0] in self.players_money[1:]) else self.players_money[0]