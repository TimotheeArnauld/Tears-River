import pygame

class UI():
	def __init__(self, window):
		self.window = window
		self.ui = pygame.image.load("../resources/ui/background.png").convert()
		self.ui.set_colorkey((0,0,0))
		self.window.blit(self.ui, (0,0))

	def update(self):
		self.window.blit(self.ui, (0,0))