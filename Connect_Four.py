import numpy as np

row_count = 6
column_count = 7
AB = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6}

def next_row(board, col):
    for r in range(row_count): 
        if board[r][col]==0:
            return r
            
def winning_move(board,piece):
    #horizontal win
    for c in range(column_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    #vertical locations
    for c in range(column_count):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    #positively sloped diagonals
    for c in range(column_count-3):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    #negatively sloped diagonals
    for c in range(column_count-3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
    
    
def who_is_winner(pieces_position_list):    
    board = np.zeros ((row_count,column_count))
    game_over = False
    
    while not game_over:
        turn = 0 if pieces_position_list[0][2:] == "Yellow" else 1
        
        for x in pieces_position_list:
            select =  AB[x[0]]
            if turn%2 == 0: 
                board[next_row(board,select),select] = 1 
                if winning_move(board,1):
                    return "Yellow"
            else:
                board[next_row(board,select),select] = 2
                if winning_move(board,2):
                    return "Red"
            turn += 1
            game_over = True
            
    return "Draw"  
    pass
