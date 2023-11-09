import pygame
from piece import *
from const import *

class Dragger:
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.init_row = 0
        self.init_col = 0
    
    # draw piece position = mouse_pos and blit piece.img in screen
    def UpdateBlit(self, surface: pygame.Surface):
        self.piece.img_rect.center = self.mouseX, self.mouseY
        surface.blit(self.piece.img, self.piece.img_rect)
        
    # other method drag
    def UpdateMouse(self, mouse_pos):
        self.mouseX, self.mouseY = mouse_pos
        
    def SaveInit(self, mouse_pos):
        self.init_row = mouse_pos[1] // SQSIZE
        self.init_col = mouse_pos[0] // SQSIZE
        
    def DragPiece(self, piece: Piece):
        self.piece = piece
        self.dragging = True
        
    def UndragPiece(self):
        self.piece = None
        self.dragging = False
        