import pygame
import threading

pygame.init()

class Game:

	def __init__(self, width, height):
		self.height = height
		self.width = width

		self.clock = pygame.time.Clock(60)
		self.running = True
		
		self.initScreen()

	def initScreen(self):
		self.gameScreen = pygame.display.set_mode([self.width, self.height])#
		pygame.gameScreen.set_caption("Monkey Mullets")

	def run(self):
		
		while self.running:


	def update(self):
		pass

	def render(self):
		pass

def main():
	pass

if __name__ == "__main__":
	main()