import sys

import pygame
from pygame.locals import *

from Core import Core
from Display import Display
from World import World
from tiles import TILES

"""
All PyGame stuff is here (rendering & inputs)
"""
def start_game():
    fps = 60
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    display = Display(fpsClock, window, TILES, fps)

    world = World(15, 10)
    core = Core(display, world, TILES)
    core.start_game()


def main():
    start_game()







if __name__ == '__main__':
    main()
