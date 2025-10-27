"""
Tic Tac Toe Player
"""

import math

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
    
    #Iterate each row in board and and sum X and O
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    #If no X and 0, then X moves.
    if x_count == 0 and o_count == 0:
        return X
    #If X bigger than O, O moves.
    elif x_count > o_count:
        return O
    #Else X moves.
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    The actions function should return a set of all of the possible actions that can be taken on a given board.
    Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    Possible moves are any cells on the board that do not already have an X or an O in them.
    Any return value is acceptable if a terminal board is provided as input.
    """
    
    possible_actions = set()
    
    #Iterate all board i->row, j->cell and if == EMPTY add to possible actions
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    The result function takes a board and an action as input, and should return a new board state, without modifying the original board.
    If action is not a valid action for the board, your program should raise an exception.
    The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
    Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.
    """
    
    i,j = action
    #Check if move is invalid, cell should be EMPTY
    if board[i][j] != EMPTY:
        raise Exception("Invalid action for the board.")
    
    #Copy board to new board
    new_board = [row[:] for row in board]
    
    #Get current player based on actual board state
    current_player = player(board)
    
    #Set new board state
    new_board[i][j] = current_player
    
    #Return the new board based on makin move i,j
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    
    The winner function should accept a board as input, and return the winner of the board if there is one.
    If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
    One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
    If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.
    """


    for row in board:
        #Check if all cells in row are the same and value is not EMPTY
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            #Return the value, X or O
            return row[0]
    
    for col in range(3):
        #Check if all cells in column are the same and value is not EMPTY
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            #Return the value, X or O
            return board[0][col]
    
    #Check diagonals left to right up to down cells are the same and value is not EMPTY
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        #Return the value, X or O
        return board[0][0]

    #Check diagonals right to left up to down cells are the same and value is not EMPTY
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        #Return the value, X or O
        return board[0][2]

    #If no winner found, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.
    If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
    Otherwise, the function should return False if the game is still in progress.
    """
    
    #Check if there is a winner = game over
    if winner(board) is not None:
        return True
    
    #Check if all cells are filled
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    The utility function should accept a terminal board as input and output the utility of the board.
    If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
    You may assume utility will only be called on a board if terminal(board) is True.
    """
    #Call winner function to check who win
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    The minimax function should take a board as input, and return the optimal move for the player to move on that board.
    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    If the board is a terminal board, the minimax function should return None.
    """
    
    #If board is terminal, return None
    if terminal(board):
        return None
    
    #Get current player
    current_player = player(board)
    
    #If X = maximize value (X=1), else minimize value (O= -1)
    if current_player == X:
        _,action = max_value(board)
    else:
        _,action = min_value(board)
    return action

def max_value(board):
    """
    Determine the maximum value action for the current board state.
    """
    
    #If terminal board, return utility value, None for action
    if terminal(board):
        return utility(board), None
    #Set initial v to -infinity and optimal action to None
    v = -math.inf
    optimal_action = None
    
    #Iterate all possible actions
    for action in actions(board):
        #Get min_value of the function min_value(result(board, action))
        min_val, _ = min_value(result(board,action))
        #If min_value > v: Set v to new min_val and optimal_action to actual action
        if min_val > v:
            v = min_val
            optimal_action = action
            
    #Return v and optimal action
    return v, optimal_action


def min_value(board):
    """
    Determine the minimum value action for the current board state.
    """
    
    #If terminal board, return utility value, None for action
    if terminal(board):
        return utility(board), None
    
    #Set initial v to +infinity and optimal action to None
    v = math.inf
    optimal_action = None
    
    #Iterate all possible actions
    for action in actions(board):
        #Get max_value of the function max_value(result(board, action))
        max_val, _ = max_value(result(board,action))
        #If max_value < v: Set v to new max_val and optimal_action to actual action
        if max_val < v:
            v = max_val
            optimal_action = action

    #Return v and optimal action
    return v, optimal_action
            
