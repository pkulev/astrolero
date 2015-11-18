from distutils.core import setup, find_packages


def read(fname):
    with open(fname) as fin:
        return fin.read()


setup(
    name="spacegame",
    author="Pavel Kulyov",
    contributors = ["Alexey Egorov"],
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    scripts=["spacegame/run_game.py"],
    license="GPLv2",
    long_description=read("README.txt"),
#   install_requires=["pygame >=1.9.2pre"],
#   until that day
)
