#author dimos

# counts the avarege money
class CounterBot():
    def __init__(self):
        self.players_money = [0] * 4

    def play_round(self, winner, win_amount):
        self.players_money = [d+500 for d in self.players_money]
        if winner != -1:
            self.players_money[winner] -= win_amount
        # avarage money of the other players
        s = sum(self.players_money) / 4
        if s > self.players_money[0]:
            return self.players_money[0]
        return s
