import pygame
from pygame.locals import *
import UI
import spritesheet

class Lifes():
	def __init__(self, window, lifes):
		self.window = window
		self.lifes = lifes
		self.template = spritesheet.spritesheet("ui/lifes.png")
		self.image = self.template.image_at((0, 0, 200, 100))

	def update(self, lifes):
		self.image = self.template.image_at((lifes * 200, 0, 200, 100))
		return self.image

