import pygame
import Animation

class Splashscreen():
	def __init__(self, window):
		self.window = window

		a = Animation.Animation(window, "../resources/ui/splashscreen.png", 5)

		pygame.mixer.music.load('../resources/musics/jingle.ogg')

		pygame.mixer.music.play(1, 1.0)

		a.fadein()
		a.update(10000)
		a.fadeout()
		
		pygame.mixer.music.fadeout(1000)