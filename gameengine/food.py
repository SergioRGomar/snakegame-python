import random, pygame
from globals.colors import Color

class Food():
    def __init__(self,screen):
        self.sideSquare = 20
        self.pos_x = int(random.randrange(0, 500, self.sideSquare))
        self.pos_y = int(random.randrange(0, 500, self.sideSquare))
        self.drawable = 0
        
        self.screen = screen

    def generateNewPosition(self):
        self.pos_x = int(random.randrange(0, 500, self.sideSquare))
        self.pos_y = int(random.randrange(0, 500, self.sideSquare))

    def draw(self):
        self.drawable = pygame.draw.rect(self.screen, Color.RED, (self.pos_x+3,self.pos_y+3,self.sideSquare-6,self.sideSquare-6),0,3)
