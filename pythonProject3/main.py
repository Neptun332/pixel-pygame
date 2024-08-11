import sys

import pygame
from pygame.locals import *

from Core import Core
from Display import Display
from EventBroker import EventBroker
from GameOver import GameOver
from World import World
from event_handlers.GameOverHandler import GameOverHandler
from tiles import TILES

def main():
    stop_token = False
    fps = 60
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    display = Display(fpsClock, window, TILES, fps)

    event_broker = EventBroker()
    world = World(15, 10)
    core = Core(display, world, TILES, stop_token, event_broker)
    game_over_handler = GameOverHandler(core, main)
    event_broker.subscribe(game_over_handler.handle, GameOver)
    core.start_game()







if __name__ == '__main__':
    main()
