from turtle import width

import pygame
import random
import math

class enemyObject(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.width = width
        self.rect = pygame.Rect(100, 100, 20, 20)
        
    def draw(self, display):
        pygame.draw.rect(display, (0, 255, 0), self.rect, 50)

    def move_towards_player(self, player):
        print(player.rect.x, self.rect.x, player.rect.y, self.rect.y)
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        if dirvect.length() > 0:
            dirvect.normalize()
        dirvect.scale_to_length(5)
        self.rect.move_ip(dirvect)