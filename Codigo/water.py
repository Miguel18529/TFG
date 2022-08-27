# -*- coding: utf-8 -*-
import pygame


class Water(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        
        self.image = pygame.image.load('../Graficos/water/water_vape.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, 26)

    def get_type(self):
        return 'water'