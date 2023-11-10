import pygame
from square import Square
from const import *
from piece import *
        
class Board:
    def __init__(self):
        self.squares = [[Square(row, col, None) for col in range(COLS)] for row in range(ROWS)]
        self.__addPiece('white')
        self.__addPiece('black')
           
    # draw board
    def draw(self, surface: pygame.Surface):
        self.__drawBoard(surface)
        self.__drawNumberLetter(surface)
        
    def __drawBoard(self, surface: pygame.Surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = BOARD_LIGHT
                else:
                    color = BOARD_DARK
                rect = pygame.Rect(col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
    
    def __drawNumberLetter(self, surface: pygame.Surface):
        # draw 1->8, A->H
        for i in range(8):
            if i % 2 == 0:
                color = BOARD_LIGHT
            else:
                color = BOARD_DARK
            number = font_small.render(str(i+1), True, color)
            number_rect = number.get_rect(topright=(8*SQSIZE-2, i*SQSIZE-2))
            surface.blit(number, number_rect)
            
            letter = font_small.render(chr(i+65), True, color)
            letter_rect = letter.get_rect(bottomleft=(i*SQSIZE+2, 8*SQSIZE+2))
            surface.blit(letter, letter_rect)
    
    # add piece into 8x8 square
    def __addPiece(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
        
        