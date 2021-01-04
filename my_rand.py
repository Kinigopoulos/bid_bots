# This class is used only for generating random numbers with a specific seed
class MyRand:
    def __init__(self, seed):
        self.val = seed

    def randint(self, a, b):
        self.val = (self.val * 6364136223846793005 + 1) % (1 << 64)
        return (self.val >> 32) % (b - a + 1) + a

    @staticmethod
    def randint_with_seed(a, b, seed):
        return (seed >> 32) % (b - a + 1) + a
