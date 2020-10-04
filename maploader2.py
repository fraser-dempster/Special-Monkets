import pygame
import math
import image_loader
import config
import os

class mapobject2(object):
		def __init__(self, filepath):
			self.path = filepath
			self.maplist = []

			self.referenceList = []

		def preLoadImages(self, path):
			for file in os.listdir(path):
				self.referenceList.append(pygame.image.load(f"{path}\\{file}"))

		def loadMapFromFile(self, path):
			with open(path, "r") as f:
				file_data = f.readlines()
			for data in file_data:
				tempList = []
				for char in data.split(data):
					if char:
						tempList.append(self.referenceList[int(char)])
				self.maplist.append(tempList)

