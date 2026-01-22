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

import os, time

from constants import *

def display_board(board, game_state):
    # print('clearing screen in 3 seconds')
    # time.sleep(3)
    os.system('clear')
    player = ('Player 1' 
              if game_state in [GameState.PLAYER1_WIN, GameState.PLAYER1_TURN]
              else 'Player 2')
    # check if game has been won
    if game_state is GameState.DRAW:
        print('Game finishes in a draw!')
    elif game_state in GameState.GAME_OVER:
        print(f'{player} has won the game!')
    else:
        print(f'Current Turn: {player}')
        print('Select column for your move')
        # display the column selection arrow here
        selected = board[0][0]
        for col in range(1, NUM_COLS + 1):
            end = '' if col < NUM_COLS else '\n'
            if col == selected:
                print(' v ', end=end)
            else:
                print('   ', end=end)
    for row in range(NUM_ROWS - 1, -1, -1):
        for col in range(1, NUM_COLS + 1):
            end = '' if col < NUM_COLS else '\n'
            print(f'[{PIECE_DISPLAY[board[col][row]]}]', end=end)
    print()
    print(board[0])


def prompt_play_again():
    pass

def clear_screen():
    pass