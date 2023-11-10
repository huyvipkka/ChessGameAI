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

    def move(self):
        pass
    
class Path:
    def __init__(self):
        self.pos_empty = []
        self.pos_rival = []
        self.pos_friend = []
    
    def resetPath(self):
        self.pos_empty = []
        self.pos_rival = []
        self.pos_friend = []
    
class KinghtMove(Move, Path):
    def __init__(self, color, row, col):
        Move.__init__(self, color, row, col)
        Path.__init__(self)
    
    def moveInit(self, board):
        self.resetPath()
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
                elif board.squares[move[0]][move[1]].color == self.color:
                    self.pos_friend.append(move)

        