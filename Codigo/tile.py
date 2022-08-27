# -*- coding: utf-8 -*-
import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        
        self.image = pygame.image.load('../Graficos/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-5, -10)
        
    def get_type(self):
        return 'tile'