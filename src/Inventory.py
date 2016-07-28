import pygame
from pygame.locals import *
import Animation
import GameVar

class Inventory():
	def __init__(self, window):
		self.window = window
		a = Animation.Animation(window, "../resources/ui/inventory.png", 1)

		self.grimoire = pygame.image.load("../resources/ui/grimoire.png")
		self.item = pygame.image.load("../resources/ui/heart_ui.png")

		self.myfont = pygame.font.SysFont("arial", 60)

		a.fadein()

		self.update()

		loop = True

		while loop:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						loop = False
						a.fadeout()
				if event.type == MOUSEBUTTONDOWN and event.button == 1:
					if event.pos[0] <  + (518 + 253) and event.pos[0] > 518 and event.pos[1] < (232 + 85) and event.pos[1] > 232:
						if GameVar.life < 3 and GameVar.item > 0:
							GameVar.life += 1
							GameVar.item -= 1
							self.update()
	
	def update(self):
		background = pygame.image.load("../resources/ui/inventory.png")
		self.window.blit(background, (0, 0))

		if GameVar.weapon == True:
			self.window.blit(self.grimoire, (115, 232))

		label = self.myfont.render("x" + str(GameVar.item), 1, (0,0,0))
		
		if GameVar.item > 0:
			self.window.blit(self.item, (518, 232))
			self.window.blit(label, (545, 250))

		pygame.display.flip()

