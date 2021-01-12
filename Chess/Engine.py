"""
Engine class is responsible for storing information about current state of the chess game, determining validity of
moves and a move log
"""


class GameState:
    def __init__(self):
        # board is an 8x8 2d list, with each element containing two characters
        # First character represents color of piece, 'b' or 'w'
        # Second character represents the type of piece, 'K', 'Q','R','B','N', and 'P'
        # "--" represents an empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.whiteToMove = True
        self.moveLog = []
