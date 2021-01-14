# Main Driver File . Responsible for handling user input + displaying game

import pygame as pg
from Chess import Engine
import pdb

WIDTH = HEIGHT = 512
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
    sq_selected = ()  # keep track of the user's last click (row,column)
    player_clicks = []  # Keep track of # of user clicks (two tuples: [(6,4),(4,4)])

    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

                if sq_selected == (row, col):  # user selected the same square twice
                    sq_selected = ()
                    player_clicks = []
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected)

                if len(player_clicks) == 2:
                    move = Engine.Move(player_clicks[0], player_clicks[1], game_state.board)
                    if game_state.is_valid_move(move):
                        print(move.get_chess_notation())
                        game_state.makeMove(move)
                    sq_selected = ()
                    player_clicks = []




        draw_game_state(screen, game_state)
        clock.tick(MAX_FPS)
        pg.display.flip()


# Draws all graphics for a game_state
def draw_game_state(screen, game_state):
    draw_board(screen)
    draw_pieces(screen, game_state.board)


# Draws the squares on the board
def draw_board(screen):
    colors = [pg.Color(232, 235, 239), pg.Color(125, 135, 150)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pg.draw.rect(screen, color, pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


# Draws the pieces on the board
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c].id
            if piece != '--':
                screen.blit(IMAGES[piece], pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
