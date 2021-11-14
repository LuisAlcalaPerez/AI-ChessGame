'''
- Main driver file
- Handles user input 
- Displays current state of the game (GameStates object)
'''

import pygame as p
from ChessEngine import *

# Constants
WIDTH = HEIGHT = 512                # size of the board
DIM = 8                       # dimension of the board (8x8)
CELL_SIZE = HEIGHT // DIM     # size of each cell
MAX_FPS = 15                        # refresh rate
IMAGES = {}                         # dictionary to store the images


'''
Initialisation of the global directory for the images
This will only happend once at the start of the main
'''
def load_images():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('assets/' + piece + '.png'), (CELL_SIZE, CELL_SIZE))
    # we can acces the image of a piece by IMAGES['wp'] for example


'''
Draw the current GameState -> responsible for the graphics
    - draw the squares
    - draw the pieces
'''
def drawGameState(display, gs):
    drawBoard(display)                 # drawing squares on the board
    drawPieces(display, gs.board)      # drawing the pieces on top of the squares


'''
Draw the squares on the board
'''
def drawBoard(display):
    background_colors = [p.Color('white'), p.Color('gray')]
    for row in range(DIM):
        for col in range(DIM):
            color = background_colors[(row+col)%2]
            p.draw.rect(display, color, p.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


'''
Draw the pieces on the board
'''
def drawPieces(display, board):
    for row in range(DIM):
        for col in range(DIM):
            piece = board[row][col]

            if piece != '--':  # if there is a piece in that cell
                display.blit(IMAGES[piece], p.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


'''
Main function:
    - hamdles user input
    - update grafics
'''
def main():
    # Initialise pygame
    p.init()

    # Initialise the display and the clock
    display = p.display.set_mode((WIDTH, HEIGHT))
    display.fill(p.Color('white'))
    clock = p.time.Clock()
    
    # Initialise the GameState
    gs = GameState()

    # Load the images (only once before the running loop)
    load_images()
    running = True

    # Initialising cell selected by the last click of the mouse
    cell_selected = ()  # (row, col) 
    player_clicks = []  # keeps track of the player clicks

    # Running Loop
    while running:

        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()     # location of the mouse when clik event happends (x, y)
                col = location[0] // CELL_SIZE
                row = location[1] // CELL_SIZE

                if cell_selected == (row, col):  # check if player has clicked twice in the same cell
                    cell_selected = ()           # deselect the cell
                    player_clicks = []           # clear player clicks
                else:
                    cell_selected = (row, col)
                    player_clicks.append(cell_selected)   # we keep track of the first two clicks

                if len(player_clicks) == 2:      # after the second click
                    move = Move(player_clicks[0], player_clicks[1], gs.board)
                    print(move.get_chess_notation())
                    gs.make_move(move)
                    cell_selected = ()           
                    player_clicks = []

        drawGameState(display, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


if __name__ == '__main__':
    main()