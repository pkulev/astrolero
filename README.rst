|PyPI| |Build Status| |codecov.io|

=========
Astrolero
=========

**Astrolero** is 2D space shooter written in python using EAF and pygame.

Requirements
============

* >=eaf-0.1.2
* >=pygame-1.9.2

Installation
============

.. code-block:: console

	$ pip install astrolero


Development
===========

Installation
------------

.. code-block:: console

   $ poetry install

Testing
-------

.. code-block:: console

   $ poetry run pytest -s -v tests/  # run all tests
   $ poetry run pytest --cov=astrolero -s -v tests/  # run all tests with coverage


Documentation
-------------

* **To be added**

.. |PyPI| image:: https://badge.fury.io/py/astrolero.svg
   :target: https://badge.fury.io/py/astrolero
.. |Build Status| image:: https://github.com/pkulev/astrolero/workflows/CI/badge.svg
.. |codecov.io| image:: http://codecov.io/github/pkulev/astrolero/coverage.svg?branch=master
   :target: http://codecov.io/github/pkulev/astrolero?branch=master
