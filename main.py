import pygame
import threading
import os
import map_object
import enemy
import Player
import bullet
import image_loader
import config

WHITE = 255,255,255
BLACK = 0,0,0

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init() 

class Game:

	def __init__(self, width, height):
		self.height = height
		self.width = width


		self.initScreen() # Initialise screen settings
		self.initVars()
		self.initSounds()
		self.run()

	def initScreen(self):
		self.gameScreen = pygame.display.set_mode([self.width, self.height]) # Set width and height
		pygame.display.set_caption("Monkey Mullets")
		icon = pygame.image.load("images\\MulletMonkeyIcon.PNG")
		pygame.display.set_icon(icon)
		
		pygame.display.set_mode()

	def initVars(self):
		self.clock = pygame.time.Clock()
		self.running = True
		self.player = Player.Player(500, 500)
		self.entities = [self.player, enemy.Enemy(200, 200, self.player), enemy.Enemy(400, 400, self.player)]
		self.level = 1
	
	def initSounds(self):
		self.music = {
			'robot': pygame.mixer.Sound("./sounds/music/robot monkey invasion.ogg"), 
			'spooky': pygame.mixer.Sound("./sounds/music/battle music spooky.ogg"),
			'normal': pygame.mixer.Sound("./sounds/music/battle music.ogg"),
			'lofi': pygame.mixer.Sound("./sounds/music/lofi v3.ogg")
		}

		for m in self.music:
			self.music[m].set_volume(0.5)
		self.music['robot'].play(-1)


		
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

			# Check for bullet-enemy collision

			if isinstance(entity, bullet.bullet):
				for collision_entity in self.entities:
					if isinstance(collision_entity, enemy.Enemy) and entity.rect.colliderect(collision_entity.rect):
						entity.hascollided = True
						collision_entity.hascollided = True
						
		


		self.entites = [x for x in self.entities if not x.isDestroyed()]	

	def render(self):
		for entity in self.entites:
			entity.render(self.gameScreen)
		pygame.display.update()

def main():
	game = Game(1280,720)

if __name__ == "__main__":
	main()