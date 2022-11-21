# -*- coding: utf-8 -*-
import pygame
from settings import WORLD_MAP, TILESIZE, WORLD_MAP2, MILI, WORLD_MAP10X10,TRASH, WORLD_MAP10X10B, WORLD_MAP10X10T, WORLD_MAP5X5
from tile import Tile
from player import Player
from enemies import Enemy
from gem import Gem
from dynamite import Dynamite
from water import Water

class Level:
    def __init__(self):
        
        #get the display surface
        self.display_surface = pygame.display.get_surface()
        #Sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.gem_sprites = pygame.sprite.Group()
        self.enemies_sprites = pygame.sprite.Group()
        self.dynamite_sprites = pygame.sprite.Group()
        self.water_sprites = pygame.sprite.Group()
        #Sprite setup
        self.state_list = []
        self.create_map()
        
        self.defe = False
        
        

    def create_map(self):
        map_list = []
        for index_row, row in enumerate(WORLD_MAP10X10):
            for index_col, col in enumerate(row):
                x = index_col *TILESIZE
                y = index_row *TILESIZE
                
                map_list.append(((x,y), col))
                
                #Los sprite se ordenan en el orden que maraca esta funcion, eso afecta en la hitbox       
                if col == 'x':
                    Tile((x,y), [self.visible_sprites, self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x,y), [self.visible_sprites], self.obstacles_sprites, self.gem_sprites, self.enemies_sprites, self.dynamite_sprites, self.water_sprites)
                if col == 'e':
                    self.enemy = Enemy((x, y), [self.visible_sprites, self.enemies_sprites], self.obstacles_sprites, self.dynamite_sprites, self.water_sprites)
                if col == 't':
                    self.gem = Gem((x, y), [self.visible_sprites, self.gem_sprites])
                if col == 'd':
                    self.dinamyte = Dynamite((x, y), [self.visible_sprites, self.dynamite_sprites])
                if col == 'w':
                    self.water = Water((x, y), [self.visible_sprites, self.water_sprites])

        self.state_list = map_list
        print('states: ', self.state_list)
        
                
    def run(self):
        #upadte and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.defe = self.player.get_defe()
        self.visible_sprites.update()
        new_state_list = self.update_state_list()
        self.visible_sprites.enemy_update(self.player, new_state_list)
        
    def get_defe(self):
        return self.defe
    
    def get_gems(self):
        return self.gem_sprites
    
    def update_state_list(self):
        new_state_list = self.state_list
        pos = self.player.get_pos()
        for i in range(len(self.state_list)):
            if self.state_list[i][1] == 'p':
                new_state_list[i] = (new_state_list[i][0], ' ')
                
            if self.state_list[i][0] ==  pos:
                new_state_list[i] = (pos, 'p')
        
        return new_state_list
        
#Ordenamos los sprites en el eje Y
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        #background
        self.floor_surf = pygame.image.load("../Graficos/grass/grass03Resized.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (-600, -600))
        
    def custom_draw(self, player):
        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        
        #ordenamos los sprites por el eje Y
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
        
    def enemy_update(self, player, state_list):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player, state_list)
            
