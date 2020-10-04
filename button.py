import config
import pygame

class button(object):
  def __init__(self, display):
    self.display = display
    self.start = False
    self.xsize = config.STARTXSIZE
    self.ysize = config.STARTYSIZE
    self.image = pygame.image.load("./images/TitleScreen/start.png")
    self.image = pygame.transform.scale(self.image, (self.xsize, self.ysize))
    self.rect = pygame.Rect(config.STARTX, config.STARTY, self.xsize, self.ysize)
    self.display.blit(self.image, [config.STARTX, config.STARTY])
