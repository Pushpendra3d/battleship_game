from .Board import Board
from .Target import TargetTypes

'''
Player class to play move by taking targets
player take targets on opposition player and gets
target information from opposition player
'''

class Player:

    def __init__(self, name, board) -> None:

        self.name = name
        self.board = Board(board)
    

    def takeChance(self, opp_player, cell):

        # shoot target to another board
        return self.shootTarget(opp_player, cell)
    

    def shootTarget(self, opp_player, cell):

        result = self.targetInfo(opp_player, cell)
        return result
    

    def targetInfo(self, opp_player, cell):

        # get target info from other player
        # whether its is a hit ot miss or ship destroyed
        return opp_player.board.targetInfo(cell)
