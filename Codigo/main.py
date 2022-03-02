# -*- coding: utf-8 -*-
import pygame, sys

from settings import (WIDTH, HEIGTH, FPS)

from level import Level

class Game:
    def __init__(self):
        
        #Ajustes generales
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        #Cambiar título de la ventana
        pygame.display.set_caption('GUAYANDO')
        self.clock = pygame.time.Clock()
        
        self.level = Level()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()