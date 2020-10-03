import pygame
import random
import config
import math
import image_loader
import enemy

class ghost(enemy.Enemy):
    def __init__(self, x, y, player):
        super().__init__(x, y, player)

        self.image = image_loader.AnimatedImage("Ghost_Right", xsize=self.xsize, ysize=self.ysize)




