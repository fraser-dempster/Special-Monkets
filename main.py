import pygame
import threading
import map_object
import enemies

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

	def initVars(self):
		self.clock = pygame.time.Clock()
		self.running = True

		self.mapObjects = []
		self.enemies = []
		
		#self.player = Player()

	def run(self):
		
		while self.running:
			self.gameScreen.fill(WHITE) #Reset game screen

			self.update()
			self.render()

			self.clock.tick(60) # Force game to 60 FPS

	def update(self):

		# Quit game when needed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				pygame.quit() 

	def render(self):

		pygame.display.update()

def main():
	game = Game(1280,720)

if __name__ == "__main__":
	main()