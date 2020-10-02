import pygame

class Enemy:

	def __init__(self, x, y):
		self.x, self.y = x, y

		self.initVars()

	def initVars(self):
		self.damage = 0
		self.speed = 0
		self.image = None

	def attack(self):
		pass

	def update(self):
		pass

	def render(self, gameDisplay):
		gameDisplay.blit(self.image)