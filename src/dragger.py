import pygame
from piece import *
from const import *

class Dragger:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
    
    # draw piece position = mouse_pos and blit piece.img in screen
    def drawPieceDragging(self, surface: pygame.Surface):
        row, col = self.getRowCol()
        rect = pygame.Rect(col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)
        pygame.draw.rect(surface, 'red', rect, 3)
        
        self.piece.img_rect.center = self.mouseX, self.mouseY
        surface.blit(self.piece.img, self.piece.img_rect)
        
        
    # other method drag
    def updateMouse(self, mouse_pos):
        self.mouseX, self.mouseY = mouse_pos
        
    def getRowCol(self):
        return self.mouseY // SQSIZE, self.mouseX // SQSIZE
    
        
    def dragPiece(self, piece: Piece):
        self.piece = piece
        self.dragging = True
        
    def undragPiece(self):
        self.piece = None
        self.dragging = False
        
    def movePiece(self, board):
        """
        if row and col valid
        set old board position = None
        set new piece position and set new board position = piece
        """
        row, col = self.getRowCol()
        if self.dragging:
            if (row, col) in self.piece.pos_rival or (row, col) in self.piece.pos_empty:
                board.squares[self.piece.row][self.piece.col] = None
                self.piece.move(row, col)
                board.squares[row][col] = self.piece
                if self.piece.name == "pawn":
                    self.piece.first_turn = False
        