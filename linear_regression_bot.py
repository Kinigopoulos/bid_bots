# Author: Thomas
from my_rand import MyRand
from global_variables import get_dollars, get_rounds, get_players


# Tries with linear regression like machine learning to find a relation like
# Y=a+bX with Y representing the winning biding amount and X the current budget.
class LinearRegressionBot:

    def __init__(self):
        self.players_money = [0] * get_players()
        self.a = 0
        self.b = MyRand(123).randint(5, 9) / 10  # starting with a relation to avoid ties
        self.budget_of_winners = []
        self.winners_biding = []
        self.round = 0

    def two_different_budgets(self):
        for value in self.budget_of_winners[1:]:
            if value != self.budget_of_winners[0]:
                return True
        return False

    def linear_regression_bid(self):
        X = self.players_money[0]  # current budget
        Y = self.a + self.b * X  # winning biding amount
        if Y <= 0:
            return 0  # cause you can't bid smaller than 0
        return min(X, Y) if self.round < get_rounds() else X  # if it can't afford Y or it is the final round it
        # plays it all in

    def calculating_relation(self):
        mean_budget = sum(self.budget_of_winners) / len(self.budget_of_winners)
        mean_biding = sum(self.winners_biding) / len(self.winners_biding)
        numerator = 0
        denominator = 0
        for i in range(len(self.budget_of_winners)):
            numerator += (self.budget_of_winners[i] - mean_budget) * (self.winners_biding[i] - mean_biding)
            denominator += pow(self.budget_of_winners[i] - mean_budget, 2)
        self.b = numerator / denominator
        self.a = mean_biding - self.b * mean_budget

    def play_round(self, winner, win_amount):
        self.round += 1
        self.players_money = [d + get_dollars() for d in self.players_money]
        if winner == -10:
            print("I don't know what I am doing")
        elif winner != -1:
            self.budget_of_winners.append(
                self.players_money[winner] - get_dollars())  # saves the budget that winner had the last turn
            self.winners_biding.append(win_amount)  # saves the win_amount of the winner
            self.players_money[winner] -= win_amount

        # we need at least 2 different winning budgets to do a linear regression
        if self.two_different_budgets():
            self.calculating_relation()
        return self.linear_regression_bid()
