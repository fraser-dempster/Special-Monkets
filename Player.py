import pygame
import math

class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 10, 10)
        self.image = pygame.image.load("images\\MulletMonkey_Idle\\sprite_0.png")
        self.image = pygame.transform.scale(self.image, (48, 72))

    def render(self, display):
        #pygame.draw.rect(display, (255, 0, 0), self.rect, 50)
        display.blit(self.image, [self.rect.x-24, self.rect.y-36, 48,72])