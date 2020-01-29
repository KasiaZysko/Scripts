""" This is simple Tick-Tack-Toe game to play with computer. "

from random import randrange

#Definition of board t
boards = [[1,2,3],[4,5,6],[7,8,9]]
FreeSpace = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def DisplayBoard(board):
# the function accepts one parameter containing the board's current status
# and prints it out to the console

    for x in range(0,3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ",board[x][0],"  |  ",board[x][1],"  |  ",board[x][2],"  |")
        print("|       |       |       |")
    print("+-------+-------+-------+")
       
def EnterMove(board):
# the function accepts the board current status, asks the user about their move,
# checks the input and updates the board according to the user's decision

    while True:
        numO = input("Enter your move:")
        if int(numO) in range(1,10):
            posx = (int(numO)- 1)//3
            posy = (int(numO)-1)-3*posx
            if (posx,posy) in FreeSpace:
                board[posx][posy] = "O"
                FreeSpace.remove((posx,posy))
                break
def XMove(board):
# the function browses the board and builds a list of all the free squares;
# the list consists of tuples, while each tuple is a pair of row and column numbers

    while True:
        numX = randrange(8)
        Xposx = (int(numX)- 1)//3
        Xposy = (int(numX)-1)-3*Xposx
        if (Xposx,Xposy) in FreeSpace:
            FreeSpace.remove((Xposx,Xposy))
            board[Xposx][Xposy] = "X"
            break


def win_indexes(n):
  #Function check what are win indexes for this type of board.
    # Rows
    for r in range(n):
        yield [(r, c) for c in range(n)]
    # Columns
    for c in range(n):
        yield [(r, c) for r in range(n)]
    # Diagonal top left to bottom right
    yield [(i, i) for i in range(n)]
    # Diagonal top right to bottom left
    yield [(i, n - 1 - i) for i in range(n)]


def Winner(board, decorator):
#check who is the winner
    n = len(board)
    for indexes in win_indexes(n):
        if all(board[r][c] == decorator for r, c in indexes):
            print("Winner is {}".format(decorator))
            return True
    return False
    
#actual game loop   
for x in range(6):
    while True:
        XMove(boards)
        DisplayBoard(boards)
        EnterMove(boards)
        DisplayBoard(boards)
        if Winner(boards, "X")or Winner(boards, "O"):
            break
        else:
            print("Noone wins!")
            break
