import sys

import pygame
from pygame import QUIT, MOUSEWHEEL, KEYDOWN

from World import World
from tiles import LeftRightTile


class Core:

    def __init__(self, display, world, tiles):
        self.display = display
        self.world = world
        self.tiles = tiles
        self.selected_tile: int = 0
        self.pause: bool = False
        self.tiles_info: bool = False
        self.counter: int = 0

    def start_game(self):
        self.generate_map()
        self.run_game_loop()

    def run_game_loop(self):
        while True:
            # Get mouse position
            mouse_position = self.display.get_mouse_world_position(self.world)
            # Get inputs
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEWHEEL:
                    if event.y == -1:
                        if self.selected_tile == 0:
                            self.selected_tile = len(self.tiles) - 1
                        else:
                            self.selected_tile -= 1
                    else:
                        if self.selected_tile == len(self.tiles) - 1:
                            self.selected_tile = 0
                        else:
                            self.selected_tile += 1
                if event.type == KEYDOWN:
                    if event.unicode == " ":
                        self.pause = not self.pause
                    elif event.scancode == 58:
                        # Press F1
                        self.tiles_info = not self.tiles_info
            if pygame.mouse.get_pressed()[0]:
                tile = self.world.get_tile_at_position(mouse_position[0], mouse_position[1])
                if tile:
                    tile.step_on()

            # update physics
            self.world.update()
            if not self.pause:
                if self.counter % 30 == 0:
                    self.world.update_moving()
            # render
            self.counter += 1
            self.display.render(self.world, self.selected_tile, mouse_position, self.pause, self.tiles_info)
            pass

    def generate_map(self):
        self.world.add_tile(LeftRightTile, 0, 0)
        self.world.add_tile(LeftRightTile, 0, 1)
        self.world.add_tile(LeftRightTile, 0, 2)
        self.world.add_tile(LeftRightTile, 0, 3)
        self.world.add_tile(LeftRightTile, 0, 4)
        self.world.add_tile(LeftRightTile, 0, 5)
        self.world.add_tile(LeftRightTile, 0, 6)
        self.world.add_tile(LeftRightTile, 0, 7)
        self.world.add_tile(LeftRightTile, 0, 8)
        self.world.add_tile(LeftRightTile, 0, 9)
