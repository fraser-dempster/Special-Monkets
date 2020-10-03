from turtle import width

import pygame
import random
import math
import image_loader


class Enemy(object):
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 20, 20)
        self.player = player
        self.image = image_loader.AnimatedImage("MulletMonkey_Idle")
        
    def render(self, display):
        self.image.render(display, self.rect.x, self.rect.y)

    def move_towards_player(self, player):
        print(player.rect.x, self.rect.x, player.rect.y, self.rect.y)
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        if dirvect.length() > 0:
            dirvect.scale_to_length(5)
        self.rect.move_ip(dirvect)


    def update(self):
        self.move_towards_player(self.player)

    def isDestroyed(self):
        return False
