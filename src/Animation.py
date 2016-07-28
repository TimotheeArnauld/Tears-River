import pygame

class Animation():
	def __init__(self, window, path, delay):
		self.window = window
		self.background = pygame.image.load(path).convert()
		self.mask = pygame.image.load("../resources/ui/mask.png").convert()
		self.update_delay = delay

	def update(self, update_delay):
		last_update = pygame.time.get_ticks()
		now = last_update

		while now - last_update < update_delay:
			now = pygame.time.get_ticks()

	def fadein(self):
		for i in range(255, 0, -10):
			self.window.blit(self.background,(0,0))
			self.window.blit(self.mask,(0,0))
			self.mask.set_alpha(i)
			pygame.display.update()
			self.update(self.update_delay)


	def fadeout(self):
		for i in range(0, 255, 10):
			self.window.blit(self.background,(0,0))
			self.window.blit(self.mask,(0,0))
			self.mask.set_alpha(i)
			pygame.display.update()
			self.update(self.update_delay)