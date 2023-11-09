import pygame
from piece import Piece

class Square:
    def __init__(self, row: int, col: int, piece: Piece):
        self.row = row
        self.col = col
        self.piece = piece
    
    def HasPiece(self):
        return self.piece != None
            