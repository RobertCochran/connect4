#!/usr/bin/env python2

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

import solver

boards = []

with open("test-boards.txt") as file:
    board = {"layout":[]}
    for line in file:
        # Comments - skip 'em
        if line[0] == '#':
            continue
        if line.strip('\n') in ("red", "black", "tie", "none"):
            board["expected"] = line.strip('\n')
            continue
        if line == '\n':
            boards.append(board)
            board = {"layout":[]}
        row = []
        for char in line:
            if char == '\n': continue
            row.append(char)
        if line != '\n':
            board["layout"].append(row)

def pretty_print_board(board):
    for row in board:
        for col in row:
            sys.stdout.write(col)
        sys.stdout.write('\n')

for board in boards:
    result = solver.solve(board["layout"])
    if result != board["expected"]:
        print("test_solver: test failed")
        print("Board:")
        pretty_print_board(board["layout"])
        print("Result: {}".format(result))
        print("Expected: {}".format(board["expected"]))
        sys.exit(-1);

print("All solver tests passed")
