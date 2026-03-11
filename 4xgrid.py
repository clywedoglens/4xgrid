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
from display import display_board, prompt_cpu, prompt_play_again
from win_conditions import *
import random
import time

def run_game(board, game_state, display=None, cpu=True):
    game_state = (GameState.PLAYER1_TURN if random.random() > 0.5 
                  else GameState.PLAYER2_TURN)
    player2_move = cpu_move if cpu else player_move
    while game_state in GameState.IN_GAME:
        turn_vars = {GameState.PLAYER1_TURN: (player_move, PLAYER1_PIECE),
                     GameState.PLAYER2_TURN: (player2_move, PLAYER2_PIECE)}
        move, piece = turn_vars[game_state]
        last_move = board[0][0]
        current = next_valid_col(ONE, board, increment_col)
        board[0][0] = current
        if display:
            display(board, game_state)
        board, game_state = move(board, game_state, display)
        # column has been selected
        # update the board
        col = board[0][0]
        row = board[0][col]
        board[col][row] = piece
        game_state = game_over(board, game_state)
    return board, game_state


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


def cpu_move(board, game_state, display):
    valid_cols = [col for col in range(1, NUM_COLS + 1) 
                  if valid_column(col, board)]
    
    if not valid_cols:
        return board, game_state

    for col in CENTER_COLS:
        if col in valid_cols:
            chosen = col
            break
    else:
        chosen = random.choice(valid_cols)
    
    board[0][0] = chosen
    
    if display:
        display(board, game_state)
    return board, game_state


def player_move(board, game_state, display):
    pending_move = True
    while pending_move:
        ch = get_input()
        if ch == ENTER:
            # hit enter
            pending_move = False
        elif ord(ch) in [LEFT_KEY, RIGHT_KEY]:
            # move selection to next valid column
            current = board[0][0]
            if ord(ch) == RIGHT_KEY:
                shift = increment_col
            else:
                shift = decrement_col
            current = shift(current)
            current = next_valid_col(current, board, shift)
            board[0][0] = current
            if display:
                display(board, game_state)
        elif valid_column(int(ch), board):
            board[0][0] = int(ch)
            pending_move = False
    return board, game_state


def game_over(board, game_state):
    game_won = False
    move_col = board[0][0]
    move_row = board[0][move_col]

    piece = PLAYER1_PIECE if game_state is GameState.PLAYER1_TURN else PLAYER2_PIECE

    game_won = any([straight_down(move_col, move_row, board, piece),
                   horizontal(move_col, move_row, board, piece),
                   left_diagonal(move_col, move_row, board, piece),
                   right_diagonal(move_col, move_row, board, piece)])
    board[0][move_col] += 1
    if not game_won and all(map((lambda x: x == NUM_ROWS), board[0][1:])):
        game_state = GameState.DRAW
    elif game_state is GameState.PLAYER1_TURN:
        game_state = (GameState.PLAYER1_WIN if game_won
                      else GameState.PLAYER2_TURN)
    else:
        game_state = (GameState.PLAYER2_WIN if game_won
                      else GameState.PLAYER1_TURN)
        
    return game_state

def run_session():
    cpu = prompt_cpu()
    game_state = GameState.START
    stats = {PLAYER1_WINS: 0,
             PLAYER2_WINS: 0,
             DRAWS: 0,
             GAMES_PLAYED: 0}
    def display_with_stats(board, game_state):
        display_board(board, game_state, stats)
    while game_state is GameState.START:
        board = initialize_board()
        board, game_state = run_game(board, game_state, display_with_stats, cpu)
        match game_state:
            case GameState.PLAYER1_WIN:
                stats[PLAYER1_WINS] += 1
            case GameState.PLAYER2_WIN:
                stats[PLAYER2_WINS] += 1
            case GameState.DRAW:
                stats[DRAWS] += 1
        stats[GAMES_PLAYED] += 1
        display_board(board, game_state, stats)
        game_state = prompt_play_again()
    print('Thanks for playing!')


if __name__ == '__main__':
    if SYSTEM == LINUX:
        save_terminal_settings()
    run_session()
    