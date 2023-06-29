# players and their rolls, checked here with beetle
#one instance of Beetle for each of four players and ask the user for player names
 
import dice


class Beetle:
    #defining all parts of beetle and player name
    def __init__(self, name):
        self.name = name
        self.body = False
        self.head = False
        self.right_wing = False
        self.left_wing = False
        self.right_legs = False
        self.left_legs = False
        self.right_antenna = False
        self.left_antenna = False
        self.right_eye = False
        self.left_eye = False

# reads rolls and if correct is rolled part of beetle is added to person
    def turn(self, roll):
        if not self.body and roll == 1:
            print("body is built.")
            self.body = True
            return True
        if not self.head and roll == 2:
            print("head is built.".format(self.name))
            self.head = True
            return True
        if not self.right_legs and roll == 3:
            print("right legs are built.".format(self.name))
            self.right_legs = True
            return True
        if not self.left_legs and roll == 3:
            print("left legs are built.".format(self.name))
            self.left_legs = True
            return True
        if not self.right_wing and roll == 4:
            print("right wing is built.".format(self.name))
            self.right_wing = True
            return True
        if not self.left_wing and roll == 4:
            print("left wing is built.".format(self.name))
            self.left_wing = True
            return True
        if not self.right_antenna and roll == 5:
            print("right antenna is built.".format(self.name))
            self.right_antenna = True
            return True
        if not self.left_antenna and roll == 5:
            print("left antenna is built.".format(self.name))
            self.left_antenna = True
            return True
        if not self.right_eye and roll == 6:
            print("right eye is built.".format(self.name))
            self.right_eye = True
            return True
        if not self.left_eye and roll == 6:
            print("left eye is built.".format(self.name))
            self.left_eye = True
            return True
        return False
        

# prints parts of beetle that person has
    def print(self):
        print(self)

    def complete(self):
        if True:
            return (self.body and self.head and self.right_wing and self.left_wing and self.right_legs and self.left_legs and self.right_antenna and self.left_antenna and self.right_eye and self.left_eye)


class Dice_roll:
    def turn(self, roll_dice):
        out = Beetle.turn(self, roll_dice)
        return out
    