import os
import pygame
from const import *

class Piece:
    def __init__(self, name: str, color: str, value: float):
        self.name = name
        self.color = color
        self.moves = []
        self.moved = False
        
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        
        self.path_img = os.path.join(
            f'assets/images/{self.color}_{self.name}.png'
        )
        self.img = pygame.image.load(self.path_img).convert_alpha()
        self.img_rect = self.img.get_rect()
        
    def AddMoves(self, move):
        self.moves.append(move)
        
    def Draw(self, surface: pygame.Surface, row: int, col: int):
        self.img_rect.center = col*SQSIZE + SQSIZE//2, row*SQSIZE + SQSIZE//2
        surface.blit(self.img, self.img_rect)
    



class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        Piece.__init__(self, 'pawn', color, 1.0)
        
class Knight(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'knight', color, 3.0)
        
class Bishop(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'bishop', color, 3.5)
        
class Rook(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'rook', color, 5.0)
        
class Queen(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'queen', color, 9.0)
        
class King(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'king', color, 10000)