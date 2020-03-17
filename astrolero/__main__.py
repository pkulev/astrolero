"""Entry point module."""

from astrolero.application import PygameApplication
from astrolero.game import SGame, SMainMenu, SPause


def main():
    """Entry point."""

    app = PygameApplication()
    app.set_caption("PYГAME: CTAДNЯ")
    app.register(SMainMenu)
    app.register(SGame)
    app.register(SPause)
    app.start()


if __name__ == "__main__":
    main()
