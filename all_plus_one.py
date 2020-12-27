#This bot bids multiples of 500 plus 1
class AllPlusOne:
    def __init__(self): 
      self.dollar = 0
      self.round = 0
      self.count500=  0

    def play_round(self, winner, win_amount):
        self.dollar += 500
        self.count500 += 1
        self.round += 1
        if winner == 0:
            self.dollar -= win_amount
            self.count500 = int(self.dollar/500)
        if (self.round == 10):
          return self.dollar
        
        return min( self.dollar,(self.count500-1)*500 +1 )