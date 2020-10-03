import pygame
import math
import image_loader

class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 10, 10)
        self.image = image_loader.AnimatedImage("MulletMonkey_Idle")
        self.images = [] # Make list with all the animated images

    def render(self, display):
        #pygame.draw.rect(display, (255, 0, 0), self.rect, 50)
        self.image.render(display, self.rect.x, self.rect.y)