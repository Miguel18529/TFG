# -*- coding: utf-8 -*-

import pygame
import random
class Gem(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        
        #self.image = pygame.image.load('../Graficos/particles/thunder/4.png').convert_alpha()
        self.orange = pygame.image.load('../Graficos/gems/orange.png').convert_alpha()
        self.pink = pygame.image.load('../Graficos/gems/pink.png').convert_alpha()
        self.green = pygame.image.load('../Graficos/gems/green.png').convert_alpha()
        self.dblue = pygame.image.load('../Graficos/gems/dblue.png').convert_alpha()
        
        self.image_list = [self.orange, self.pink, self.green, self.dblue]
        self.image = random.choice(self.image_list)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-20, -10)
        
    def get_type(self):
        return 'gem'