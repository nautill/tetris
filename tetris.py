import pygame
from copy import deepcopy
from random import choice, randrange

import pygame
from copy import deepcopy
from random import choice, randrange


width, height = 10, 20
TILE = 45
RESOLUTION = width * TILE, height * TILE
FPS = 60


pygame.init
game_sc = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(width) for y in range(height)]
figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]
