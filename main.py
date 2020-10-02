import pygame
import threading

pygame.init()

WHITE = 255,255,255
BLACK = 0,0,0

class Game:

	def __init__(self, width, height):
		self.height = height
		self.width = width

		self.clock = pygame.time.Clock()
		self.running = True
		
		self.initScreen()
		self.run()

	def initScreen(self):
		self.gameScreen = pygame.display.set_mode([self.width, self.height])#
		pygame.display.set_caption("Monkey Mullets")

	def run(self):
		
		while self.running:
			self.gameScreen.fill(WHITE) #Reset game screen

			self.update()
			self.render()

			self.clock.tick(60)

	def update(self):
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				pygame.quit()

	def render(self):

		pygame.display.update()

def main():
	game = Game(800,800)

if __name__ == "__main__":
	main()