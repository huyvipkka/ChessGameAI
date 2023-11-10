import pygame
from piece import Piece

class Square:
    def __init__(self, row: int, col: int, piece: Piece):
        self.row = row
        self.col = col
        self.piece = piece
    
    def hasPiece(self):
        return self.piece != None
    
    def drawPiece(self, surface: pygame.Surface):
        if self.hasPiece():
            self.piece.draw(surface, self.row, self.col)
            