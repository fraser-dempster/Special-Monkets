import pygame
import os

class AnimatedImage:

	def __init__(self, path, width, height):
		self.imageList = []
		self.timer = 0
		self.threshold = 30
		self.imageIndex = 0
		self.active = False

		self.loadAllImages(path, width, height)

	def loadAllImages(self, p, width, height):
		for path in os.listdir(f"images\\{p}"):
			self.imageList.append(pygame.image.load(f"images\\{p}\\{path}"))
		for i in range(len(self.imageList)):
			self.imageList[i] = pygame.transform.scale(self.imageList[i], (width, height))

	def render(self, display, x, y):
		self.timer += 1;
		if self.timer == self.threshold and self.imageIndex < len(self.imageList):
			self.imageIndex += 1
			self.timer = 0
		if self.imageIndex == len(self.imageList):
			self.imageIndex = 0
		display.blit(self.imageList[self.imageIndex], [x, y])
