from setuptools import setup, find_packages


def read(fname):
    with open(fname) as fin:
        return fin.read()

def files():
    return [
        "res/gfx/asteroids/*",
        "res/gfx/menu/*",
        "res/snd/*"
    ]


setup(
    name="astrolero",
    author="Pavel Kulyov",
    author_email="kulyov.pavel@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    license="GPLv2",
    long_description=read("README.md"),
    entry_points={
        "gui_scripts": [
            "astrolero = astrolero.__main__:main"]},
)
