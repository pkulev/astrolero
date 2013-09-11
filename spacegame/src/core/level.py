import pygame
from .entity import *


def AbstractLevel(object):
    def __init__(self):
        pass

    def start(self):
        raise NotImplementedError("Cannot start abstract level instance")


        
