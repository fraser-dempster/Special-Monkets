import pygame
import math
import image_loader
import config
import os
import mapobject2

class maploader2(object):
		def __init__(self, filepath):
			self.path = filepath
			self.maplist = []

			self.referenceList = []
			self.preLoadImages("./images/ArenaTiles/")
			self.loadMapFromFile("testmap1.txt")
			self.loadMapFromFile("testmap1_trees.txt")

		def preLoadImages(self, path):
			for file in os.listdiimport pygame
import math
import image_loader
import config
import os
import mapobject2

class maploader2(object):
		def __init__(self, path1, path2):
			self.path1 = path1
			self.path2 = path2
			self.maplist = []

			self.referenceList = []
			self.preLoadImages("./images/ArenaTiles/")
			self.loadMapFromFile(path1)
			self.loadMapFromFile(path2)

		def preLoadImages(self, path):
			for file in os.listdir(path):
				self.referenceList.append(pygame.image.load(f"{path}\\{file}"))

		def loadMapFromFile(self, path):
			with open(path, "r") as f:
				file_data = f.readlines()
			j = 0
			for data in file_data:
				tempList = []
				i = 0
				for char in data:
					if char != "\n":
						tmp = mapobject2.mapobject2(i, j, False)
						tmp.image = self.referenceList[ord(char) - ord('a')]
					#	if (char == ""):
						if (char == 'g'):
							tmp.bridge = True
						elif (char in 'qrstuvwxyz'):
							tmp.collision = True
						tmp.image = pygame.transform.scale(tmp.image, (config.TILEXSIZE, config.TILEYSIZE))
						tempList.append(tmp)
						i += 32
				j += 32
			#	for data in tempList:
			#		if data.image == 
				self.maplist.append(tempList)

r(path):
				self.referenceList.append(pygame.image.load(f"{path}\\{file}"))

		def loadMapFromFile(self, path):
			with open(path, "r") as f:
				file_data = f.readlines()
			j = 0
			for data in file_data:
				tempList = []
				i = 0
				for char in data:
					if char != "\n":
						tmp = mapobject2.mapobject2(i, j, False)
						tmp.image = self.referenceList[ord(char) - ord('a')]
					#	if (char == ""):
						if (char == 'g'):
							tmp.bridge = True

						tmp.image = pygame.transform.scale(tmp.image, (config.TILEXSIZE, config.TILEYSIZE))
						tempList.append(tmp)
						i += 32
				j += 32
			#	for data in tempList:
			#		if data.image == 
				self.maplist.append(tempList)

