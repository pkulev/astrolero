"""Entry point module."""

import random
import sys

from spacegame.application import Application
from spacegame.game import SGame, SMainMenu, SPause


def main(args=None):
    """Entry point."""

    random.seed("menacing llama wool spike")
    App = Application("PYГAME: CTAДNЯ")
    App.addState(SGame, "game")
    App.addState(SMainMenu, "Main Menu")
    App.addState(SPause, "Pause Menu")
    App.state = "Main Menu"
    App.start()


if __name__ == "__main__":
    main(sys.argv)
