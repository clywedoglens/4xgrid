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
from select import select



def save_terminal_settings():
    import sys, termios, atexit
    # Save normal terminal settings
    fd = sys.stdin.fileno()
    old_term = termios.tcgetattr(fd)

    def set_normal_term():
        termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

    # Debuffer new terminal until exit
    new_term = termios.tcgetattr(fd)
    new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

    def set_curses_term():
        termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

    atexit.register(set_normal_term)
    set_curses_term()
    
def get_input():
    if SYSTEM == 'Windows':
        from msvcrt import kbhit, getch
    else:
        import sys
        def kbhit():
            dr,_,_ = select([sys.stdin], [], [], 0)
            return dr != []
        
        def getch():
            print('getch')
            return sys.stdin.buffer.read(1)
        kb_input = ''
    while kb_input == '':
        if kbhit():
            ch = getch()
            print(f'ch: {ch}')
            if b'1' <= ch <= b'7':
                kb_input = int(ch)
            elif ch == ENTER:
                kb_input = ENTER
            elif ch == ESC:
                getch()
                ch = getch()
                if ord(ch) in [LEFT_KEY, RIGHT_KEY]:
                    kb_input = ord(ch)
            else:
                kb_input = chr(ord(ch))
    
    return kb_input


def play_again():
    ans = ''
    while ans not in [YES, NO]:
        ans = get_input()
    return ans