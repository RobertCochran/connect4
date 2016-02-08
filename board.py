empty = '.'
red = 'r'
black = 'b'

colums = 7
rows = 6


def start_new_board_game()
    '''
    Creates a new game board.  Initially, a game board has the size
    BOARD_COLUMNS x BOARD_ROWS and is comprised only of strings with the
    value empty
    '''
    board = []

    for col in range(columns):
        board.append([])
        for row in range(rows):
            board[-1].append(empty)

    return board

def drop_token(board, column, color, x, y):
    '''
    This drops a point in a specific spot that the user inputs.
    '''
    drop_point = in board.drop.color(column.(x,y))

    
def move_is_valid(board, column):
    '''
    This will check the board for empty spaces.
    '''
    if board.columns.(7, 6) == True:
        if board.columns.(6, 6) == True:
            if board.columns.(5, 6) == True:
                if board.columns.(4, 6) == True:
                    if board.columns.(3, 6) == True:
                        if board.columns.(2, 6) == True:
                            if board.columns.(1, 6) == True:
    return True                            
    if board.columns.(7, 6) == False:
         if board.columns.(6, 6) == False:
              if board.columns.(5, 6) == False:
                  if board.columns.(4, 6) == False:
                       if board.columns.(3, 6) == False:
                            if board.columns.(2, 6) == False:
                                 if (oard.columns.(1, 6) == False:     
    return False                            


def main():
    board = start_new_board_game()
    if move_is_valid(board, colums) == True:
        drop_token(board, colums, color, x, y)
    else:
        # I don't know what to write here can you help please.?
