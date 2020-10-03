import pygame
import os

class MapLoader:

	def __init__(self):
		self.referenceList = []
		self.imageList = []

		self.mapList = []

		self.preLoadImages("images\\ArenaTiles")

	def preLoadImages(self, path):
		for file in os.listdir(path):
			self.imageList.append(pygame.image.load(f"{path}\\{file}"))
			self.referenceList.append(file)

	def loadMapFromFile(self, path):
		with open(path, "r") as f:
			file_data = f.readlines()
		for data in file_data:
			tempList = []
			for char in data.split(data):
				if char != "\\" or char != "n":
					tempList.append(int(char))
			self.imageList.append(tempList)

	def loadMap(self):
		

	def render(self, display):
		i, j = 0, 0
		for subList in self.mapList:
			for image in subList:
				display.blit(image, [j*32, i*32, 32, 32])
				j += 1
			i += 1