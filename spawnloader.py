import pygame
import math
import image_loader
import config
import os
import mapobject2
import ghost
import ui

class spawnloader(object):
		def __init__(self, path, player):
			self.player = player
			self.path = path
			self.enemylist = [self.player, ui.ui(self.player)]
			self.loadMapFromFile(self.path)

		def loadMapFromFile(self, path):
			with open(path, "r") as f:
				file_data = f.readlines()
			j = 0
			for data in file_data:
				i = 0
				for char in data:
					if char != "\n":
						if int(char):
							gh = ghost.ghost(i, j, self.player)
							self.enemylist.append(gh)
					i += 32
							
				j += 32
			#	for data in tempList:
			#		if data.image == 

