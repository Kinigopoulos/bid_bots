# Author: Dimos
from global_variables import get_dollars, get_players


# counts the average money
class CounterBot:
    def __init__(self):
        self.players_money = [0] * get_players()

    def play_round(self, winner, win_amount):
        self.players_money = [d + get_dollars() for d in self.players_money]
        if winner == -10:
            self.players_money[1] -= win_amount
        elif winner != -1:
            self.players_money[winner] -= win_amount
        # average money of the other players
        s = sum(self.players_money) / len(self.players_money)
        if s > self.players_money[0]:
            return self.players_money[0]
        return s
