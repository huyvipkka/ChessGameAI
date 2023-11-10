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
    def updateBlit(self, surface: pygame.Surface):
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
        