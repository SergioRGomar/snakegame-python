import pygame
from .game import Game


green_cola = (106,160,26)
green = (127,236,17)
gray = (30,30,30)
red = (230,38,13)
blue = (20,77,100)
white = (0,0,0)

class Snake(Game):
    def __init__(self):
        Game.__init__(self)

        self.pos_x = 220
        self.pos_y = 220

    def emit(self):
        self.cabeza = pygame.draw.rect(self.screen, green, (self.pos_x,self.pos_y,self.sideSquare,self.sideSquare))
