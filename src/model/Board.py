from .Target import TargetTypes
from .utility import utility


class Board():

    """
    Class Board with all the information regarding the remaining and 
    destroyed ships. Have methods to check whether the ship target was hit or
    miss and return the information to the caller
    """

    def __init__(self, board) -> None:

        self.board = board
    

    def targetInfo(self, cell):

        if self.board[cell[0]][cell[1]]:

            ship_type = self.board[cell[0]][cell[1]]
            self.board[cell[0]][cell[1]] = 0
            count = 0
            N = len(self.board)
            M = len(self.board[0])
            n = cell[0]
            m = cell[1]

            # Ship destroyed logic TODO
            if ship_type:
                if n == N-1 and m == M-1:
                    print(self.allShipsSunk(cell[0], cell[1], ship_type))
                elif n == N-1 and not(self.board[n-1][m] or self.board[n][m-1] or self.board[n][m+1]):
                    print(self.allShipsSunk(cell[0], cell[1], ship_type))
                elif m == M-1 and not(self.board[n-1][m] or self.board[n][m-1] or self.board[n+1][m]):
                    print(self.allShipsSunk(cell[0], cell[1], ship_type))
                elif n > 0 and n < N and m > 0 and not(self.board[n-1][m] or self.board[n+1][m] or self.board[n][m+1] or self.board[n][m-1]):
                    print(self.allShipsSunk(cell[0], cell[1], ship_type))
                elif m > 0 and m < M and n > 0 and not(self.board[n][m-1] or self.board[n][m+1] or self.board[n+1][m+1] or self.board[n-1][m]):
                    print(self.allShipsSunk(cell[0], cell[1], ship_type))
                elif n > 0 and n < N and not(self.board[n-1][m] or self.board[n+1][m] or self.board[n][m+1]):
                    print(self.allShipsSunk(cell[0], cell[1], ship_type))
                elif m > 0 and m < M and not(self.board[n][m-1] or self.board[n][m+1] or self.board[n+1][m+1]):
                    print(self.allShipsSunk(cell[0], cell[1], ship_type))
                elif not(self.board[n+1][m] or self.board[n][m+1]):
                    print(self.allShipsSunk(cell[0], cell[1], ship_type))
                else:
                    print(self.hitMessage(cell[0], cell[1], ship_type))
                    return TargetTypes.HIT

            for n in range(len(self.board)):
                for m in range(len(self.board[n])):
                    if self.board[n][m] == 0:
                        count += 1
            if count == len(self.board)*len(self.board):
                return TargetTypes.COMPLETE
        else:
            print(self.missMessage(cell[0], cell[1]))
            return TargetTypes.MISS


    def hitMessage(self, X, Y, ship_type):

        y_ind = utility.getCharFromIndex(Y)
        msg = f"{y_ind}{X} - {ship_type} hit"
        return msg


    def missMessage(self, X, Y):

        y_ind = utility.getCharFromIndex(Y)
        msg = f"{y_ind}{X} - Miss"
        return msg


    def allShipsSunk(self, X, Y, ship_type):

        y_ind = utility.getCharFromIndex(Y)
        msg = f"{y_ind}{X} - {ship_type} destroyed"
        return msg
