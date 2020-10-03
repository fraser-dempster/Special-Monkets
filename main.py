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
		self.entities = [self.player, enemy.Enemy(200, 200, self.player), enemy.Enemy(400, 400, self.player)]
		self.level = 1

		#self.enemies.append(enemy.enemyObject(0, 0, 30))

	def run(self):
		
		while self.running:
			self.gameScreen.fill(BLACK) #Reset game screen

			self.update()
			self.render()

			self.clock.tick(60) # Force game to 60 FPS


	def update(self):

		# Quit game when needed

		x, y = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.entities.append(bullet.bullet(self.player.rect.x, self.player.rect.y, x, y))

		for entity in self.entities:
			entity.update()
			
		self.entites = [x for x in self.entities if not x.isDestroyed()]	

	def render(self):
		for entity in self.entites:
			entity.render(self.gameScreen)
		pygame.display.update()

def main():
	game = Game(1280,720)

if __name__ == "__main__":
	main()