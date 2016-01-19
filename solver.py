# The MIT License (MIT)
#
# Copyright (c) 2016 Robert Cochran
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys

def solve(board):
    """Determines who (if anyone) has won the game

    Expects a 2 dimensional array 'board', where coordinates (0, 0) represent
    the top left of the board, containing the string "r" where a red token is,
    "b" where a black token is, and "." for an open space

    Returns "red" if red player wins
    Returns "black" if black player wins
    Returns "tie" if no one has won and there is no space left
    Returns "none" if no one has won and there still space left
    """

    board_width = len(board)
    board_height = len(board[0])

    # Let's talk about the board solving algorithm. It starts from the bottom
    # right most cell, and works its way rightward, going up a line when it
    # reaches the end. We only check for the northwest, north, northeast, and
    # east directions because going from left to right, bottom to top, all
    # cases are covered that way.

    for i in range(board_width):
        for j in reversed(range(board_height)):
            for dir in ("nw", "n", "ne", "e"):
                if board[i][j] in ('r', 'b'):
                    result = __check_line__(board, i, j, board[i][j], dir, 1);
                    if result in ('r', 'b'):
                        # Convert letter to word, then return
                        return {'r':"red", 'b':"black"}[result];

    # Appears we didn't find a match...

    # So, lets check if the board is all filled up...
    for col in board[0]:
        if col[0] == ".": return "none"

    # Appears so
    return "tie"

def __check_line__(board, x, y, color, direction, depth):
    """Check for a line of tokens

    board - the playing board
    x - the X coordinate to check
    y - the Y coordinate to check
    color - what piece color to check for
    direction - what direction to search
    depth - how many pieces we've seen

    Returns "red" for red winner
    Returns "black" for black winner
    Returns "none' for no winner

    Not meant to be called externally
    """
    board_width = len(board)
    board_height = len(board[0])

    # Don't bother with empty spaces
    if color == '.': return "none"

    # Check if we have found a valid string (board[x][y] == color, depth == 4)
    if depth == 4:
        if board[x][y] == color:
            # Excellent, we have a winner
            return color
        else:
            # Drat. Return "none" since we are at the depth limit
            return "none"

    # Check if we have a match and should continue
    if board[x][y] != color: return "none"

    # Check if we're on the side edges of the board. If we are, return "none"
    # since we haven't reached depth limit and there's no more board to traverse
    # in the correct direction (split into two ifs for readability)
    if direction == "nw" and x == 0: return "none"
    if direction in ("ne", "e") and x == board_width - 1: return "none"

    # Ditto for the top of the board
    if direction in ("nw", "n", "ne") and y == 0: return "none"

    # Alright. Since we've now eliminated all possible dead ends,
    # there must be more to explore on the board
    if direction == "nw":
        return __check_line__(board, x - 1, y - 1, color, "nw", depth + 1)
    elif direction == "n":
        return __check_line__(board, x, y - 1, color, "n", depth + 1)
    elif direction == "ne":
        return __check_line__(board, x + 1, y - 1, color, "ne", depth + 1)
    elif direction == "e":
        return __check_line__(board, x + 1, y, color, "e", depth + 1)

    # At this point, we've effectively mapped out all possible avenues of
    # meaningful continuation, should we make it this far... well...
    print("__check_line__(): Impossible situation!")
    print("board = {}".format(board))
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("color = {}".format(color))
    print("direction = {}".format(direction))
    print("depth = {}".format(depth))
    sys.exit(-1);
