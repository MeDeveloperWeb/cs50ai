"""
Tic Tac Toe Player
"""

import math
import copy
import time
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
    x_count = 0
    o_count = 0

    for row in board:
        for column in row:
            if column is X:
                x_count += 1
            elif column is O:
                o_count += 1

    if x_count is not o_count:
        return O

    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                action.add((i,j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    board = copy.deepcopy(board)

    if board[i][j] is not EMPTY:
        raise Exception("Illegal Move")

    board[i][j] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    d2win = [0, board[1][1]]
    d1win = [0, board[1][1]]
    for i in range(3):
        hwin = [0, board[i][0]]
        vwin = [0, board[0][i]]
        for j in range(3):
            if board[i][j] is hwin[1]:
                hwin[0] += 1
            if board[j][i] is vwin[1]:
                vwin[0] += 1
            if i is j and board[i][j] is d1win[1]:
                d1win[0] += 1
            if i is 2 - j and board[i][j] is d2win[1]:
                d2win[0] += 1
        for win in [hwin, vwin, d1win, d2win]:
            if win[0] == 3:
                return win[1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        for column in row:
            if column is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    victor = winner(board)
    if victor is O:
        return -1
    elif victor is X:
        return 1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # choice = actions(board)
    # return random.choice(list(choice))
    opt_action = (0,0)
    if player(board) is O:
        score = math.inf
        for action in actions(board):
            new_score = maxScore(result(board, action), -math.inf, math.inf)
            if score > new_score:
                score = new_score
                opt_action = action
    else:
        score = -math.inf
        actions_set = actions(board)
        if (len(actions_set) == 9):
            return (0,2)
        for action in actions_set:
            new_score = minScore(result(board, action), -math.inf, math.inf)
            if score < new_score:
                score = new_score
                opt_action = action
    return opt_action

def minScore(board, alpha, beta):
    if terminal(board):
        return utility(board)

    score = math.inf
    
    for action in actions(board):
        score = min(score, maxScore(result(board, action), alpha, beta))
        beta = min( beta, score)
        if beta <= alpha:
            break
    return score 

def maxScore(board, alpha, beta):
    if terminal(board):
        return utility(board)

    score = -math.inf
    
    for action in actions(board):
        score = max(score, minScore(result(board, action), alpha, beta))
        alpha = max(alpha, score)
        if beta <= alpha:
            break
    return score 