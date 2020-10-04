import pygame
import random
import config
import math
import image_loader
import enemy

class zombie(enemy.Enemy):
    def __init__(self, x, y, player):
        super().__init__(x, y, player)


    def move_towards_player(self, player):
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        tup = tuple(dirvect)
        if tup[0] > 0:
            self.image = image_loader.AnimatedImage("Zombie_IdleRight", xsize=self.xsize, ysize=self.ysize)
        else:
            self.image = image_loader.AnimatedImage("Zombie_IdleLeft", xsize=self.xsize, ysize=self.ysize)



