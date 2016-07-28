import pygame
import Animation
import spritesheet
from pygame.locals import *

BLACK = (0,0,0)

class Options():
	def __init__(self, window):
		self.window = window
		a = Animation.Animation(window, "../resources/ui/options_menu.png", 2)
		a.fadein()
		a.update(2000)
		loop = True

		checkbox_ = spritesheet.spritesheet("../resources/ui/checkbox.png")

		self.checkbox = checkbox_.image_at((0, 0, 100, 100))

		self.display()

		while loop:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						loop = False
						a.fadeout()
				if event.type == MOUSEBUTTONDOWN and event.button == 1:
					if event.pos[0] < 600 + 200 and event.pos[0] > 600 and event.pos[1] < 190 and event.pos[1] > 70:
						a.fadeout()
						pygame.mixer.music.stop()
						self.checkbox = checkbox_.image_at(100,0,100,100)

	def display(self):
		self.checkbox.set_colorkey(BLACK)
		self.window.blit(self.checkbox, (600, 70))
		pygame.display.update()