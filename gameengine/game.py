import pygame, sys

class Game():
    def __init__(self):
        pygame.init()
        self.sideSquare = 20
        size = (500,500)
        self.screen = pygame.display.set_mode(size,pygame.RESIZABLE | pygame.SCALED)
        pygame.display.set_caption('Snake Game - pygame')

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def fill(self):
        self.screen.fill((12,12,12))

    def drawScenario(self):
        for i in range(25):
            for j in range(25):
                pygame.draw.rect(self.screen, (30,30,30), (i*self.sideSquare,j*self.sideSquare,self.sideSquare-1,self.sideSquare-1))
        
    def update(self):
        pygame.display.flip()
