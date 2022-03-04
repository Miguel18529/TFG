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
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        
        #Sprite setup
        self.create_map()
        
    def create_map(self):
        for index_row, row in enumerate(WORLD_MAP):
            for index_col, col in enumerate(row):
                x = index_col *TILESIZE
                y = index_row *TILESIZE
                #Los sprite se ordenan en el orden que maraca esta funcion, eso afecta en la hitbox
                if col == 'x':
                    Tile((x,y), [self.visible_sprites, self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x,y), [self.visible_sprites], self.obstacles_sprites)
    def run(self):
        #upadte and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        
        
        
#Ordenamos los sprites en el eje Y
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
    def custom_draw(self, player):
        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        #ordenamos los sprites por el eje Y
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
            
