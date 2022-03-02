# -*- coding: utf-8 -*-
import pygame
from settings import WORLD_MAP, TILESIZE
from tile import Tile
from player import Player

from debug import debug

class Level:
    def __init__(self):
        
        #get the display surface
        self.display_surface = pygame.display.get_surface()
        #Sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
        #Sprite setup
        self.create_map()
        
    def create_map(self):
        for index_row, row in enumerate(WORLD_MAP):
            for index_col, col in enumerate(row):
                x = index_col *TILESIZE
                y = index_row *TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_sprites, self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x,y), [self.visible_sprites], self.obstacles_sprites)
    def run(self):
        #upadte and draw the game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        
        debug(self.player.direction)