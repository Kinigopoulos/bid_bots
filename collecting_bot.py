# author dimos


# collects money for 2 rounds and go all in
class CollectingBot():
    def __init__(self):
        self.money = 0
        self.wins = []
        self.round = 0

    def play_round(self, winner, win_amount):
        self.money += 500
        self.round += 1

        if winner==0:
            self.money -= win_amount
            self.wins.append(self.round)
        # after 2 non winning rounds go all in
        last_win = 0
        if len(self.wins) > 0:
            last_win = self.wins[-1]

        if self.round - last_win > 2:
            return self.money
        return 0

