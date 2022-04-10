from .keys import CHARTOINDEX


def isCornerContact(p, board, x, y):

    if ((board[x - 1] and (board[x - 1][y - 1] or board[x - 1][y + 1])) or 
        (board[x + 1] and (board[x + 1][y - 1] or board[x + 1][y + 1]))):

        y_ind = getCharFromIndex(y)
        print(f"{p} has overlapping ships at {y_ind}{x} position")

        return True
    return False


def lengthExist(table, k):

    for data in table:
        if data[0] == k:
            return True
    return False


def getCharFromIndex(ind):

    return CHARTOINDEX[ind]


def getIndexFromChar(char):

    return CHARTOINDEX.index(char)


def updateShipName(board, x, y, increment, name, horizontal=False):

    if horizontal:
        for i in range(increment):
            board[x][y+i] = str(name)
    else:
        for i in range(increment):
            board[x+i][y] = str(name)        

