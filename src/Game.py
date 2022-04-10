from Battleship import Battleship
from model.Player import Player

import config, P1config, P2config
from model.Target import TargetTypes
from model.utility import utility

import sys


'''
Main class to start the game and play moves
Calls all the board validations and switch chances
between players depending upon the tagets hit or miss
In the end it returns message who won the game
'''

class Game():

    def __init__(self, board1, board2, p1, p2) -> None:

        self.start(board1, board2, p1, p2)
    

    def start(self, board1, board2, p1, p2):

        battleship1 = Battleship(board1, p1)
        if not battleship1:
            print("Simulation aborted")
            sys.exit()
        print("Validating P1 configuration: OK")
        battleship2 = Battleship(board2, p2)
        if not battleship2:
            print("Simulation aborted")
            sys.exit()
        print("Validating P2 configuration: OK")


    def playPlayerMove(self, player, opp_player, x, y):
        # Funtion to call takeChance for each player and its opponent
        # and print message according to the target result

        cell = [x, y]
        targetInfo = player.takeChance(opp_player, cell)
        
        if targetInfo == TargetTypes.HIT:
            return True
        elif targetInfo == TargetTypes.MISS:
            return False
        elif targetInfo == TargetTypes.SINK:
            return False
        elif targetInfo == TargetTypes.COMPLETE:
            msg = f"{player.name} won!"
            print(msg)
            return "abort"


if __name__ == '__main__':

    game_args = len(sys.argv)
    p1 = sys.argv[1]
    p2 = sys.argv[2]
    first_player = sys.argv[3]
    
    board1 = P1config.BOARD
    board2 = P2config.BOARD

    game = Game(board1, board2, p1, p2)
    print("Starting the game")
    print(f"{first_player} shoots first")
    p1 = Player(p1, board1)
    p2 = Player(p2, board2)

    if str(first_player) == "p1":
        player1 = p1
        player2 = p2
    else:
        player1 = p2
        player2 = p1

    i = 4
    while i < game_args:
        shot = sys.argv[i]
        y, x = list(shot)
        x = int(x)
        y_ind = utility.getIndexFromChar(str(y))
        result = game.playPlayerMove(player1, player2, x, y_ind)
        if result == "abort":
            break
        if not result:
            player1, player2 = player2, player1
        i += 1
