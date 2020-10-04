import pygame
import config

class mapObject:

	def __init__(self, x, y, typeObject, width=config.DEFAULT_IMAGE_SIZEX, height=config.DEFAULT_IMAGE_SIZEY):
		self.x, self.y = x, y
		self.width, self.height = width, height
		
		self.loadImage(typeObject)

	def loadImage(self, typeObject):
		if typeObject == "tree":
			self.image = pygame.image.load("images\\ArenaTiles\\Tree_32x48-1.png")
		else:
			self.image = ""
		self.image = pygame.image.transform(self.image, [self.width, self.height])

	def checkCollision(self, x, y):
		if x < self.x+self.width and x > self.width and y > self.y and y < self.y+self.height:
			return True

	def update(self, x, y):
		pass

	def render(self, display):
		display.blit(self.image, [self.x, self.y, self.width, self.height])
