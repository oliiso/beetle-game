 
import random 

class Dice:
    def __init__(self, seed):
        random.seed(seed)
        self.roll = 1
    def roll_dice(self):
        self.roll = random.randint(1, 6)
        return self.roll
    