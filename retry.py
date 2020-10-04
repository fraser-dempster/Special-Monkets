import config
import pygame

class retry(object):
  def __init__(self, display):
    self.display = display
    self.start = False
    self.xsize = config.RETRYXSIZE
    self.ysize = config.RETRYYSIZE
    self.image = pygame.image.load("./images/retry.png")
    self.image = pygame.transform.scale(self.image, (self.xsize, self.ysize))
    self.rect = pygame.Rect(config.RETRYX, config.RETRYY, self.xsize, self.ysize)
    self.display.blit(self.image, [config.RETRYX, config.RETRYY])
