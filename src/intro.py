import pygame
import Animation

class intro():
	def __init__(self, window):
		self.window = window
		a = Animation.Animation(window, "../resources/ui/intro.png", 5)
		a.fadein()
		a.update(7000)
		a.fadeout()