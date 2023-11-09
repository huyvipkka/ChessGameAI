import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600

ROWS = 8
COLS = 8

SQSIZE = WIDTH // COLS

BOARD_DARK = (167,113,31)
BOARD_LIGHT = (255,251,161)

font_small = pygame.font.SysFont('arial', SQSIZE//3, True)
