import pygame
import math

class Player(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.rect = pygame.Rect(x, y, 10, 10)

    def render(self, display):
        pygame.draw.rect(display, (255, 0, 0), self.rect, 50)