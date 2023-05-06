import pygame
from .game import Game


green_cola = (106,160,26)
green = (127,236,17)
gray = (30,30,30)
red = (230,38,13)
blue = (20,77,100)
white = (0,0,0)

class Snake():
    def __init__(self,screen):
        self.sideSquare = 20
        self.pos_x = 220
        self.pos_y = 220
        self.speed = 0.8
        self.aux = 0
        self.direction = 4

        self.screen = screen

    def emit(self):
        self.head = pygame.draw.rect(self.screen, green, (self.pos_x,self.pos_y,self.sideSquare,self.sideSquare))

    def move(self):
        self.aux += self.speed # steps

        if(self.aux > 20):
            
            # new head position
            if self.direction == 1:
                self.pos_y-=20
            if self.direction == 2:
                self.pos_x-=20
            if self.direction == 3:
                self.pos_y+=20
            if self.direction == 4:
                self.pos_x+=20

            self.aux = 0


    def setDirection(self,direction):
        aux_pasa = 0 # find invalid movements
        if self.direction == 4 and (direction == 1 or direction == 3):
            aux_pasa = 1
        if self.direction == 2 and (direction == 1 or direction == 3):
            aux_pasa = 1
        if self.direction == 1 and (direction == 2 or direction == 4):
            aux_pasa = 1
        if self.direction == 3 and (direction == 2 or direction == 4):
            aux_pasa = 1

        if aux_pasa:
            self.direction = direction
        