import pygame
import threading
import os
import map_object
import enemy
import Player
import bullet
import image_loader
import config
import ui

WHITE = 255,255,255
BLACK = 0,0,0


class Game:

	def __init__(self, width, height):
		self.height = height
		self.width = width
		self.running = False
		self.initScreen() # Initialise screen settings
		self.initSounds()

		self.runMenu()

		self.initVars()
		self.run()

		
	def runMenu(self):
		pass
		

	def initScreen(self):
		self.gameScreen = pygame.display.set_mode([self.width, self.height]) # Set width and height
		pygame.display.set_caption("Monkey Mullets")
		icon = pygame.image.load("images\\MulletMonkeyIcon.PNG")
		pygame.display.set_icon(icon)
		pygame.display.set_mode()

	def initVars(self):
		self.clock = pygame.time.Clock()
		self.player = Player.Player(500, 500)
		self.entities = [self.player, enemy.Enemy(200, 200, self.player), enemy.Enemy(400, 400, self.player), ui.ui(self.player)]
		self.level = 1
		self.running = True
	
	def initSounds(self):
		self.music = {
			'robot': pygame.mixer.Sound("./sounds/music/robot monkey invasion.ogg"), 
			'spooky': pygame.mixer.Sound("./sounds/music/battle music spooky.ogg"),
			'normal': pygame.mixer.Sound("./sounds/music/battle music.ogg"),
			'lofi': pygame.mixer.Sound("./sounds/music/lofi v3.ogg")
		}

		self.sounds = {
			'defeat': pygame.mixer.Sound("./sounds/sfx/defeat.ogg"),
			'death' : pygame.mixer.Sound("./sounds/sfx/death.ogg"),
			'gameover' : pygame.mixer.Sound("./sounds/sfx/gameover.ogg"),
			'impact' : pygame.mixer.Sound("./sounds/sfx/impact.ogg"),
			'stagecomplete' : pygame.mixer.Sound("./sounds/sfx/stagecomplete.ogg")
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
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and self.player.bananas > 0:
					self.player.bananas -= 1
					self.entities.append(bullet.bullet(self.player.rect.x, self.player.rect.y, x, y))

		for entity in self.entities:
			entity.update()

			# Check for bullet-enemy collision

			if isinstance(entity, bullet.bullet):
				for collision_entity in self.entities:
					if isinstance(collision_entity, enemy.Enemy) and entity.isactive and entity.rect.colliderect(collision_entity.rect):
						entity.disable()
						collision_entity.hascollided = True
						self.sounds['impact'].play()
					elif isinstance(collision_entity, Player.Player) and not entity.isactive and entity.rect.colliderect(collision_entity.rect):
						collision_entity.bananas += 1
						entity.hascollided = True

			if isinstance(entity, Player.Player):
				for collision_entity in self.entities:
					if isinstance(collision_entity, enemy.Enemy) and entity.rect.colliderect(collision_entity.rect):
						entity.hascollided = True
						self.sounds['gameover'].play()
						for i in self.music:
							self.music[i].stop()
						


		self.entities = [x for x in self.entities if not x.isDestroyed()]	

			# Check for player-enemy collision

			


	def render(self):
		for entity in self.entities:
			entity.render(self.gameScreen)
		pygame.display.update()

def main():
	pygame.display.set_mode()
	pygame.mixer.pre_init(44100, -16, 2, 512)
	pygame.mixer.init() 
	pygame.init()

	game = Game(config.SCREENX, config.SCREENY)

if __name__ == "__main__":
	main()