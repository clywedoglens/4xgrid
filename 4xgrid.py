"""
4xGrid
Copyright (C) 2026 George Vergara

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from constants import *
from userinput import get_input, save_terminal_settings
from display import display_board
from win_conditions import *
from random import random
import time

def run_game(game_state):
    # method should probably return the result of the game 
    board = initialize_board()
    game_state = (GameState.PLAYER1_TURN if random() > 0.5 
                  else GameState.PLAYER2_TURN)
    while game_state in GameState.IN_GAME:
        turn_vars = {GameState.PLAYER1_TURN: (prompt_player, PLAYER1_PIECE),
                     GameState.PLAYER2_TURN: (player2_move, PLAYER2_PIECE)}
        move, piece = turn_vars[game_state]
        last_move = board[0][0]
        # move arrow to lowest possible value
        current = next_valid_col(ONE, board, increment_col)
        board[0][0] = current
        display_board(board, game_state)
        board, game_state = move(board, game_state)
        # column has been selected
        # update the board
        col = board[0][0]
        row = board[0][col]
        board[col][row] = piece
        game_state = game_over(board, game_state)
        if game_state not in GameState.GAME_OVER:
            # update the row value for the column
            board[0][col] += 1
    display_board(board, game_state)
    time.sleep(5)


def initialize_board():
    board = []
    sentinel = [ONE]
    sentinel.extend([STARTING_INDEX] * (NUM_COLS))
    board.append(sentinel)
    for _ in range(NUM_COLS):
        board.append([EMPTY] * NUM_ROWS)
    return board


def next_valid_col(col, board, op):
    while not valid_column(col, board):
        col = op(col)
    return col


def valid_column(col, board):
        return col <= NUM_COLS and board[0][col] < NUM_ROWS


def increment_col(col):
    return col + 1 if col < SEVEN else ONE


def decrement_col(col):
    return col - 1 if col > ONE else SEVEN


def player2_move(board, game_state):
    # default CPU turn
    # update board
    # check if game is over
    # game_state = game_over(board, GameState.PLAYER2_TURN)
    # return board data and corresponding game state
    return board, game_state


def prompt_player(board, game_state):
    pending_move = True
    while pending_move:
        ch = get_input()
        print(f'ch: {ch}')
        if ch == ENTER:
            # hit enter
            pending_move = False
        elif valid_column(ch, board):
            board[0][0] = ch
            pending_move = False
        elif ch in [LEFT_KEY, RIGHT_KEY]:
            # move selection to next valid column
            current = board[0][0]
            if ch == RIGHT_KEY:
                shift = increment_col
            else:
                shift = decrement_col
            current = shift(current)
            current = next_valid_col(current, board, shift)
            board[0][0] = current
            print("shifting arrow")
            display_board(board, game_state)
        elif ch == ENTER:
            pending_move = False
    return board, game_state


def game_over(board, game_state):
    game_won = False
    move_col = board[0][0]
    move_row = board[0][move_col]

    # return immediately in case of draw
    if all(map((lambda x: x == SEVEN), board[0][1:])):
        return GameState.DRAW

    piece = PLAYER1_PIECE if game_state is GameState.PLAYER1_TURN else PLAYER2_PIECE
    # helper functions for win conditions

    # check if last_move results in win
    game_won = any([straight_down(move_col, move_row, board, piece),
                   horizontal(move_col, move_row, board, piece),
                   left_diagonal(move_col, move_row, board, piece),
                   right_diagonal(move_col, move_row, board, piece)])
    if game_state is GameState.PLAYER1_TURN:
        game_state = (GameState.PLAYER1_WIN if game_won
                      else GameState.PLAYER2_TURN)
    else:
        game_state = (GameState.PLAYER2_WIN if game_won
                      else GameState.PLAYER1_TURN)
    # function should also check if game ends in draw
        
    return game_state


if __name__ == '__main__':
    if SYSTEM == LINUX:
        save_terminal_settings()

    game_state = GameState.START
    while game_state is GameState.START:
        run_game(game_state)
        # ask player to play again
        game_state = prompt_play_again()