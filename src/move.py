import pygame
from const import *


class Move:
    def __init__(self, color, row, col):
        self.moves = []
        self.moved = False
        self.row = row
        self.col = col
        self.color = color
        
    @staticmethod
    def inRange(position: tuple):
        for arg in position:
            if arg < 0 or arg > 7:
                return False
        return True
    
    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col
    
class Path:
    def __init__(self):
        self.pos_empty = []
        self.pos_rival = []
    
    def resetPath(self):
        self.pos_empty = []
        self.pos_rival = []
    
class KnightMove(Move, Path):
    def __init__(self, color, row, col):
        Move.__init__(self, color, row, col)
        Path.__init__(self)
    
    def moveInitPath(self, board):
        knight_moves = [
            (self.row+2, self.col+1),
            (self.row+2, self.col-1),
            (self.row-2, self.col+1),
            (self.row-2, self.col-1),
            (self.row+1, self.col+2),
            (self.row+1, self.col-2),
            (self.row-1, self.col+2),
            (self.row-1, self.col-2),
        ]
        for move in knight_moves:
            if Move.inRange(move): 
                if board.squares[move[0]][move[1]] == None:
                    self.pos_empty.append(move)
                elif board.squares[move[0]][move[1]].color != self.color:
                    self.pos_rival.append(move)

class PawnMove(Move, Path):
    def __init__(self, color, row, col):
        Move.__init__(self, color, row, col)
        Path.__init__(self)
        self.dir = -1 if color == 'white' else 1
        self.first_turn = True
        
    def moveInitPath(self, board):
        if board.squares[self.row+self.dir][self.col] == None:
            self.pos_empty.append((self.row+self.dir, self.col))
            if self.first_turn and board.squares[self.row+self.dir][self.col] == None:
                self.pos_empty.append((self.row+2*self.dir, self.col))
        
        pawn_cross = [
            (self.row+self.dir, self.col+self.dir),
            (self.row+self.dir, self.col-self.dir),
        ]
        for move in pawn_cross:
            if Move.inRange((move[0], move[1])):
                if board.squares[move[0]][move[1]] != None and board.squares[move[0]][move[1]].color != self.color:
                    self.pos_rival.append(move)
                 
class RookMove(Move, Path):
    def __init__(self, color, row, col):
        Move.__init__(self, color, row, col)
        Path.__init__(self)
        
    def moveInitPath(self, board):
        self.__moveHorizontal(board, 1)
        self.__moveHorizontal(board, -1)
        self.__moveVertical(board, 1)
        self.__moveVertical(board, -1)

    def __moveVertical(self, board, dir):
        i = 1
        while Move.inRange((self.row+i*dir, self.col)) and board.squares[self.row+i*dir][self.col] == None:
            if not Move.inRange((self.row+i*dir, self.col)):
                break
            self.pos_empty.append((self.row+i*dir, self.col))
            i += 1
        if Move.inRange((self.row+i*dir, self.col)) and board.squares[self.row+i*dir][self.col].color != self.color:
            self.pos_rival.append((self.row+i*dir, self.col))
    
    def __moveHorizontal(self, board, dir):
        i = 1
        while Move.inRange((self.row, self.col+i*dir)) and board.squares[self.row][self.col+i*dir] == None:
            if not Move.inRange((self.row, self.col+i*dir)):
                break
            self.pos_empty.append((self.row, self.col+i*dir))
            i += 1
        if Move.inRange((self.row, self.col+i*dir)) and board.squares[self.row][self.col+i*dir].color != self.color:
            self.pos_rival.append((self.row, self.col+i*dir))

class BishopMove(Move, Path):
    def __init__(self, color, row, col):
        Move.__init__(self, color, row, col)
        Path.__init__(self)
        
    def moveInitPath(self, board):
        self.__moveCrossLeft(board, 1)
        self.__moveCrossLeft(board, -1)
        self.__moveCrossRight(board, 1)
        self.__moveCrossRight(board, -1)
    
    def __moveCrossLeft(self, board, dir):
        i = 1
        while Move.inRange((self.row+i*dir, self.col-i*dir)) and board.squares[self.row+i*dir][self.col-i*dir] == None:
            if not Move.inRange((self.row+i*dir, self.col-i*dir)):
                break
            self.pos_empty.append((self.row+i*dir, self.col-i*dir))
            i += 1
        if Move.inRange((self.row+i*dir, self.col-i*dir)) and board.squares[self.row+i*dir][self.col-i*dir].color != self.color:
            self.pos_rival.append((self.row+i*dir, self.col-i*dir))
            
    def __moveCrossRight(self, board, dir):
        i = 1
        while Move.inRange((self.row+i*dir, self.col+i*dir)) and board.squares[self.row+i*dir][self.col+i*dir] == None:
            if not Move.inRange((self.row+i*dir, self.col+i*dir)):
                break
            self.pos_empty.append((self.row+i*dir, self.col+i*dir))
            i += 1
        if Move.inRange((self.row+i*dir, self.col+i*dir)) and board.squares[self.row+i*dir][self.col+i*dir].color != self.color:
            self.pos_rival.append((self.row+i*dir, self.col+i*dir))
    
class QueenMove(BishopMove, RookMove):
    def __init__(self, color, row, col):
        RookMove.__init__(self, color, row, col)
        BishopMove.__init__(self, color, row, col)
        
    def moveInitPath(self, board):
        RookMove.moveInitPath(self, board)
        BishopMove.moveInitPath(self, board)
        
class KingMove(Move, Path):
    def __init__(self, color, row, col):
        Move.__init__(self, color, row, col)
        Path.__init__(self)
        
    def moveInitPath(self, board):
        king_moves = [
            (self.row+1, self.col+1),
            (self.row+1, self.col-1),
            (self.row+1, self.col+0),
            (self.row-1, self.col-1),
            (self.row-1, self.col+1),
            (self.row-1, self.col+0),
            (self.row+0, self.col+1),
            (self.row+0, self.col-1),
        ]
        for move in king_moves:
            if Move.inRange(move): 
                if board.squares[move[0]][move[1]] == None:
                    self.pos_empty.append(move)
                elif board.squares[move[0]][move[1]].color != self.color:
                    self.pos_rival.append(move)