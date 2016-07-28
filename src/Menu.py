import pygame
import Animation
from pygame.locals import *
import spritesheet
import Play
import Options

BLACK = (0,0,0)

class Menu():
	def __init__(self, window):
		self.window = window

		pygame.mixer.music.load('../resources/musics/gameover.wav')
		pygame.mixer.music.stop()
		pygame.mixer.music.play(-1, 0.0)

		a = Animation.Animation(window, "../resources/ui/menu.png", 2)
		a.fadein()
		a.update(2000)
		loop = True

		play_ = spritesheet.spritesheet("../resources/ui/play.png")
		options_ = spritesheet.spritesheet("../resources/ui/options.png")
		exit_ = spritesheet.spritesheet("../resources/ui/exit.png")

		self.play = play_.image_at((0, 0, 200, 120))
		self.options = options_.image_at((0, 0, 200, 120))
		self.exit = exit_.image_at((0, 0, 200, 120))

		self.display()

		while loop:
			for event in pygame.event.get():
				if event.type == MOUSEMOTION:
					if event.pos[0] < 600 + 200 and event.pos[0] > 600 and event.pos[1] < 190 and event.pos[1] > 70:
						self.play = play_.image_at((200, 0, 200, 120))
					else:
						self.play = play_.image_at((0, 0, 200, 120))

					if event.pos[0] < 600 + 200 and event.pos[0] > 600 and event.pos[1] < 340 and event.pos[1] > 220:
						self.options = options_.image_at((200, 0, 200, 120))
					else:
						self.options = options_.image_at((0, 0, 200, 120))


					if event.pos[0] < 600 + 200 and event.pos[0] > 600 and event.pos[1] < 490 and event.pos[1] > 370:
						self.exit = exit_.image_at((200, 0, 200, 120))
					else:
						self.exit = exit_.image_at((0, 0, 200, 120))

					self.display()

				if event.type == MOUSEBUTTONDOWN and event.button == 1:
					if event.pos[0] < 600 + 200 and event.pos[0] > 600 and event.pos[1] < 190 and event.pos[1] > 70:
						a.fadeout()
						pygame.mixer.music.stop()
						self.playGame()

					if event.pos[0] < 600 + 200 and event.pos[0] > 600 and event.pos[1] < 340 and event.pos[1] > 220:
						a.fadeout()
						pygame.mixer.music.stop()
						self.openOptions()
						tmp = pygame.image.load("../resources/ui/menu.png").convert()
						self.window.blit(tmp, (0,0))
						self.display()

					if event.pos[0] < 600 + 200 and event.pos[0] > 600 and event.pos[1] < 490 and event.pos[1] > 370:
						a.fadeout()
						pygame.mixer.music.stop()
						exit()
				
	def playGame(self):
		p = Play.Play(self.window)	

	def openOptions(self):
		o = Options.Options(self.window)

	def display(self):
		self.play.set_colorkey(BLACK)
		self.exit.set_colorkey(BLACK)
		self.window.blit(self.play, (600, 70))
		self.window.blit(self.options,(600, 220))
		self.window.blit(self.exit, (600, 370))
		pygame.display.update()
		