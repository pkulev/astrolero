import sources.CGame

if __name__ == "__main__":
    spacegame = sources.CGame.Game()

    while True:
        spacegame.handleEvents()
        spacegame.updateState()
        spacegame.drawScreen()
