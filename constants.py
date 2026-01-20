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

import platform
from enum import Flag, auto

WINDOWS = "Windows"
LINUX = "Linux"

SYSTEM = platform.system()


class GameState(Flag):
    START = auto()
    PLAYER1_TURN = auto()
    PLAYER2_TURN = auto()
    IN_GAME = PLAYER1_TURN | PLAYER2_TURN
    PLAYER1_WIN = auto()
    PLAYER2_WIN = auto()
    DRAW = auto()
    GAME_OVER = PLAYER1_WIN | PLAYER2_WIN | DRAW
    END = auto()


NUM_COLS = 7
NUM_ROWS = 6
EMPTY = 0
STARTING_INDEX = 0
PLAYER1_PIECE = 1
PLAYER2_PIECE = 2
PIECE_DISPLAY = (' ', '@', '#')

# input keys
ESC = b'\x1b'
LEFT_KEY = 68
RIGHT_KEY = 67
ENTER = b'\n'
YES = 'y'
NO = 'n'

ZERO = 0
ONE = 1
SEVEN = 7
GOAL = 4

CPU_WEIGHTS = [0.1, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1]