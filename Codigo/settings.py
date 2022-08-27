# -*- coding: utf-8 -*-
# ajustes del juego
WIDTH    = 1280 
HEIGTH   = 720
FPS      = 60
TILESIZE = 64

#El tamaño de los sprites es de 64 (TILESIZE) por tanto, en orden se cuentan como: (0, 0) (64, 0)....
WORLD_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','p',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ','e',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','e',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ','t',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ','e',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','e',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]

WORLD_MAP2 = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','',' ',' ',' ',' ',' ','x'],
['x','x',' ',' ','x',' ',' ',' ',' ',' ',' ','e',' ',' ',' ','x',' ',' ','x','x'],
['x','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ','x','x'],
['x','x',' ',' ','x',' ',' ',' ',' ','p',' ',' ',' ',' ',' ','x',' ',' ','x','x'],
['x','x',' ',' ','x',' ',' ',' ','x','x','x','x',' ',' ',' ','x',' ',' ','x','x'],
['x','x',' ',' ','x',' ',' ',' ','x','x','x','x',' ',' ',' ','x',' ',' ','x','x'],
['x','x',' ',' ','x',' ',' ',' ','x','x','x','x',' ',' ',' ','x',' ',' ','x','x'],
['x','x',' ',' ','x',' ',' ',' ','x','x','x','x',' ',' ',' ','x',' ',' ','x','x'],
['x','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]


MILI = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','x',' ',' ',' ','x',' ','x',' ','x',' ',' ',' ','x',' ',' ',' ',' ','x'],
['x',' ','x','x',' ','x','x',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','x',' ','x',' ','x',' ','x',' ','x',' ',' ',' ','x',' ',' ',' ',' ','x'],
['x',' ','x',' ',' ',' ','x',' ','x',' ','x',' ',' ',' ','x',' ',' ',' ','x','x'],
['x',' ','x',' ',' ',' ','x',' ','x',' ','x',' ',' ',' ','x',' ',' ',' ','x','x'],
['x',' ','x',' ',' ',' ','x',' ','x','p','x',' ',' ',' ','x',' ',' ',' ','x','x'],
['x',' ','x',' ',' ',' ','x',' ','x',' ','x',' ',' ',' ','x',' ',' ',' ','x','x'],
['x',' ','x',' ',' ',' ','x',' ','x',' ','x',' ',' ',' ','x',' ',' ',' ','x','x'],
['x',' ','x',' ',' ',' ','x',' ','x',' ','x',' ',' ',' ','x',' ',' ',' ','x','x'],
['x',' ','x',' ',' ',' ','x',' ','x',' ','x','x','x',' ','x',' ',' ',' ','x','x'],
['x',' ','x',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]

WORLD_MAP10X10T = [
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','t',' ',' ',' ','t','e',' ',' ',' ','t','x'],
['x',' ','x','x','x',' ',' ','x','x','x',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x',' ','x','t','p','e',' ','x',' ','x','x'],
['x','x','t','x',' ','x','x','t','x','t','x','x'],
['x','x',' ','x',' ','x','x',' ','x',' ','x','x'],
['x','x',' ','x',' ',' ',' ',' ','x',' ','x','x'],
['x',' ',' ',' ',' ','e',' ',' ',' ',' ',' ','x'],
['x',' ','x','x','x',' ',' ','x','x','x',' ','x'],
['x',' ','t',' ',' ',' ',' ',' ',' ',' ','t','x'],
['x','x','x','x','x','x','x','x','x','x','x','x']
]

WORLD_MAP10X10 = [
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','t',' ',' ',' ','w','e',' ',' ',' ',' ','x'],
['x',' ','x','x','x',' ',' ','x','x','x',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x',' ','x',' ',' ','e',' ','x',' ','x','x'],
['x','x',' ','x',' ','x','x','t','x',' ','x','x'],
['x','x',' ','x',' ','x','x',' ','x','p','x','x'],
['x','x',' ','x',' ',' ',' ',' ','x',' ','x','x'],
['x',' ',' ',' ',' ','e',' ',' ',' ',' ',' ','x'],
['x',' ','x','x','x',' ',' ','x','x','x',' ','x'],
['x',' ','d',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x']
]

WORLD_MAP10X10B = [
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','t',' ',' ',' ','w','e',' ',' ',' ',' ','x'],
['x',' ','x','x','x',' ',' ','x','x','x',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x',' ','x',' ',' ','e',' ','x',' ','x','x'],
['x','x',' ','x',' ','x','x','t','x',' ','x','x'],
['x','x',' ','x','d','x','x',' ','x',' ','x','x'],
['x','x',' ','x',' ',' ',' ',' ','x',' ','x','x'],
['x',' ',' ',' ','p',' ',' ',' ',' ',' ',' ','x'],
['x',' ','x','x','x',' ',' ','x','x','x',' ','x'],
['x',' ','d',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x']
]

TRASH = [
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','p','x','t','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x'],]