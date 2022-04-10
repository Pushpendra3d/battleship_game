"""
Config file to have the configurations for the board.
2 Dimensions are defined as rectangular boundary with N and M as
the row and column of the 2D matrix. The board matrix has ships in defined
position. "" means empty value and "S" means there is a ship on the specific position.
"""

N = 10
M = 10

DIMENSIONS = [N, M]

BOARD = [
        # A, B, C, D, E, F, G, H, I, J
        [ 0,0,0,0,0,"S",0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0 ],
        [ 0,"S","S",0,0,0,0,0,0,0 ],
        [ 0,0,0,0,"S","S","S","S",0,0 ],
        [ "S",0,0,0,0,0,0,0,0,0 ],
        [ "S",0,0,"S","S",0,0,0,0,0 ],
        [ "S",0,0,0,0,0,0,"S","S","S" ],
        [ 0,0,"S","S",0,0,0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0 ],
        [ 0,0,0,"S",0,"S",0,"S",0,0 ]
    ]