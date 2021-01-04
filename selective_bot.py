# Author: Thomas
from my_rand import MyRand
from global_variables import get_dollars, get_players, get_rounds


# selects every turn a behaviour from all-in,half-in, average bit_below and zero
# according to which way is more winnable.
# if there is a winning tie, the behaviour is random.
# in 10th round it selects the behaviour all in because there's a risk to have a surplus money.

class SelectiveBot:
    # 1 means all in,0.5 means half in, 0 means biding 0 and all the other situations are "not specific value".
    keys = [1, 0.5, "not specific value", 0]  # keys represent the value win_amount/winner_player_money

    def allin(self):
        return self.players_money[0]

    def halfin(self):
        return self.players_money[0] / 2

    def bit_below(self):
        average_bit_bellow = self.sumof_bit_bellow_values / self.behaviours["not specific value"][0]
        return self.players_money[0] - average_bit_bellow

    def zero(self):
        return 0

    def __init__(self):
        self.random = MyRand(123)
        self.round = 0
        self.players_money = [0] * get_players()
        self.sumof_bit_bellow_values = 0  # sum of all bit_below_values that won
        self.behaviours = {
            1: [0, self.allin],  # first value is the winning counter of this behaviour in the specific auction.
            0.5: [0, self.halfin],
            "not specific value": [0, self.bit_below],
            0: [0, self.zero]
        }

    def play_round(self, winner, win_amount):
        self.round += 1
        self.players_money = [d + get_dollars() for d in self.players_money]

        if winner == -10:
            print("I don't know what I am doing")
        elif winner != -1:
            self.winning_behaviour_inturn = win_amount / (
                        self.players_money[winner] - get_dollars())  # the behaviour of the recent winner
            if self.winning_behaviour_inturn != 1 and self.winning_behaviour_inturn != 0.5 and self.winning_behaviour_inturn != 0:
                self.winning_behaviour_inturn = "not specific value"
                self.sumof_bit_bellow_values += (self.players_money[
                                                     winner] - get_dollars()) - win_amount  # the needed bit bellow value to win
            self.players_money[winner] -= win_amount
            self.behaviours[self.winning_behaviour_inturn][0] += 1  # adding 1 to the winning behaviour of this turn

        if self.round == get_rounds():
            return self.players_money[0]  # default all in acting if it is the final round.

        max_wins = max(
            [self.behaviours[key][0] for key in self.keys])  # the max_wins that have been with 1 or more behaviours
        winnable_behaviours = []  # saves all the behaviours that won max_wins times.

        for key in self.keys:
            if self.behaviours[key][0] == max_wins:
                winnable_behaviours.append(key)

        # ideally it's only one the winnable behaviour but if it isn't the chosen behaviour will be randomly.
        chosen_behaviour = winnable_behaviours[self.random.randint(0, len(winnable_behaviours) - 1)]

        return self.behaviours[chosen_behaviour][1]()
