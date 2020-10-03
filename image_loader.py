import pygame
import os
import config
class AnimatedImage:

	def __init__(self, path, xsize = config.DEFAULT_IMAGE_SIZEX, ysize = config.DEFAULT_IMAGE_SIZEY):
		self.imageList = []
		self.timer = 0
		self.threshold = 30
		self.imageIndex = 0
		self.active = False
		self.xsize = xsize
		self.ysize = ysize

		self.loadAllImages(path)

	def loadAllImages(self, p):
		for path in os.listdir(f"images\\{p}"):
			self.imageList.append(pygame.image.load(f"images\\{p}\\{path}"))
		for i in range(len(self.imageList)):
			self.imageList[i] = pygame.transform.scale(self.imageList[i], (self.xsize, self.ysize))

	def render(self, display, x, y):
		self.timer += 1
		if self.timer == self.threshold and self.imageIndex < len(self.imageList):
			self.imageIndex += 1
			self.timer = 0
		if self.imageIndex == len(self.imageList):
			self.imageIndex = 0
		display.blit(self.imageList[self.imageIndex], [x, y])