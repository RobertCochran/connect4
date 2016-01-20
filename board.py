NONE = '.'
RED = 'R'
BLACK = 'B'

BOARD_COLUMNS = 7
BOARD_ROWS = 6


def _new_game_board():
    '''
    Creates a new game board.  Initially, a game board has the size
    BOARD_COLUMNS x BOARD_ROWS and is comprised only of strings with the
    value NONE
    '''
    board = []

    for col in range(BOARD_COLUMNS):
        board.append([])
        for row in range(BOARD_ROWS):
            board[-1].append(NONE)

    return board
