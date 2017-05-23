#!/bin/python
from __future__ import print_function, unicode_literals
import sys
#from __future__ import print_function, unicode_literals
class Piece(object):

    def __init__(self, color, ptype, row, col):
        self.color = color
        self.ptype = ptype
        self.row = row
        self.col = col
        self.captured = False

    def valid_moves(self, board):
        pass

    def can_move_to(self, r, c):
        if r == self.row and c == self.col:
            return False

        if r < 0 or r > 3:
            return False
        if c < 0 or c > 3:
            return False

        if board.mat[r][c] is None:
            return True
        elif board.mat[r][c].color != self.color:
            return True

        return False

    def can_move_to_s(self, r, c):
        if r == self.row and c == self.col:
            return False

        if r < 0 or r > 3:
            return False
        if c < 0 or c > 3:
            return False
        #print board.mat[r][c].color, self.color
        # Straight pawn
        if board.mat[r][c] is None:
            return True

        return False

    def can_move_to_d(self, r, c):
        if r == self.row and c == self.col:
            return False

        if r < 0 or r > 3:
            return False
        if c < 0 or c > 3:
            return False

        #print board.mat[r][c].color, self.color
        if board.mat[r][c] is not None:
            if board.mat[r][c].color != self.color:
                return True

        return False
    
    def _straight_moves1(self, board):
        possible = []
        if self.color == 'B':
            # straight up
            for row in range(1, 2):
                r, c = self.row - row, self.col
                if self.can_move_to_s(r, c):
                    possible.append((r, c))
                if not board.is_open(r, c):
                    break
        else:
            # straight down
            for row in range(1, 2):
                r, c = self.row + row, self.col
                if self.can_move_to_s(r, c):
                    possible.append((r, c))
                if not board.is_open(r, c):
                    break
        return possible
            
    def _diagonal_moves1(self, board):
        possible = []
        if self.color == 'B':
        # straight left up
            for rc in range(1, 2):
                r, c = self.row - rc, self.col - rc
                if self.can_move_to_d(r, c):
                    possible.append((r, c))
                if not board.is_open(r, c):
                    break
            # straight right up
            for rc in range(1, 2):
                r, c = self.row - rc, self.col + rc
                if self.can_move_to_d(r, c):
                    possible.append((r, c))
                if not board.is_open(r, c):
                    break
            
        else:
            # straight left down
            for rc in range(1, 2):
                r, c = self.row + rc, self.col - rc
                if self.can_move_to_d(r, c):
                    possible.append((r, c))
                if not board.is_open(r, c):
                    break

            # straight right down
            for rc in range(1, 2):
                r, c = self.row + rc, self.col + rc
                if self.can_move_to_d(r, c):
                    possible.append((r, c))
                if not board.is_open(r, c):
                    break

        return possible  
    
    def _straight_moves(self, board):
        possible = []
        # straight up
        for row in range(1, 4):
            r, c = self.row - row, self.col
            if self.can_move_to(r, c):
                possible.append((r, c))
            if not board.is_open(r, c):
                break

        # straight down
        for row in range(1, 4):
            r, c = self.row + row, self.col
            if self.can_move_to(r, c):
                possible.append((r, c))
            if not board.is_open(r, c):
                break

        # straight left
        for col in range(1, 4):
            r, c = self.row, self.col - col
            if self.can_move_to(r, c):
                possible.append((r, c))
            if not board.is_open(r, c):
                break

        # straight right
        for col in range(1, 4):
            r, c = self.row, self.col + col
            if self.can_move_to(r, c):
                possible.append((r, c))
            if not board.is_open(r, c):
                break

        return possible

    def _diagonal_moves(self, board):
        possible = []
        # straight left up
        for rc in range(1, 4):
            r, c = self.row - rc, self.col - rc
            if self.can_move_to(r, c):
                possible.append((r, c))
            if not board.is_open(r, c):
                break

        # straight left down
        for rc in range(1, 4):
            r, c = self.row + rc, self.col - rc
            if self.can_move_to(r, c):
                possible.append((r, c))
            if not board.is_open(r, c):
                break

        # straight right up
        for rc in range(1, 4):
            r, c = self.row - rc, self.col + rc
            if self.can_move_to(r, c):
                possible.append((r, c))
            if not board.is_open(r, c):
                break

        # straight right down
        for rc in range(1, 4):
            r, c = self.row + rc, self.col + rc
            if self.can_move_to(r, c):
                possible.append((r, c))
            if not board.is_open(r, c):
                break

        return possible

class Pawn(Piece):
    
    def valid_moves(self, board):
        possible = self._straight_moves1(board) + self._diagonal_moves1(board)
        return possible

