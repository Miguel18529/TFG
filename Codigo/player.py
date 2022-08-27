# -*- coding: utf-8 -*-
import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, gem_sprites, enemies_sprites, dynamite_sprites, water_sprites):
        super().__init__(groups)
        
        self.stand = pygame.image.load('../Graficos/test/player.png').convert_alpha()
        self.image = self.stand
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -26)
        
        self.down = pygame.image.load('../Graficos/player/down/down_0.png')
        self.up = pygame.image.load('../Graficos/player/up/up_0.png')
        self.left = pygame.image.load('../Graficos/player/left/left_0.png')
        self.right = pygame.image.load('../Graficos/player/right/right_0.png')
        
        #Vector (x=0, y=0) x speed
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.obstacle_sprites = obstacle_sprites
        self.gem_sprites = gem_sprites
        self.enemies_sprites = enemies_sprites
        self.dynamite_sprites = dynamite_sprites
        self.water_sprites = water_sprites
        
        self.dance1 = pygame.image.load('../Graficos/player/down/down_1.png').convert_alpha()
        self.dance2 = pygame.image.load('../Graficos/player/down/down_3.png').convert_alpha()
        self.dance3 = pygame.image.load('../Graficos/player/up/up_1.png').convert_alpha()
        self.dance4 = pygame.image.load('../Graficos/player/up/up_3.png').convert_alpha()
        
        self.dance = [self.dance1, self.dance2, self.dance3, self.dance4]
    
        self.defe = False
    
    def get_type(self):
        return 'player'
    
    def get_defe(self):
        return self.defe
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.image = self.up
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.image = self.down
        else:
            self.direction.y = 0
            self.image = self.stand
            
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.image = self.left
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.image = self.right
        else:
            self.direction.x = 0
        
        if keys[pygame.K_0]:
            self.image = random.choice(self.dance)
            
    def move(self, speed):
        #normalized speed vector, with that, same speed straight and diagonal
        if self.direction.magnitude_squared() != 0:
            self.direction = self.direction.normalize()
         
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
    
    def collision(self, direction):
        if direction == 'horizontal':
            self.speed = 5
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left
                        
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
        
        if direction == 'vertical':
            self.speed = 5
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                        
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
        
        for gem in self.gem_sprites:
            if gem.hitbox.colliderect(self.hitbox):
                gem.kill()
                self.speed = 5
        
        for enemy in self.enemies_sprites:
            if enemy.hitbox.colliderect(self.hitbox):
                self.defe = True
        
        for dynamite in self.dynamite_sprites:
            if dynamite.hitbox.colliderect(self.hitbox):
                self.defe = True
                
        for water in self.water_sprites:
            if water.hitbox.colliderect(self.hitbox):
                self.speed = 2
        
    
    def update(self):

        self.input()
        self.move(self.speed)