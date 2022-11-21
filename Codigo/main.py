# -*- coding: utf-8 -*-
import pygame, sys

from settings import (WIDTH, HEIGTH, FPS)

from level import Level

import time

class Game:
    def __init__(self):
        
        #Ajustes generales
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
       
        #Cambiar título de la ventana
        pygame.display.set_caption('GUAYANDO')
        
        self.clock = pygame.time.Clock()
        
        
        self.level = Level()
        self.game_over = False
        self.points_surf = pygame.image.load('../Graficos/gems/life2.png').convert_alpha()
        self.points = 0
        self.test_font = pygame.font.Font('../Graficos/font/joystix.ttf', 40)
        self.gemas_iniciales = len(self.level.get_gems())

        
        self.victory = pygame.image.load('../Graficos/victoria/victoria4.jpeg').convert_alpha()
        self.victory = pygame.transform.scale(self.victory, [1280, 720])
        self.win = False
        
        self.defeat = pygame.image.load('../Graficos/derrota/derrota3.jpeg').convert_alpha()
        self.defeat = pygame.transform.scale(self.defeat, [1280, 720])
        
        self.defe = False
        
        self.start_screen = pygame.image.load('../Graficos/inicio/inicio.jpeg').convert_alpha()
        self.start_screen = pygame.transform.scale(self.start_screen, [1280, 720])
        self.inicio = False
        
        self.start_time = 0
        self.time = 0
        
        self.tiempo_muerto = 0
        
        self.time_exec = time.time()
        
    def get_point(self):
        if len(self.level.get_gems()) == self.gemas_iniciales -1:
            self.points += 1
            self.gemas_iniciales = len(self.level.get_gems())
    
    def display_time(self, tiempo_muerto):
        current_time = int((pygame.time.get_ticks()/1000) - self.start_time) - tiempo_muerto
        score_surf = self.test_font.render(f'{current_time}', False, (64, 64, 64))
        self.screen.blit(score_surf, (50, 50))
        self.time = current_time
    
    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.win:
                        self.__init__()
                        
                    
                    if self.defe:
                        self.__init__()
                        
                    
                    if not self.inicio:
                        self.tiempo_muerto = int((pygame.time.get_ticks()/1000) - self.start_time)
                        self.inicio = True
                        
            if not self.inicio:
                self.screen.blit(self.start_screen, (0,0))
                
            
            else: 
                if not self.win and not self.defe:
                    
                    self.level.run()
                    
                    self.screen.blit(self.points_surf, (0, 0))
                    points = self.points
                    font_surf = self.test_font.render(f':{points}', False, (64, 64, 64))
                    self.screen.blit(font_surf, (self.points_surf.get_width(), self.points_surf.get_rect().y))
                    
                    self.get_point()
                    
                    if self.gemas_iniciales == 0: self.win = True
                    
                    self.defe = self.level.get_defe()
                    
                    self.display_time(self.tiempo_muerto)
                    
                if self.win:
                    
                    self.screen.blit(self.victory, (0, 0))
                    points = self.points
                    font_surf = self.test_font.render(f'{points}', False, (64, 64, 64))
                    self.screen.blit(font_surf, (230, 455))
                    
                    current_time = self.time
                    score_surf = self.test_font.render(f'{current_time}', False, (64, 64, 64))
                    self.screen.blit(score_surf, (230, 515))
                    
                    
                if self.defe:
                    self.screen.blit(self.defeat, (0, 0))
                    points = self.points
                    points = self.points
                    font_surf = self.test_font.render(f'{points}', False, (64, 64, 64))
                    self.screen.blit(font_surf, (200, 275))

                    current_time = self.time
                    score_surf = self.test_font.render(f'{current_time}', False, (64, 64, 64))
                    self.screen.blit(score_surf, (200, 320))
                
            pygame.display.update()
            self.clock.tick(FPS)
        print('tiempo transcurrido: ', time.time() - self.time_exec)
        pygame.quit()
        sys.exit()

    
if __name__ == '__main__':
    game = Game()
    game.run()
    