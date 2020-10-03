import pygame
import math
import image_loader
import config

class bullet(object):
    def __init__(self, x, y, mouse_x, mouse_y):
        self.lifetime = config.BULLET_LIFETIME
        self.speed = config.BULLET_SPEED
        self.xsize = config.BULLET_XSIZE
        self.ysize = config.BULLET_YSIZE

        self.angle = math.atan2(mouse_y-y, mouse_x-x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.image = image_loader.AnimatedImage("ThrowingBanana", xsize = self.xsize, ysize = self.ysize)
        self.rect = self.rect = pygame.Rect(x, y, self.xsize, self.ysize)

        self.hascollided = False

    def render(self, display):
        self.image.render(display, self.rect.x, self.rect.y)
    
    def update(self):
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel

        self.lifetime -= 1
    
    def isDestroyed(self):
        return self.lifetime <= 0 or self.hascollided
