import pygame
W, H = 10, 20
TITLE = 30 
GAME_RESOLUTION = W * TITLE, H * TITLE
FPS = 45
pygame.init()
game_screen = pygame.display.pygame.display.set_mode(GAME_RESOLUTION)
clock = pygame.time.Clock()
