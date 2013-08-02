import CGame

if __name__ == "__main__":
    spacegame = CGame.Game()

    while True:
        spacegame.handleEvents()
        spacegame.updateState()
        spacegame.drawScreen()
