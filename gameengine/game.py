import pygame, sys
from globals.colors import Color

class Game():
    def __init__(self,screen,objSnake,objFood):
        self.points = 0
        self.clock = pygame.time.Clock()
        self.sideSquare = 20

        self.screen = screen
        self.objSnake = objSnake
        self.objFood = objFood

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
        self.screen.fill(Color.rgb(12,12,12))

    def drawScenario(self):
        for i in range(25):
            for j in range(25):
                pygame.draw.rect(self.screen, Color.GRAY , (i*self.sideSquare,j*self.sideSquare,self.sideSquare-1,self.sideSquare-1))
        
    def update(self):
        pygame.display.flip()
        self.clock.tick(120)

    def handleCollisions(self):
            # detect if snake eat a food
        if self.objFood.drawable.colliderect(self.objSnake.head):
            self.incrementPoints()

        for body_element in self.objSnake.body_drawable:
            if body_element.colliderect(self.objSnake.head):
                self.gameOver()
    
    def gameOver(self):
        self.points = 0
        self.objSnake.restart()

    def incrementPoints(self):
        self.points+=1
        self.objFood.generateNewPosition()
        self.objSnake.incrementSpeed()
        self.objSnake.length+=1
