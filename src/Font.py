import pygame
from pygame.locals import *
import UI

class Font():
	def __init__(self, window, map, text, character):
		self.window = window
		self.map = map
		self.text = text
		myfont = pygame.font.SysFont("arial", 15)

		ui = UI.UI(window)
		label = myfont.render(text, 1, (255,255,0))

		if character == 0:
			self.hero= pygame.image.load("../resources/ui/hero.png").convert_alpha()
			self.hero.set_colorkey((0,0,0))
			self.window.blit(self.hero, (0,333))
		else:
			self.pnj = pygame.image.load("../resources/ui/pnj2.jpg").convert_alpha()
			self.pnj.set_colorkey((0,0,0))
			self.window.blit(self.pnj, (700,333))

		self.window.blit(label, (165, 430))
		pygame.display.flip()
		loop = True

		while(loop):
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_RETURN:
						loop = 0

		self.clear()

	def clear(self):
		pygame.draw.rect(self.window, (0, 0, 0), (155, 420, 490, 60))
		self.map.refresh()
		pygame.display.flip()
