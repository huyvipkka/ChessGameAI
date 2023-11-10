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
    def showPiece(self, surface: pygame.Surface):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board.squares[row][col]
                if self.dragger.dragging and self.dragger.piece == piece:
                    self.dragger.updateBlit(surface)
                elif piece != None:
                    piece.draw(surface)
         
    def showPathMove(self, surface: pygame.Surface, piece):
        self.board.drawPathPiece(surface, piece)  
    
    def showMoves(self, surface: pygame.Surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            
            for move in piece.moves:
                move.draw(surface)
                
                    