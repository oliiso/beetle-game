from random import randint
from dice import Dice
from build import Beetle


class Game:

    def __init__(self, player_list):
        self.players = player_list
        self.dice = Dice(randint(1,100))
        self.complete = False
        

    def turn(self):
        for player in self.players:
            roll = self.dice.roll_dice()
            player.turn(roll)
            print()
            print("{} rolled a {}".format(player.name, roll))
            if player.complete():
                if player.name != "":
                    print("Congrats! {} wins!".format(player.name))
                self.complete = True
                return


    def round(self):
        self.complete = False
        while not self.complete:
            self.turn() 
        print("GAME OVER, thank you for playing!")
        return



print("Welcome to the Beetle game!")
print("Roll a dice and be the first to build a full beetle!")
players = input("Input names of players with a space: ")
player_list = players.split()
beetle_list = []
for name in player_list:
    beetle_list.append(Beetle(name))
game = Game(beetle_list)
game.round()