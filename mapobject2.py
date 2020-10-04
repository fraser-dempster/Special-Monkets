import pygame
import math
import image_loader
import config

class mapobject2(object):
    def __init__(self, x, y, collision, type):
      self.xsize = config.TILEXSIZE
      self.ysize = config.TILEYSIZE
      self.x = x
      self.y = y
      self.collision = collision
      self.rect = pygame.Rect(x, y, self.xsize, self.ysize)
      self.image = pygame.image.load(self.type2path(1))
      self.image = pygame.transform.scale(self.image, (self.xsize, self.ysize))
      print(self.xsize, self.ysize)
     
    def type2path(self, type):
      if (type == 1):
        return ("./images/ArenaTiles/1.png")
      
    def update(self):
      pass

    def render(self, display):
      display.blit(self.image, [self.x, self.y])

