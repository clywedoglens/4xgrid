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

def in_bounds(i, j):
        return (ZERO < i <= NUM_COLS) and (ZERO <= j < NUM_ROWS)
    
def straight_down(i, j, board, piece):
    cons = 0
    while in_bounds(i, j) and board[i][j] == piece:
        cons += 1
        j -= 1
    return cons == GOAL

def horizontal(i, j, board, piece):
    cons1 = 0
    cons2 = 0
    for n in range(1, -GOAL, -1):
        if not in_bounds(i - n, j) or board[i - n][j] != piece:
            break
        cons1 += 1
    
    for n in range(1, GOAL):
        if not in_bounds(i + n, j) or board[i + n][j] != piece:
            break
        cons2 += 1
    
    return GOAL <= 1 + cons1 + cons2


def left_diagonal(i, j, board, piece):
    cons1 = 0
    cons2 = 0
    for n in range(1, -GOAL, -1):
        if not in_bounds(i - n, j + n) or board[i - n][j + n] != piece:
            break
        cons1 += 1
    
    for n in range(1, GOAL):
        if not in_bounds(i + n, j - n) or board[i + n][j - n] != piece:
            break
        cons2 += 1
    
    return GOAL <= 1 + cons1 + cons2

def right_diagonal(i, j, board, piece):
    cons1 = 0
    cons2 = 0
    for n in range(1, -GOAL, -1):
        if not in_bounds(i + n, j + n) or board[i + n][j + n] != piece:
            break
        cons1 += 1
    
    for n in range(1, GOAL):
        if not in_bounds(i - n, j - n) or board[i - n][j - n] != piece:
            break
        cons2 += 1
    
    return GOAL <= 1 + cons1 + cons2