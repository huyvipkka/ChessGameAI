import os
import pygame
from const import *
from move import *

class Piece:
    def __init__(self, name: str, color: str, row: int, col: int, value: float):
        self.name = name
        self.color = color
        self.row = row
        self.col = col
        
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        
        self.path_img = os.path.join(
            f'assets/images/{self.color}_{self.name}.png'
        )
        self.img = pygame.image.load(self.path_img).convert_alpha()
        self.img_rect = self.img.get_rect()
        
    def draw(self, surface: pygame.Surface):
        self.img_rect.center = self.col*SQSIZE + SQSIZE//2, self.row*SQSIZE + SQSIZE//2
        surface.blit(self.img, self.img_rect)
    



class Pawn(Piece):
    def __init__(self, color, row: int, col: int):
        self.dir = -1 if color == 'white' else 1
        Piece.__init__(self, 'pawn', color, row, col, 1.0)
        
        
class Knight(Piece, KinghtMove):
    def __init__(self, color, row: int, col: int):
        Piece.__init__(self, 'knight', color, row, col, 3.0)
        KinghtMove.__init__(self, color, row, col)
        
class Bishop(Piece):
    def __init__(self, color, row: int, col: int):
        Piece.__init__(self, 'bishop', color, row, col, 3.5)


class Rook(Piece):
    def __init__(self, color, row: int, col: int):
        Piece.__init__(self, 'rook', color, row, col, 5.0)


class Queen(Piece):
    def __init__(self, color, row: int, col: int):
        Piece.__init__(self, 'queen', color, row, col, 9.0)


class King(Piece):
    def __init__(self, color, row: int, col: int):
        Piece.__init__(self, 'king', color, row, col, 10000)
