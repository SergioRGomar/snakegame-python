from gameengine.game import Game

objGame = Game()

while True:
    objGame.handleEvents()

    objGame.drawScenario()

       # --- Colliders

    objGame.update()
  