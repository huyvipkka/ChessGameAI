import pygame
import sys

from const import *
from piece import *
from game import Game
from square import Square


class Main:
    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        LOGO = pygame.image.load('assets/images/white_king.png').convert_alpha()
        pygame.display.set_icon(LOGO)
        self.running = True
        self.game = Game()
    
    def MainLoop(self):
        board = self.game.board
        dragger = self.game.dragger
        
        while self.running:
            # draw game
            self.game.ShowBg(self.screen)
            self.game.ShowPiece(self.screen)
            if dragger.dragging:
                dragger.UpdateBlit(self.screen)
            
            # handle event
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.UpdateMouse(event.pos)
                    row_clicked = dragger.mouseY // SQSIZE
                    col_clicked = dragger.mouseX // SQSIZE
                    if board.squares[row_clicked][col_clicked].HasPiece():
                        piece = board.squares[row_clicked][col_clicked].piece
                        dragger.SaveInit(event.pos)
                        dragger.DragPiece(piece)
                    
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.UpdateMouse(event.pos)
                        
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.UndragPiece()
                
                elif event.type == pygame.QUIT:
                    self.running = False
            

            pygame.display.update()
        pygame.quit()
        sys.exit()
    
main = Main()
main.MainLoop()