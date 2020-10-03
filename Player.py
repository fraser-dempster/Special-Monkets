import pygame
import math
import image_loader

class Player(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.rect = pygame.Rect(x, y, 10, 10)
		self.image = image_loader.AnimatedImage("MulletMonkey_Idle")
		self.images = [] # Make list with all the animated images
		self.lastpressedkey = 0


	def render(self, display):
		#pygame.draw.rect(display, (255, 0, 0), self.rect, 50)
		self.image.render(display, self.rect.x, self.rect.y)

	def update(self):
		self.move()
	
	def isDestroyed(self):
		return False

	def going_diagonal(self, keys):
		return (keys[pygame.K_w] + keys[pygame.K_s] + keys[pygame.K_a] + keys[pygame.K_d]) > 1

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			if (self.lastpressedkey != 1 and not self.going_diagonal(keys)):
				self.lastpressedkey = 1
				self.image = image_loader.AnimatedImage("MulletMonkey_MoveUp")
			self.rect.y -= 5

		if keys[pygame.K_s]:
			if (self.lastpressedkey != 2 and not self.going_diagonal(keys)):
				self.lastpressedkey = 2
				self.image = image_loader.AnimatedImage("MulletMonkey_MoveDown")
			self.rect.y += 5

		if keys[pygame.K_a]:
			if (self.lastpressedkey != 3 and not self.going_diagonal(keys)):
				self.lastpressedkey = 3
				self.image = image_loader.AnimatedImage("MulletMonkey_WalkLeft")
			self.rect.x -= 5

		if keys[pygame.K_d]:
			if (self.lastpressedkey != 4 and not self.going_diagonal(keys)):
				self.lastpressedkey = 4
				self.image = image_loader.AnimatedImage("MulletMonkey_WalkRight")

			self.rect.x += 5 