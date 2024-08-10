from typing import Tuple

import pygame

from World import World
from utils.clamp import clamp


class Display:

    def __init__(self, fpsClock, window, tiles, fps):
        pygame.init()
        self.fpsClock = fpsClock
        self.window = window
        self.tiles = tiles
        self.fps = fps
        self.font = pygame.font.Font('resources/font.otf', 18)
        self.small_font = pygame.font.Font('resources/font.otf', 14)
        self.paused_text = self.font.render("Simulation paused", False, (255, 255, 255))
        pygame.display.set_caption('jetmen-revival-pygame')

    def render(self, world: World, selected_tile: int, mouse_position: Tuple[int, int], paused: bool, tiles_info: bool):
        # set window caption (show FPS)
        pygame.display.set_caption(f'Jetmen Revival | FPS: {int(self.fpsClock.get_fps())}')
        # render world
        surface = pygame.Surface((world.width, world.height))
        for tile in world.tiles:
            surface.set_at((tile.x, tile.y), tile.color)
        surface.set_at(mouse_position, (255, 255, 255))
        scaled_surface = pygame.transform.scale(surface, self.window.get_size())
        # render selected tile
        tile_text = self.font.render(
            f"selected ({selected_tile + 1}/{len(self.tiles)}): {self.tiles[selected_tile].NAME}",
            False,
            (255, 255, 255)
        )
        scaled_surface.blit(tile_text, (10, 10))
        # render additional information if tiles info is on
        if tiles_info:
            total_particles_text = self.font.render(f"Total tiles: {len(world.tiles)}", False, (255, 255, 255))
            scaled_surface.blit(total_particles_text, (10, 50))
            tile = world.spatial_matrix[mouse_position[1]][mouse_position[0]]
            if tile:
                mouse_pos = pygame.mouse.get_pos()
                tile_type_text = self.small_font.render(
                    f"Type: {tile.NAME}",
                    False,
                    (255, 255, 255)
                )
                tile_type_text_shadow = self.small_font.render(
                    f"Type: {tile.NAME}",
                    False,
                    (0, 0, 0)
                )
                scaled_surface.blit(tile_type_text_shadow, (mouse_pos[0] + 12, mouse_pos[1] + 2))
                scaled_surface.blit(tile_type_text, (mouse_pos[0] + 10, mouse_pos[1]))
                if "heat" in tile.__dict__:
                    tile_heat_text = self.small_font.render(
                        f"Heat: {tile.heat}",
                        False,
                        (255, 255, 255)
                    )
                    tile_heat_text_shadow = self.small_font.render(
                        f"Heat: {tile.heat}",
                        False,
                        (0, 0, 0)
                    )
                    scaled_surface.blit(tile_heat_text_shadow, (mouse_pos[0] + 12, mouse_pos[1] + 22))
                    scaled_surface.blit(tile_heat_text, (mouse_pos[0] + 10, mouse_pos[1] + 20))
        # render pause text if the simulation is paused
        if paused:
            scaled_surface.blit(self.paused_text, (self.window.get_width() - self.paused_text.get_width() - 10, 10))
        # render surface to window
        self.window.blit(scaled_surface, (0, 0))
        pygame.display.flip()
        self.fpsClock.tick(self.fps)

    def get_mouse_world_position(self, world: World) -> Tuple[int, int]:
        window_size = self.window.get_size()
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = clamp(int((mouse_pos[0] / window_size[0]) * world.width), 0, world.width - 1)
        mouse_y = clamp(int((mouse_pos[1] / window_size[1]) * world.height), 0, world.height - 1)
        return mouse_x, mouse_y
