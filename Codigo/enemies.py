# -*- coding: utf-8 -*-
import pygame
import random
import time

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, dynamite_sprites, water_sprites):
        super().__init__(groups)
        
        self.image = pygame.image.load('../Graficos/monsters/spirit/idle/0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-50, -26)
        
        self.pos_o = pos
        
        #Vector (x=0, y=0) x speed
        self.direction = pygame.math.Vector2()
        self.direction.x = 1
        self.direction.y = 1
        
        self.speed = 2
        
        self.obstacle_sprites = obstacle_sprites
        self.dynamite_sprites = dynamite_sprites
        self.water_sprites = water_sprites
        
        self.state = pos
        self.state_list = []
        
        self.sprite_type = 'enemy'
        
        self.politica = {}
        self.polit = False
        
        self.p_sin_sprite = {}
        
    
    #MDP
    def set_state_list(self, state_list):
        self.state_list = state_list
        
    
    def action(self):
        return ['up', 'down', 'left', 'right']
    
    #state (posicion, tipo), ejemplo: ((64, 64), 'w')
    def reward(self, state):
        rs = {'x': -1, 'w': -0.02, ' ': -0.00001, 'p': 1, 'e': -1, 't': -0.00001, 'd': -1}
        return rs[state[1]]
    
    
    def transitionL(self, state, action):
        t = time.time()
        ts = {}
        dic_states = self.get_dic_states()
        #print('d: ', dic_states)
        #print('empiezo> ', state)
        if state[0][0]-64 < 0:
            #print(1)
            if state[0][1]+64 > 704:
                #print(2)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
                
            elif state[0][1]-64 < 0:
                #print(3)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
            else:
                #print(4)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
        
        elif state[0][0]+64 > 704:
            #print(5)
            if state[0][1]+64 > 704:
                #print(6)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)]}
           
            elif state[0][1]-64 < 0:
                #print(7)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)]}
            else:
                #print(8)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)]}
        else:
            #print(9, ':', state)
            if state[0][1]+64 > 704:
                #print(10)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
            
            elif state[0][1]-64 < 0:
                #print(11, ':', state)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
                #print('ts: ', ts)
                
            else:
                #print(12)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
       
        #print('t en transicion', time.time() - t)
        return ts[(state, action)]
    
    def transition(self, state, action):
        t = time.time()
        ts = {}
        dic_states = self.get_dic_states()
        #print('d: ', dic_states)
        #print('empiezo> ', state)
        if state[0][0]-64 < 0:
            #print(1)
            if state[0][1]+64 > 384:
                #print(2)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
                
            elif state[0][1]-64 < 0:
                #print(3)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
            else:
                #print(4)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
        
        elif state[0][0]+64 > 384:
            #print(5)
            if state[0][1]+64 > 384:
                #print(6)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)]}
           
            elif state[0][1]-64 < 0:
                #print(7)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)]}
            else:
                #print(8)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)]}
        else:
            #print(9, ':', state)
            if state[0][1]+64 > 384:
                #print(10)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
            
            elif state[0][1]-64 < 0:
                #print(11, ':', state)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]), dic_states[(state[0][0], state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
                #print('ts: ', ts)
                
            else:
                #print(12)
                ts = {(state, 'up'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.8), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1)],
                      (state, 'left'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'right'): [(((state[0][0], state[0][1]-64), dic_states[(state[0][0], state[0][1]-64)]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.8), (((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.1)],
                      (state, 'down'): [(((state[0][0], state[0][1]+64), dic_states[(state[0][0], state[0][1]+64)]), 0.8), (((state[0][0]-64, state[0][1]), dic_states[(state[0][0]-64, state[0][1])]), 0.1), (((state[0][0]+64, state[0][1]), dic_states[(state[0][0]+64, state[0][1])]), 0.1)]}
       
        #print('t en transicion', time.time() - t)
        return ts[(state, action)]
    
    def get_states(self):
        return self.state_list
    
    def get_type(self):
        return 'enemy'
    
    def get_dic_states(self):
        return {x[0]:x[1]  for x in self.get_states()}

    def GVI(self, U_v, U1_v, num_states_below_zero_v):
        tiempo = time.time()
        #U = U_v
        #print('U inicial: ', U)
        #U1 = U1_v
        all_states_changed = False
        num_states_below_zero = num_states_below_zero_v
        last_num_states_below_zero = 0
        itera=1
        tiempo_t = 1
        while not all_states_changed:
            for (x, y), s in self.get_states():
                if s != 'x' or s != 'e':
                    ri = self.reward(((x, y), s))
                    
                    #maxim = 0
                    #for a in self.action():
                        #mija = self.transition(((x, y), s), a)
                        #m = sum([i[1]*U[i[0]] for i in mija])
                   #     m = sum([i[1]*U[i[0]] for i in self.transition(((x, y), s), a)])
                   #     if maxim < m:
                   #         maxim = m
                   #     tiempo+=1
                   
                    maxim = max([sum([i[1]*U_v[i[0]] for i in self.transition(((x, y), s), a) ]) for a in self.action()])
                    U1_v[((x, y), s)] = ri + maxim
            U_v = U1_v
            last_num_states_below_zero = num_states_below_zero
            
            #for (x, y), s in self.get_states():
            #    tiempo+=1
            #    if s != 'x' or s != 'e':
            #        if U[((x, y), s)] <= 0:
            #            if s != 'p':
            #                num_states_below_zero += 1
            
            num_states_below_zero = sum([1 if (s != 'x' or s != 'e') and U_v[((x, y), s)] <= 0 and s != 'p' else 0 for (x, y), s in self.get_states()])
            
            if last_num_states_below_zero == num_states_below_zero: all_states_changed = True
            itera+=1
        
        #print('U final:, ', U)
       # print('itera: ', itera)
       # print(tiempo_t)
       # print(time.time() - tiempo)
        return U_v
        
    def move(self, speed):
        
        if self.direction.magnitude_squared() != 0:
            self.direction = self.direction.normalize()
            
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
    
    def moveGVI(self, speed, polit):
        if self.get_states():
            U = {x: self.reward(x) for x in self.get_states()}
            U1 = {x: self.reward(x) for x in self.get_states()}
            num_states_below_zero = sum([1 for x in self.get_states() if self.reward(x) < 0])
            
            self.politica = self.GVI(U, U1, num_states_below_zero)
            self.polit = True
#            self.p_sin_sprite = {(x, y): self.politica[(x, y),s] if s != 'x' else (x, y): 0 for (x, y), s in self.politica}
            self.p_sin_sprite = {(x, y) : self.politica[(x, y), s] for (x, y), s in self.politica}
            
            #for (x, y),s in self.politica:
            #    if s!='x':
            #        self.p_sin_sprite[(x, y)] = self.politica[(x, y),s]
            #    else:
            #        self.p_sin_sprite[(x, y)] = 0.0
            
        #print('p: ', self.politica)
        
        #print(self.p_sin_sprite)
        if self.direction.magnitude_squared() != 0:
            self.direction = self.direction.normalize()

        if polit:
            pos_conv = self.convertir_estado(self.hitbox.x, self.hitbox.y)
            
            
            opciones = {}
            if pos_conv[0] == 0:
                opciones = {('right', (1.0, 0.0)): self.p_sin_sprite[(pos_conv[0]+64, pos_conv[1])],
                        ('down', (0.0, 1.0)): self.p_sin_sprite[(pos_conv[0], pos_conv[1]+64)],
                        ('left', (-1.0, 0.0)): self.p_sin_sprite[(0, pos_conv[1])],
                        ('up', (0.0, -1.0)): self.p_sin_sprite[(pos_conv[0], pos_conv[1]-64)]}
            elif pos_conv[1] == 0:
                opciones = {('right', (1.0, 0.0)): self.p_sin_sprite[(pos_conv[0]+64, pos_conv[1])],
                        ('down', (0.0, 1.0)): self.p_sin_sprite[(pos_conv[0], pos_conv[1]+64)],
                        ('left', (-1.0, 0.0)): self.p_sin_sprite[(pos_conv[0]-64, pos_conv[1])],
                        ('up', (0.0, -1.0)): self.p_sin_sprite[(pos_conv[0], 0)]}
            else: 
                opciones = {('right', (1.0, 0.0)): self.p_sin_sprite[(pos_conv[0]+64, pos_conv[1])],
                            ('down', (0.0, 1.0)): self.p_sin_sprite[(pos_conv[0], pos_conv[1]+64)],
                            ('left', (-1.0, 0.0)): self.p_sin_sprite[(pos_conv[0]-64, pos_conv[1])],
                            ('up', (0.0, -1.0)): self.p_sin_sprite[(pos_conv[0], pos_conv[1]-64)]}
            mayor = None
            valor = -10000
            for x in opciones:
                if opciones[x] > valor:
                    mayor = x
                    valor = opciones[x]
            
            
            '''
            rand = random.uniform(0,1)
            
            if rand < 0.8:
                self.direction.x = mayor[1][0]
                self.direction.y = mayor[1][1]
            else:
                n_mayor = self.mayor_falla(mayor[1][0], mayor[1][1])
                self.direction.x = n_mayor[0]
                self.direction.y = n_mayor[1]
            '''
            
            self.direction.x = mayor[1][0]
            self.direction.y = mayor[1][1]
        #print(self.direction)
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        self.state = (self.hitbox.x, self.hitbox.y)

  


    def mayor_falla(self, x, y):
        rand = random.randint(0, 1)
        if rand == 0:
            if x == 1:
                y = 1
                x = 0
            elif y == 1:
                x = -1
                y = 0
            elif x == -1:
                x = 0
                y = -1
            elif y == -1:
                x = 1
                y = 0
        else:
            if x == 1:
                y = -1
                x = 0
            elif y == 1:
                x = 1
                y = 0
            elif x == -1:
                x = 0
                y = 1
            elif y == -1:
                x = -1
                y = 0
        return (x, y)
        
    
    def convertir_estado(self, x, y):
        nueva_x = 0
        nueva_y = 0
        i_prev = 0
        y_ready = False
        x_ready = False
        for i in range(0, 768, 64):
            if x < i and not x_ready:
                nueva_x = i_prev
                x_ready = True
            if y < i and not y_ready:
                
                nueva_y = i_prev
                y_ready = True
            i_prev = i
        return (nueva_x, nueva_y)

    def collision(self, direction):
        if direction == 'horizontal':
            self.speed = 2
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #moving right
                        self.hitbox.right = sprite.hitbox.left    
                        
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                    #self.direction.x *= -1
        if direction == 'vertical':
            self.speed = 2
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    
                    if self.direction.y > 0: #moving down
                        self.hitbox.bottom = sprite.hitbox.top
                        
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                    #self.direction.y *= -1
        
        for dynamite in self.dynamite_sprites:
            if dynamite.hitbox.colliderect(self.hitbox):
                self.hitbox.x = self.pos_o[0]
                self.hitbox.y = self.pos_o[1]
                self.state = (self.hitbox.x, self.hitbox.y)
                self.speed = 2
                
        for water in self.water_sprites:
            if water.hitbox.colliderect(self.hitbox):
                self.speed = 1
    
    def get_player_distance_direction(self,player):
        
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance,direction)
    
    def enemy_update(self, player, state_list):
        #self.direction = self.get_player_distance_direction(player)[1]
        self.state_list = state_list
        #print(self.state_list)
    
    def update(self):
        self.moveGVI(self.speed, self.polit)
        #self.move(self.speed)
        
        
