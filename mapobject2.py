import pygame
import math
import image_loader
import config

class mapobject2(object):
    def __init__(self, x, y, collision, bridge = False):
      self.xsize = config.TILEXSIZE
      self.ysize = config.TILEYSIZE
      self.x = x
      self.y = y
      self.bridge = bridge
      self.collision = collision
      self.rect = pygame.Rect(x, y, self.xsize, self.ysize)
      self.refresh = 1

    def update(self):
      pass

    def render(self, display):
      if self.refresh:
        display.blit(self.image, [self.x, self.y])
        self.refresh -= 1

