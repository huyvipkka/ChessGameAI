import pygame
from const import *
from board import Board
from dragger import Dragger


class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
    
    # draw board
    def showBg(self, surface: pygame.Surface):
        self.board.draw(surface)
      
    # draw piece in board
    def showPiece(self, surface:pygame.Surface=None):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.squares[row][col]
                if self.dragger.dragging and self.dragger.piece == square.piece:
                    self.dragger.updateBlit(surface)
                else:
                    square.drawPiece(surface)
                
                    