class Rook(Piece):

    def valid_moves(self, board):
        possible = self._straight_moves(board)
        return possible


class Queen(Piece):

    def valid_moves(self, board):
        possible = self._straight_moves(board) + self._diagonal_moves(board)
        return possible


class Knight(Piece):

    def valid_moves(self, board):
        r, c = self.row, self.col
        possible = [
            (r - 2, c - 1), (r - 2, c + 1),
            (r - 1, c + 2), (r - 1, c - 2),
            (r + 1, c + 2), (r + 1, c - 2),
            (r + 2, c - 1), (r + 2, c + 1),
        ]
        return [(r, c) for r, c in possible if self.can_move_to(r, c)]


class Bishop(Piece):

    def valid_moves(self, board):
        possible = self._diagonal_moves(board)
        return possible


class Board(object):

    def __init__(self):
        self.mat = [[None for i in range(4)] for u in range(4)]
        self.white = []
        self.black = []

    def add_piece(self, color, ptype, row, col):
        if ptype == "Q":
            piece = Queen(color, ptype, row, col)
        elif ptype == "N":
            piece = Knight(color, ptype, row, col)
        elif ptype == "B":
            piece = Bishop(color, ptype, row, col)
        elif ptype == "R":
            piece = Rook(color, ptype, row, col)
        elif ptype == "P":
            piece = Pawn(color, ptype, row, col)
        else:
            raise Exception("Invalid type")

        self.mat[row][col] = piece
        if color == "W":
            self.white.append(piece)
        elif color == "B":
            self.black.append(piece)

    def move_to(self, piece, row, col):
        self.mat[piece.row][piece.col] = None
        if self.mat[row][col] is not None:
            captured = self.mat[row][col]
            captured.captured = True
        self.mat[row][col] = piece
        piece.row = row
        piece.col = col

    def undo_move(self, captured, piece, prev_r, prev_c):
        self.move_to(piece, prev_r, prev_c)
        if captured:
            cr, cc = captured.row, captured.col
            self.mat[cr][cc] = captured
            captured.captured = False

    def is_open(self, r, c):
        if r < 0 or r > 3:
            return False
        if c < 0 or c > 3:
            return False
        if self.mat[r][c] is None:
            return True
        return False

    def white_can_win(self, turns_left):
        if turns_left <= 0:
            return False

        white_pieces = self.white

        q = []
        for piece in white_pieces:
            if piece.captured is True:
                continue

            valid_moves = piece.valid_moves(self)
            for r, c in valid_moves:
                captured = self.mat[r][c]
                if captured is not None and captured.ptype == "Q":
                    return True

                q.insert(0, (piece, r, c))

        for piece, r, c in q:
            prev_r, prev_c = piece.row, piece.col
            captured = self.mat[r][c]
            self.move_to(piece, r, c)

            # if for all follow-up opponent moves, we can find a winning move within the limit, return True
            if self.black_cannot_avoid_loss(turns_left - 1):
                self.undo_move(captured, piece, prev_r, prev_c)
                return True

            self.undo_move(captured, piece, prev_r, prev_c)

        return False

    def black_cannot_avoid_loss(self, turns_left):
        if turns_left <= 0:
            return False

        black_pieces = self.black

        for piece in black_pieces:
            if piece.captured is True:
                continue

            valid_moves = piece.valid_moves(self)
            for r, c in valid_moves:
                prev_r, prev_c = piece.row, piece.col
                captured = self.mat[r][c]

                if captured is not None and captured.ptype == "Q":
                    return False

                self.move_to(piece, r, c)

                if not self.white_can_win(turns_left - 1):
                    self.undo_move(captured, piece, prev_r, prev_c)
                    return False

                self.undo_move(captured, piece, prev_r, prev_c)

        return True

    def __repr__(self):
        s = []

        for i, row in enumerate(self.mat[::-1]):
            s.append("{} ".format(4 - i))
            for col in row:
                if col is None or col.captured is True:
                    s.append(".")
                elif col.color == "W":
                    s.append(col.ptype.upper())
                elif col.color == "B":
                    s.append(col.ptype.lower())
            s.append("\n")
        s.append("  ABCD")
        return "".join(s)

g = int(raw_input().strip())
for a0 in xrange(g):
    board = Board()
    cols = "ABCD"
    w, b, m = map(int, raw_input().split(" "))
    for i in range(w):
        ptype, col, row = raw_input().split(" ")
        col = cols.index(col)
        row = int(row) - 1
        board.add_piece("W", ptype, row, col)
    for i in range(b):
        ptype, col, row = raw_input().split(" ")
        col = cols.index(col)
        row = int(row) - 1
        board.add_piece("B", ptype, row, col)
    # your code goes here
    print("YES" if board.white_can_win(m) else "NO")