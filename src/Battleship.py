from collections import defaultdict

import config, P1config, P2config
from model.ShipTypes import ShipTypes
from model.utility import utility


'''
Class to validate the boards configuration for each player
Has methods to check various validations and print messages accordingly
Returns True or False whether the Board was validated or not
'''


class Battleship():

    def __init__(self, board, player) -> None:

        self.validate = self.boardValidation(board, player)
    

    def __bool__(self):

        if self.validate:
            return True
        return False


    def printValidationFailed(self, player):
        print(f"Validating {player} configuration: FAIL")


    def printValidationMsg(self, reason, p=None, x1=None, y1=None, x2=None, y2=None, len_=None):

        # This funtion prints defined messages for each case of wrong board configuration

        if reason == "wrong_unit":
            self.printValidationFailed(p)
            y1 = utility.getCharFromIndex(y1)
            y2 = utility.getCharFromIndex(y2)
            print(f"{p} has unrecognized {len_}-unit ship at {y1}{x1}-{y2}{x2}")

        elif reason == "cross":
            self.printValidationFailed(p)
            y1 = utility.getCharFromIndex(y1)
            print(f"{p} has overlapping ships at {y1}{x1} position")

        elif reason == "position":
            self.printValidationFailed(p)
            y1 = utility.getCharFromIndex(y1)
            print(f"{p} has ship with wrong orientation at {y1}{x1} position")


    def boardValidation(self, board, p):

        # Function with core logic to validate the boards
        # Return True or False to the caller to say whether board 
        # was validated or not

        dim1 = P1config.DIMENSIONS
        dim2 = P2config.DIMENSIONS
        self.validateDimensions(dim1, dim2)
        
        ships = []
        color = {}

        ship_types = ShipTypes()
        ships = [value for attr, value in ship_types.__dict__.items()]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if (all(ship[1] == 0 for ship in ships) and board[i][j]):
                    return False
                if (not color.get(f"{i},{j}") and board[i][j]):
                    if not self.searchShips(p, i, j, board, color, ships):
                        return False
        
        return all(list(ship[1] == 0 for ship in ships))


    def searchShips(self, player, x, y, board, color, ships):

        # Function to validate the placement and correct counts of different 
        # types of ships on the board. Returns True or False to the caller

        # ship should not be in contact with other ship in corner
        if x < P1config.DIMENSIONS[0]-1 and y < P1config.DIMENSIONS[1]-1:
            utility.isCornerContact(player, board, x, y)
        
        s = n = m = 0
        for s in range(len(ships)-1):
            # Check for horizontal orientation
            for n in range(len(board[x])):
                if not (y+n < len(board[x])) or board[x][y + n] == 0:
                    break
                # The ship cannot be in contact with any other ship
                if (n > 0 and board[x + 1] and board[x + 1][y + n]):
                    self.printValidationMsg("cross", player, x+1, y+n)
                    return False
                color[f"{x},{y + n}"] = 1
            # Check for vertical orientation
            for m in range(len(board)):
                if not (x+m < len(board)) or board[x + m][y] == 0:
                    break
                # The ship cannot be in contact with any other ship
                if m > 0 and board[x + m][y + 1]:
                    self.printValidationMsg("cross", player, x+m, y+1)
                    return False
                color[f"{x + m},{y}"] = 1
        
        # Reduce count for a ship
        max_ = max(n, m)
        if max_ and not utility.lengthExist(ships, max_):
            if max_ == n:
                self.printValidationMsg("wrong_unit", player, x, y, x, y+n, n)
                return False
            if max_ == m:
                self.printValidationMsg("wrong_unit", player, x+m, y, x+m, y, m)
                return False
        ships[max_ - 1][1] -= 1
        if n > 1 and m > 1:
            self.printValidationMsg("position", player, n, m)
            return False
        
        # Update and replace "S" with ship name on the board for easy tracking
        if max_ == n:
            utility.updateShipName(board, x, y, n, ships[max_ - 1][2], True)
        if max_ == m:
            utility.updateShipName(board, x, y, m, ships[max_ - 1][2])

        return True

    
    def validateDimensions(self, dim1, dim2):

        if not dim1[0] or dim1[0] < config.MIN_Y_DIMENSION or not dim1[1] or dim1[1] < config.MIN_X_DIMENSION:

            raise ValueError("Dimensions should be more than 8 unit")

        if not dim2[0] or dim2[0] < config.MIN_Y_DIMENSION or not dim2[1] or dim2[1] < config.MIN_X_DIMENSION:

            raise ValueError("Dimensions should be more than 8 unit")

