import map_object
import enemy
import Player
import bullet
import image_loader
import config
import uibanana

class ui(object):
  def __init__(self, player):
    self.x = config.UI_X
    self.y = config.UI_Y
    self.player = player
    self.banana1 = uibanana.uibanana(config.SCREENX - self.x, self.y)
    self.banana2 = uibanana.uibanana(config.SCREENX - (self.x + config.UIBANANA_XSIZE + config.PADDING), self.y)
    self.banana3 = uibanana.uibanana(config.SCREENX - (self.x + 2 * config.UIBANANA_XSIZE + 2 * config.PADDING), self.y)
    self.bananas = [self.banana1, self.banana2, self.banana3]

  def update(self):
    if self.player.bananas == 3:
      self.bananas[0].available = True
      self.bananas[1].available = True
      self.bananas[2].available = True
    if self.player.bananas == 2:
      self.bananas[0].available = True
      self.bananas[1].available = True
      self.bananas[2].available = False
    if self.player.bananas == 1:
      self.bananas[0].available = True
      self.bananas[1].available = False
      self.bananas[2].available = False
    if self.player.bananas == 0:
      self.bananas[0].available = False
      self.bananas[1].available = False
      self.bananas[2].available = False

  def isDestroyed(self):
    return False

  def render(self, display):
    for banana in self.bananas:
      banana.render(display)


