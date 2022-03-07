# -*- coding: utf-8 -*-
import pygame

from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        
        self.image = pygame.image.load('../Graficos/monsters/spirit/idle/0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        
        #Vector (x=0, y=0) x speed
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.obstacle_sprites = obstacle_sprites
    
    def move(self, speed):
        if self.direction.magnitude_squared() != 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.speed
        self.rect.y += self.speed
        

    
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left
                        
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                        
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
        
    def update(self):
        self.move(self.speed)
