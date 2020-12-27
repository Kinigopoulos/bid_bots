#This bot aspires to win the first round by bidding 499. Will continue to go all-in minus 1 to avoid conflict until it has won.
#Then it will just go all-in.
class attackBot:
    def __init__(self): 
      self.dollar = 0
      self.round = 0
      self.hasWon = False

    def play_round(self, winner, win_amount):
      self.dollar +=500
      self.round += 1
      if winner == 0:
        self.dollar -= win_amount
        self.hasWon = True

      if self.round == 10:
        return self.dollar

      if self.hasWon == False:
        return self.dollar - 1
      else:
        return self.dollar

