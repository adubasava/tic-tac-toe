"""
Tic Tac Toe Player
"""

import math
import copy

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
    if terminal(board):
        return None
    
    # Number of empty cells available
    empt = 0
    for i in board:
        for j in i:
            if j == None:
                empt = empt + 1
    
    # If odd number of empty cells remains - X, if even - O    
    if empt % 2 == 0:
        return O
    else:
        return X    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if winner(board) != None:
        return None
    
    actions = set()

    # Available empty cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i, j))

    if len(actions) == 0:
        return None
    else:
        return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """    
    
    new = copy.deepcopy(board)
    
    if action not in actions(board):
        raise Exception("Not allowed action")

    action = list(action)

    if player(board) == X:
        new[action[0]][action[1]] = X
    else:
        new[action[0]][action[1]] = O

    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win = None

    # Check horizontal winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != None:
                win = board[i][0]
                break
    
    # Check vertical winner
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != None:
                win = board[0][i]
                break

    # Check diagonal winner
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != None:
            win = board[0][0]            

    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] != None:
            win = board[2][0]            

    return win


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
   
    if actions(board) == None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            if min_value(result(board, action)) > v:
                v = min_value(result(board, action))
                act = action
        return act
    if player(board) == O:
        v = math.inf
        for action in actions(board):
            if max_value(result(board, action)) < v:
                v = max_value(result(board, action))
                act = action
        return act


def max_value(board):
    """
    Function Max-Value(state)
    """
    v = -math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    Function Min-Value(state)
    """
    v = math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
