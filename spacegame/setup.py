from distutils.core import setup

#pygame-study/
#    README.md
#    gtest.py
#    tutor/
#    spacegame/
#        Makefile
#        deltemp.bat
#        README.txt
#        setup.py
#        run_game.py [x]
#        res/
#        src/ [p]
#            __init__.py
#            controller.py
#            Classes.py
#            game.py
#            core/ [p]
#                __init__.py
#                entity.py
#                rmanager.py

setup(
    name="РYГAME: CTADNЯ",
    author="P. Kulyov",
    contributors = ["A. Egorov"],
    version="0.001dev",
    packages=["src","src.core"],
    scripts=["run_game.py"],
    license="GPLv2",
    long_description=open('README.txt').read(),
    install_requires=["pygame >=1.9.2pre"],
)
