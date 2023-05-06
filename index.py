import pygame
from gameengine.game import Game
from gameengine.snake import Snake
from gameengine.food import Food


pygame.init()
size = (500,500)
screen = pygame.display.set_mode(size,pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption('Snake Game - pygame')

objSnake = Snake(screen) 
objFood = Food(screen) 
objGame = Game(screen,objSnake,objFood)

while True:
  
    objGame.handleEvents()

    objSnake.move()

    objGame.fill()
    objGame.drawScenario()
    
    objSnake.draw()
    objFood.draw()

    objGame.handleCollisions()
    
    objGame.update()