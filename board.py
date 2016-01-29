empty = '.'
red = 'r'
black = 'b'

BOARD_COLUMNS = 7
BOARD_ROWS = 6


def start_new_board_game()
    '''
    Creates a new game board.  Initially, a game board has the size
    BOARD_COLUMNS x BOARD_ROWS and is comprised only of strings with the
    value empty
    '''
    board = []

    for col in range(BOARD_COLUMNS):
        board.append([])
        for row in range(BOARD_ROWS):
            board[-1].append(empty)

    return board
