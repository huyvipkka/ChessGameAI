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
                piece = self.board.squares[row][col].piece
                if self.dragger.dragging and self.dragger.piece == piece:
                    self.dragger.UpdateBlit(surface)
                elif self.board.squares[row][col].HasPiece():
                    piece.Draw(surface, row, col)
                
                    