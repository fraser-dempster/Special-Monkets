import pygame
import random
import math
import image_loader
import config

class Enemy(object):
    def __init__(self, x, y, player):
        self.xsize = config.ENEMY_XSIZE
        self.ysize = config.ENEMY_YSIZE

        self.x = x
        self.y = y
        self.player = player
        self.image = image_loader.AnimatedImage("MulletMonkey_Idle", xsize = self.xsize, ysize = self.ysize)
      #  self.image = pygame.transform.scale(self.image, )
        self.rect = pygame.Rect(x, y, self.xsize, self.ysize)

        self.hascollided = False


    def render(self, display):
        self.image.render(display, self.rect.x, self.rect.y)

    def move_towards_player(self, player):
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        if dirvect.length() > 0:
            dirvect.scale_to_length(config.ENEMY_MOVEMENT_SPEED)
        self.rect.move_ip(dirvect)


    def update(self):
        self.move_towards_player(self.player)

    def isDestroyed(self):
        return self.hascollided
