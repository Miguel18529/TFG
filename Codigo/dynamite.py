# -*- coding: utf-8 -*-
import pygame

class Dynamite(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        
        self.image = pygame.image.load('../Graficos/dynamite/dynamite2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-20, -10)
    
    def get_type(self):
        return 'dynamite'