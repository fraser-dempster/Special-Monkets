import pygame
import math
import image_loader
import config

class Player(object):
	def __init__(self, x, y):
		self.speed= config.PLAYER_MOVEMENT_SPEED
		self.xsize = config.PLAYER_XSIZE
		self.ysize = config.PLAYER_YSIZE
		self.rect = pygame.Rect(x, y, self.xsize, self.ysize)

		self.hascollided = False
		self.bananas = 3
		self.initialiseVars()

	def initialiseVars(self):
		self.image = image_loader.AnimatedImage("MulletMonkey_Idle", self.xsize, self.ysize)
		self.images = [] # Make list with all the animated images
		self.lastpressedkey = 0

		imageFiles = ["MulletMonkey_Idle", "MulletMonkey_MoveDown", "MulletMonkey_MoveUp", "MulletMonkey_WalkLeft", "MulletMonkey_WalkRight"]

		for name in imageFiles:
			self.images.append(image_loader.AnimatedImage(name, xsize = self.xsize, ysize = self.ysize))

	def render(self, display):
		self.image.render(display, self.rect.x, self.rect.y)

	def update(self):
		self.move()
	
	def isDestroyed(self):
		return self.hascollided

	def going_diagonal(self, keys):
		return (keys[pygame.K_w] + keys[pygame.K_s] + keys[pygame.K_a] + keys[pygame.K_d]) > 1

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			if (self.lastpressedkey != 1 and not self.going_diagonal(keys)):
				self.lastpressedkey = 1
				self.image = self.images[2]
			self.rect.y -= self.speed

		if keys[pygame.K_s]:
			if (self.lastpressedkey != 2 and not self.going_diagonal(keys)):
				self.lastpressedkey = 2
				self.image = self.images[1]
			self.rect.y += self.speed

		if keys[pygame.K_a]:
			if (self.lastpressedkey != 3 and not self.going_diagonal(keys)):
				self.lastpressedkey = 3
				self.image = self.images[3]
			self.rect.x -= self.speed

		if keys[pygame.K_d]:
			if (self.lastpressedkey != 4 and not self.going_diagonal(keys)):
				self.lastpressedkey = 4
				self.image = self.images[4]
			self.rect.x += self.speed

		if (not keys[pygame.K_w]) and (not keys[pygame.K_s]) and (not keys[pygame.K_d]) and (not keys[pygame.K_a]):
			self.image = self.images[0]
			self.lastpressedkey = 0