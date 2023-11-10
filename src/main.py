import pygame
import sys

from const import *
from game import Game


class Main:
    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        LOGO = pygame.image.load('assets/images/white_king.png').convert_alpha()
        pygame.display.set_icon(LOGO)
        self.running = True
        self.game = Game()
    
    def mainLoop(self):
        board = self.game.board
        dragger = self.game.dragger
        while self.running:
            # draw game
            self.game.showBg(self.screen)
            if dragger.dragging:
                self.game.showPathMove(self.screen, dragger.piece)
            self.game.showPiece(self.screen)
            
            # handle event
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.updateMouse(event.pos)
                    row_clicked, col_clicked = dragger.getRowCol()
                    if board.squares[row_clicked][col_clicked] != None:
                        piece = board.squares[row_clicked][col_clicked]
                        dragger.dragPiece(piece)
                        print(f'{piece.name} {piece.color} ({piece.row}, {piece.col})')
                        piece.moveInit(board)
                        print(f'square empty: {piece.pos_empty}')
                        print(f'square rival: {piece.pos_rival}')
                        
                        
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.updateMouse(event.pos)
                        
                elif event.type == pygame.MOUSEBUTTONUP:
                    row, col = dragger.getRowCol()
                    if board.squares[row][col] == None:
                        board.squares[dragger.piece.row][dragger.piece.col] = None
                        dragger.piece.row, dragger.piece.col = row, col
                        board.squares[row][col] = dragger.piece
                    
                    dragger.undragPiece()
                
                elif event.type == pygame.QUIT:
                    self.running = False
            
            pygame.display.update()
        pygame.quit()
        sys.exit()
    
main = Main()
main.mainLoop()