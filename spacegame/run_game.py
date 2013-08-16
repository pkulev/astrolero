#! /usr/bin/env python
import sources.game

if __name__ == "__main__":
    spacegame = sources.game.CGame()

    while True:
        spacegame.handleEvents()
        spacegame.updateState()
        spacegame.drawScreen()
