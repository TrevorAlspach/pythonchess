# Main Driver File . Responsible for handling user input + displaying game

import pygame as pg
from Chess import Engine

WIDTH = HEIGHT = 720
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 20
IMAGES = {}

'''
Initialize a global dictionary of piece images
'''


def load_images():
    pieces = ["wR", "wN", "wB", "wQ", "wK", "wP", "bR", "bN", "bB", "bQ", "bK", "bP"]
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("Chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
Main Driver for Chess Game
'''


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    game_state = Engine.GameState()
    load_images()
    running = True

    while running:
        draw_game_state(screen,game_state)
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        clock.tick(MAX_FPS)
        pg.display.flip()


# Draws all graphics for a game_state
def draw_game_state(screen, game_state):
    draw_board(screen)
    draw_pieces(screen, game_state.board)


# Draws the squares on the board
def draw_board(screen):
    colors = [pg.Color( 232, 235, 239), pg.Color(125, 135, 150)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            pg.draw.rect(screen, color, pg.Rect(c*SQ_SIZE, r*SQ_SIZE,SQ_SIZE, SQ_SIZE))


# Draws the pieces on the board
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece],pg.Rect(c*SQ_SIZE, r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


if __name__ == "__main__":
    main()
