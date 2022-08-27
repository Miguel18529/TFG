# -*- coding: utf-8 -*-
import pygame, sys

class WorldMap1:
    #dim: dimensiones del mapa (x, y)
    def __init__(self, dim):
        self.dim = dim

    
            
            
class Game:
    def __init__(self):
        
        #Ajustes generales
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
       
        #Cambiar título de la ventana
        pygame.display.set_caption('GUAYANDO')
        
        self.worldMap = WorldMap1((20, 20))
        
        self.clock = pygame.time.Clock()
        
        self.game_over = False
    
        
    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    
if __name__ == '__main__':
    game = Game()
    game.run()
    