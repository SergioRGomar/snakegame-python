import pygame, sys

from gameengine.snake import Snake
from gameengine.game import Game

pygame.init()
size = (500,500)
screen = pygame.display.set_mode(size,pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption('Snake Game - pygame')


objSnake = Snake(screen) 

objGame = Game(screen,objSnake)


while True:
  
    objGame.handleEvents()

    objSnake.move()

    objGame.fill()
    objGame.drawScenario()
    
    objSnake.emit()
    

    objGame.update()
  