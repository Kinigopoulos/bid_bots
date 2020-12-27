#Doesn't expect to win on the 5 first rounds and bids amounts to mess with other bots.
#After that it goes for the ol'reliable 1002.
#Has a safety net with min() in case things go south.
class ThornOnMySide:
    def __init__(self): 
      self.dollar = 0
      self.round = 0

    def play_round(self, winner, win_amount):
        self.dollar += 500
        self.round += 1
        if winner == 0:
          self.dollar -= win_amount
        if self.round == 1:
          return 0
        elif self.round ==2:
          return min(self.dollar,1000)
        elif self.round ==3:
          return min(self.dollar,1001)
        elif self.round ==4:
          return min(self.dollar,2000)
        elif self.round == 5:
          return min(self.dollar,1001)
        elif self.round == 10:
          return self.dollar
        return min(self.dollar,1002)
