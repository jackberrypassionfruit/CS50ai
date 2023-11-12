"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    cnt_x = 0
    cnt_o = 0
    for row in board:
        for cell in row:
            if cell == 'X':
                cnt_x += 1
            elif cell == 'O':
                cnt_o += 1
    
    # print('cnt_x: ', cnt_x, 'cnt_o: ', cnt_o)
    if cnt_x == cnt_o:
        return 'X'
    elif cnt_x == cnt_o+1:
        return 'O'
    else:
        raise Exception
                

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    poss = set()
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                poss.add((i, j))
                
    return poss


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    next_player = player(board)
    new_board = copy.deepcopy(board)
    
    new_board[action[0]][action[1]] = next_player
    return new_board
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    """ Check for Horizonal winners """

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    """ Check for Vertical winners """
    for col_num in range(3):
        if board[0][col_num] == board[1][col_num] == board[2][col_num] and board[0][col_num] is not EMPTY:
            return board[0][col_num]


    """ Check for Diagonal Winners """
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0] and board[1][1] is not EMPTY:
        return board[1][1]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    return winner(board) or not any([EMPTY in row for row in board])
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    win_check = winner(board)
    if win_check == X:
        return 1
    elif win_check == O:
        return -1
    else: 
        return 0
    

# next 2 are helper functions for minimax()
def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -1 # Ideally would make v = -inf, but -1 is the lowest the utility can go so I don't care
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = 1 # Ideally would make v = inf, but 1 is the highest the utility can go so I don't care
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v

def minimax(board):
    if terminal(board):
        return None
    current_player = player(board)
    if current_player == X:
        v = -1
        for action in actions(board):
            util = minValue(result(board, action))
            if util > v:
                v = util
                next_move = action
    elif current_player == O:
        v = 1
        for action in actions(board):
            util = maxValue(result(board, action))
            if util < v:
                v = util
                next_move = action
    return next_move