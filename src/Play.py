import pygame
from pygame.locals import *
import Player
import MapStructure
import Splashscreen
import intro

class Play():
	def __init__(self, window):
		loop = 1

		"""pygame.mixer.music.load('../resources/musics/game.wav')
		pygame.mixer.music.play(-1, 0.0)

		i = intro.intro(window)"""

		m = MapStructure.MapStructure(window)

		player = Player.Player(window, m)

		pygame.key.set_repeat (1, 1)
		pygame.display.flip()

		while loop:
			for event in pygame.event.get():
				player.moveplayer(event)
				if event.type == QUIT:
					exit()

		"""pygame.mixer.music.stop()"""