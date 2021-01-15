"""
Engine class is responsible for storing information about current state of the chess game, determining validity of
moves and a move log
"""
black_piece_ids = ()
white_piece_ids = ()

class Piece:
    def __init__(self, color, type, can_take=False):
        self.color = color
        self.type = type
        self.can_take = can_take
        self.id = color + type
        self.movecount = 0
        # for determining if a pawn can move 1 or 2 spaces


class GameState:
    def __init__(self):
        self.board = [
            [Piece("b", "R"), Piece("b", "N"), Piece("b", "B"),
             Piece("b", "Q"), Piece("b", "K"), Piece("b", "B"), Piece("b", "N"), Piece("b", "R")],
            [Piece("b", "P"), Piece("b", "P"), Piece("b", "P"),
             Piece("b", "P"), Piece("b", "P"), Piece("b", "P"), Piece("b", "P"), Piece("b", "P")],
            [Piece("-", "-"), Piece("-", "-"), Piece("-", "-"),
             Piece("-", "-"), Piece("-", "-"), Piece("-", "-"), Piece("-", "-"), Piece("-", "-")],
            [Piece("-", "-"), Piece("-", "-"), Piece("-", "-"),
             Piece("-", "-"), Piece("-", "-"), Piece("-", "-"), Piece("-", "-"), Piece("-", "-")],
            [Piece("-", "-"), Piece("-", "-"), Piece("-", "-"),
             Piece("-", "-"), Piece("-", "-"), Piece("-", "-"), Piece("-", "-"), Piece("-", "-")],
            [Piece("-", "-"), Piece("-", "-"), Piece("-", "-"),
             Piece("-", "-"), Piece("-", "-"), Piece("-", "-"), Piece("-", "-"), Piece("-", "-")],
            [Piece("w", "P"), Piece("w", "P"), Piece("w", "P"),
             Piece("w", "P"), Piece("w", "P"), Piece("w", "P"), Piece("w", "P"), Piece("w", "P")],
            [Piece("w", "R"), Piece("w", "N"), Piece("w", "B"),
             Piece("w", "Q"), Piece("w", "K"), Piece("w", "B"), Piece("w", "N"), Piece("w", "R")]]

        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.start_row][move.start_col] = Piece("-", "-")
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.board[move.end_row][move.end_col].movecount += 1
        self.moveLog.append(move)

        self.whiteToMove = not self.whiteToMove

    def is_valid_move(self, move):
        if self.board[move.start_row][move.start_col].id == '--':
            return False
        if self.whiteToMove:
            if self.board[move.start_row][move.start_col].id in ("bP", "bR", "bN", "bB", "bQ", "bK"):
                return False
            if self.board[move.end_row][move.end_col].id in ("wP", "wR", "wN", "wB", "wQ", "wK"):
                return False
        else:
            if self.board[move.start_row][move.start_col].id in ("wP", "wR", "wN", "wB", "wQ", "wK"):
                return False
            if self.board[move.end_row][move.end_col].id in ("bP", "bR", "bN", "bB", "bQ", "bK"):
                return False
        if self.board[move.start_row][move.start_col].id in ("wP", "bP"):
            if [move.end_row, move.end_col] not in get_legal_pawn_moves([move.start_row,move.start_col], self.board, self.whiteToMove):
                return False
        return True


class Move:
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]


def get_legal_pawn_moves(pos, board, white_to_move):
    legal_moves = []
    if white_to_move:
        if board[pos[0] - 1][pos[1]].id == '--':
            legal_moves.append([pos[0] - 1, pos[1]])
        if (board[pos[0] - 2][pos[1]].id == '--') \
                and (board[pos[0] - 1][pos[1]].id == '--') and (board[pos[0]][pos[1]].movecount == 0):
            legal_moves.append([pos[0] - 2, pos[1]])
        if pos[1] in range(0, 6):
            if board[pos[0] - 1][pos[1] + 1].id not in ('--', 'bK'):
                legal_moves.append([pos[0]-1, pos[1]+1])
        if pos[1] in range(1, 7):
            if board[pos[0] - 1][pos[1] - 1].id not in ('--', 'bK'):
                legal_moves.append([pos[0]-1, pos[1]-1])

        print(legal_moves)
        return legal_moves
    else:
        if board[pos[0] + 1][pos[1]].id == '--':
            legal_moves.append([pos[0] + 1, pos[1]])
        if (board[pos[0] + 2][pos[1]].id == '--') \
                and (board[pos[0] + 1][pos[1]].id == '--') and (board[pos[0]][pos[1]].movecount == 0):
            legal_moves.append([pos[0] + 2, pos[1]])
        if pos[1] in range(0, 6):
            if board[pos[0] + 1][pos[1] + 1].id not in ('--', 'bK'):
                legal_moves.append([pos[0]+1, pos[1]+1])
        if pos[1] in range(1, 7):
            if board[pos[0] + 1][pos[1] - 1].id not in ('--', 'bK'):
                legal_moves.append([pos[0]+1, pos[1]-1])
        print(legal_moves)
        return legal_moves


