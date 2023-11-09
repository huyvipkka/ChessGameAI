import pygame
from const import *
from board import Board
from dragger import Dragger


class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
    
    # draw board
    def ShowBg(self, surface: pygame.Surface):
        self.board.Draw(surface)
      
    # draw piece in board
    def ShowPiece(self, surface:pygame.Surface=None):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].HasPiece():
                    self.board.squares[row][col].piece.Draw(surface, row, col)
                    