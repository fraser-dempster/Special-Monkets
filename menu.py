import config
import pygame

class menu(object):
  def __init__(self, display):
    self.display = display
    self.start = False
    self.display.blit(pygame.image.load("./images/TitleScreen/Title_screen.png"), [config.MENUXOFFSET, config.MENUYOFFSET])
 
