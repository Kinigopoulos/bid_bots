# Author: Thomas
from my_rand import MyRand
from global_variables import get_dollars, get_players


# Goes all in if no one of the opponents have the same amount of money
# or it bids something randomly a bit lower to avoid any ties.
class NoTieBot:
    def __init__(self):
        self.players_money = [0] * get_players()
        self.random = MyRand(123)

    def play_round(self, winner, win_amount):
        self.players_money = [d + get_dollars() for d in self.players_money]
        if winner == -10:
            self.players_money[self.random.randint(1, get_players() - 1)] -= win_amount
        elif winner != -1:
            self.players_money[winner] -= win_amount

        if self.players_money[0] in self.players_money[1:]:
            return self.players_money[0] - self.random.randint(1, 10)
        return self.players_money[0]
