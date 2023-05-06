from gameengine.game import Game
from gameengine.snake import Snake

objGame = Game()
objSnake = Snake() 

while True:
  
    objGame.handleEvents()

    objGame.fill()

    objGame.drawScenario()

    objSnake.emit()
    
    objGame.update()
  