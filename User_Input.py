from random import *


def user_input(board):
    """ This function allows the user to choose where their red piece goes. """
    
    print "Were going to play Connect Four."
    print " I'll be black and you'll  be red. "

    print "You go first and choose where you want to put your piece. There are seven columns in total."


valid_move = False
while not valid_move:
    col = input(" Choose a column to put your piece in (1-7): ")
    for row in range (6,0,-1):
        if (1 <= row <= 6) and (1 <= col <= 7) and (board[row-1][col-1] == " "):
            board[row-1][col-1] = 'r'
            valid_move = True
            break
        else:
            print "Error, please restart game and try again."
            

def computer_choice(board):
    """ this function has the computer randomly choose where it will set its
    piece """


valid_move = False
while not valid_move:
    row = random.randint(0,6)
    col = random.randint(0,7)
    for row in range (6,0,-1):
        if board[row][col] == " ":
            board[row][colum] == "b"
            valid_move = True
            break
