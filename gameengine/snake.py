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

        self.length = 3
        self.head = 0 
        self.body_positions = []
        self.body_drawable = []

        self.screen = screen

        self.initTail()
       
    def initTail(self):
        for i in range(self.length):
            self.body_positions.append([self.pos_x-20*(i+1),self.pos_y])

    def draw(self):
        # draw head
        self.head = pygame.draw.rect(self.screen, green, (self.pos_x,self.pos_y,self.sideSquare,self.sideSquare))

        # draw tail
        self.body_drawable = []
        for posicion in self.body_positions:
            self.body_drawable.append(pygame.draw.rect(self.screen, green_cola, (posicion[0],posicion[1],self.sideSquare,self.sideSquare)))
   
    def incrementSpeed(self):
        self.speed+=0.1

    def move(self):
        self.aux += self.speed # steps

        if(self.aux > 20):
            # new tail position 
                # this is my "tail to head algorithm", 
                # this consist in remove the last position of tail an colocate in the current head position 
            aux_positions = self.body_positions
            self.body_positions = [] 
            self.body_positions.append([self.pos_x,self.pos_y])
            for i in range(self.length-1):  
                self.body_positions.append(aux_positions[i])

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
        invalid_movement_flag = 0 
        
        # find invalid movements
        if self.direction == 4 and (direction == 1 or direction == 3):
            invalid_movement_flag = 1
        if self.direction == 2 and (direction == 1 or direction == 3):
            invalid_movement_flag = 1
        if self.direction == 1 and (direction == 2 or direction == 4):
            invalid_movement_flag = 1
        if self.direction == 3 and (direction == 2 or direction == 4):
            invalid_movement_flag = 1

        if invalid_movement_flag:
            self.direction = direction