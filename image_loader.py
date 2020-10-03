import pygame

class ImageLoader:

	def __init__(self):
		self.imageList = []

	def load_image(self, path):
		return pygame.image.load("images\\", path)