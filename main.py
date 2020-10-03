import pygame
import threading
import os
import map_object
import enemy
import Player
import bullet
import image_loader

pygame.init()

WHITE = 255,255,255
BLACK = 0,0,0

class Game:

	def __init__(self, width, height):
		self.height = height
		self.width = width

		self.initScreen() # Initialise screen settings
		self.initVars()
		self.run()

	def initScreen(self):
		self.gameScreen = pygame.display.set_mode([self.width, self.height]) # Set width and height
		pygame.display.set_caption("Monkey Mullets")
		icon = pygame.image.load("images\\MulletMonkeyIcon.PNG")
		pygame.display.set_icon(icon)

	def initVars(self):
		self.clock = pygame.time.Clock()
		self.running = True
		self.player = Player.Player(500, 500)

		self.mapObjects = []
		self.enemies = []
		self.bullets = []

		self.level = 1

		self.lastpressedkey = 0

		
		#self.enemies.append(enemy.enemyObject(0, 0, 30))

	def run(self):
		
		while self.running:
			self.gameScreen.fill(WHITE) #Reset game screen

			self.update()
			self.render()

			self.clock.tick(60) # Force game to 60 FPS

	def going_diagonal(self, keys):
		return (keys[pygame.K_w] + keys[pygame.K_s] + keys[pygame.K_a] + keys[pygame.K_d]) > 1

	def update(self):

		# Quit game when needed
		x, y = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.bullets.append(bullet.bullet(self.player.rect.x, self.player.rect.y, x, y))

		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			if (self.lastpressedkey != 1 and not self.going_diagonal(keys)):
				self.lastpressedkey = 1
				self.player.image = image_loader.AnimatedImage("MulletMonkey_MoveUp")
			self.player.rect.y -= 5

		if keys[pygame.K_s]:
			if (self.lastpressedkey != 2 and not self.going_diagonal(keys)):
				self.lastpressedkey = 2
				self.player.image = image_loader.AnimatedImage("MulletMonkey_MoveDown")
			self.player.rect.y += 5

		if keys[pygame.K_a]:
			if (self.lastpressedkey != 3 and not self.going_diagonal(keys)):
				self.lastpressedkey = 3
				self.player.image = image_loader.AnimatedImage("MulletMonkey_WalkLeft")
			self.player.rect.x -= 5

		if keys[pygame.K_d]:
			if (self.lastpressedkey != 4 and not self.going_diagonal(keys)):
				self.lastpressedkey = 4
				self.player.image = image_loader.AnimatedImage("MulletMonkey_WalkRight")

			self.player.rect.x += 5 

		for bullet_ in self.bullets:
			if bullet_.lifetime <= 0:
				self.bullets.pop(self.bullets.index(bullet_))
			bullet_.render(self.gameScreen)

		for enemy in self.enemies:
			enemy.move_towards_player(self.player)

	def render(self):

		self.player.render(self.gameScreen)

		for enemy in self.enemies:
			enemy.draw(self.gameScreen)

		pygame.display.update()

def main():
	game = Game(1280,720)

if __name__ == "__main__":
	main()