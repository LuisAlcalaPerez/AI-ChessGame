'''
- Storing all the information about the current state of the chess game
- Determine valid moves at the current state of the chess game
- Move log
'''


class GameState():

    def __init__(self):
        # The board is 8x8 2d list
        # Each element of the list has 2 character
        # -- : empty cell (no piece on it)
        # For the pieces: 
        #       - first character is the color of the piece. 'b' or 'w'
        #       - second character the type of the piece: 'R', 'N', 'B', 'Q', 'K', 'P'
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]

        self.whiteToMove = True
        self.moveLog = []

        