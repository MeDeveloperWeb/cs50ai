"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    raise NotImplementedError


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
    return None

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    choice = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY:
                choice.append((i,j))
    return random.choice(choice)
