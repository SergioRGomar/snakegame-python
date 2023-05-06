import pygame, sys

class Game():
    def __init__(self,screen,objSnake):
        self.clock = pygame.time.Clock()
        self.sideSquare = 20

        self.screen = screen
        self.objSnake = objSnake

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                  # Move snake
                if event.key == pygame.K_w:
                    self.objSnake.setDirection(1)
                if event.key == pygame.K_a:
                    self.objSnake.setDirection(2)
                if event.key == pygame.K_s:
                    self.objSnake.setDirection(3)
                if event.key == pygame.K_d:
                    self.objSnake.setDirection(4)     

    def fill(self):
        self.screen.fill((12,12,12))

    def drawScenario(self):
        for i in range(25):
            for j in range(25):
                pygame.draw.rect(self.screen, (30,30,30), (i*self.sideSquare,j*self.sideSquare,self.sideSquare-1,self.sideSquare-1))
        
    def update(self):
        pygame.display.flip()
        self.clock.tick(120)