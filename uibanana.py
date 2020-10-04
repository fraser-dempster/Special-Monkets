import config
import image_loader
import pygame

class uibanana(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.xsize = config.UIBANANA_XSIZE
    self.ysize = config.UIBANANA_YSIZE
    self.enabled = image_loader.AnimatedImage("BananaUIAvailable", xsize = self.xsize, ysize = self.ysize)
    self.disabled = image_loader.AnimatedImage("BananaUIUnavailable", xsize = self.xsize, ysize = self.ysize)

    self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
    self.available = True

  def swap(self):
    self.available = not self.available

  def update(self):
    pass

  def render(self, display):
    if self.available:
      self.enabled.render(display, self.rect.x, self.rect.y)
    else:
      self.disabled.render(display, self.rect.x, self.rect.y)



    
