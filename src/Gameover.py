import pygame
import Animation
from pygame.locals import *
import spritesheet
import Play
import Menu

BLACK = (0,0,0)

class Gameover():
	def __init__(self, window):
		self.window = window

		pygame.mixer.music.load('../resources/musics/gameover.wav')
		pygame.mixer.music.stop()
		pygame.mixer.music.play(-1, 0.0)

		a = Animation.Animation(window, "../resources/ui/gameover.png", 2)
		a.fadein()
		a.update(2000)
		loop = True

		yes_ = spritesheet.spritesheet("../resources/ui/yes.png")
		no_ = spritesheet.spritesheet("../resources/ui/no.png")

		self.yes = yes_.image_at((0, 0, 200, 100))
		self.no = no_.image_at((0, 0, 200, 100))

		self.display()

		while loop:
			for event in pygame.event.get():
				if event.type == MOUSEMOTION:
					if event.pos[0] < 150 + 200 and event.pos[0] > 150 and event.pos[1] < 470 and event.pos[1] > 370:
						self.yes = yes_.image_at((200, 0, 200, 100))
					else:
						self.yes = yes_.image_at((0, 0, 200, 100))

					if event.pos[0] < 550 + 200 and event.pos[0] > 550 and event.pos[1] < 470 and event.pos[1] > 370:
						self.no = no_.image_at((200, 0, 200, 100))
					else:
						self.no = no_.image_at((0, 0, 200, 100))

					self.display()

				if event.type == MOUSEBUTTONDOWN and event.button == 1:
					if event.pos[0] < 150 + 200 and event.pos[0] > 150 and event.pos[1] < 470 and event.pos[1] > 370:
						a.fadeout()
						pygame.mixer.music.stop()
						self.play()

					if event.pos[0] < 550 + 200 and event.pos[0] > 550 and event.pos[1] < 470 and event.pos[1] > 370:
						a.fadeout()
						pygame.mixer.music.stop()
						menu = Menu.Menu(self.window)
				
	def play(self):
		p = Play.Play(self.window)	

	def display(self):
		self.yes.set_colorkey(BLACK)
		self.no.set_colorkey(BLACK)
		self.window.blit(self.yes, (150, 370))
		self.window.blit(self.no, (550, 370))
		pygame.display.update()
		