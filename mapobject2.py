import pygame
import math
import image_loader
import config

class mapobject2(object):
    def __init__(self, x, y, collision):
      self.xsize = config.TILEXSIZE
      self.ysize = config.TILEYSIZE
      self.x = x
      self.y = y
      self.collision = collision
      self.rect = pygame.Rect(x, y, self.xsize, self.ysize)
     
    def update(self):
      pass

    def render(self, display):
      display.blit(self.image, [self.x, self.y])

