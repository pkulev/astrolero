::This script for deleting temporary files on windows
@echo off
del *.pyc *.*~ *.pyo
del src\*.pyc src\*.py~ src\*.pyo
del src\core\*.pyc src\core\*py~ src\core\*.pyo