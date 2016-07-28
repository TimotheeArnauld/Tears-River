import pygame
import spritesheet
from PIL import Image
from threading import Thread
import os
import GameVar

class Direction():
	RIGHT = 0
	DOWN = 2
	UP = 3
	LEFT = 4
	STAY = 5

class Test(Thread):
	def __init__(self, sprite, direction, static):
		super().__init__()
		self.sprite = sprite
		self.static = static
		self.direction = direction

	def run(self):
		self.sprite.setDirection(self.direction)
		if self.static == False:
			self.sprite.animation()
		else:
			self.sprite.animationstatic()

class SpriteAnimation():
	col = 4
	x = 0
	y = 0
	row = col = 4
	step = 4
	update_delay = 2
	last_update = pygame.time.get_ticks()
	tmp = 0

	def __init__(self, window, map, resource, posx, posy, row, col, static=False):
		self.window = window
		self.isVisible = True
		self.ss = spritesheet.spritesheet(resource)
		self.map = map
		self.posx = posx
		self.posy = posy
		self.row = row
		self.col = col
		self.x_offset = self.ss.getXOffset(col)
		self.y_offset = self.ss.getYOffset(row)

		self.backgroundtmp = pygame.image.load(map.getBackgroundMap()).convert()
		self.masktmp = pygame.image.load(os.path.join('../resources/ui/', "mask_2.png")).convert_alpha()
		self.sprite = self.ss.image_at((0, 0, self.x_offset, self.y_offset))
		self.background = self.background_at((self.posx, self.posy, self.x_offset, self.y_offset))

		if static == False:
			self.display()

	def updatestatic(self):
		last_update = pygame.time.get_ticks()
		now = last_update
		update_delay = 100

		while now - last_update < update_delay:
			now = pygame.time.get_ticks()

		self.x += self.x_offset
		if self.x == self.x_offset * self.col:
			self.x = 0

	def update(self):
		last_update = pygame.time.get_ticks()
		now = last_update

		while now - last_update < self.update_delay:
			now = pygame.time.get_ticks()

		while now - self.last_update >= self.update_delay:
			self.last_update = now
		
		self.x += self.x_offset
		if self.x == self.x_offset * self.col:
			self.x = 0

	def setDirection(self, direction):
		if  direction == Direction.RIGHT:
			self.y = 2 * self.y_offset
			self.direction = Direction.RIGHT
		elif direction == Direction.LEFT:
			self.y = 1 * self.y_offset
			self.direction = Direction.LEFT
		elif direction == Direction.UP:
			self.y = 3 * self.y_offset
			self.direction = Direction.UP
		elif direction == Direction.DOWN:
			self.y = 0 * self.y_offset
			self.direction = Direction.DOWN

	def clear(self):
		self.background = self.background_at((self.posx, self.posy, self.x_offset, self.y_offset))
		self.window.blit(self.background,(self.posx, self.posy))

	def move(self):
		if self.direction == Direction.RIGHT:
			self.posx += self.step
		elif self.direction == Direction.LEFT:
			self.posx -= self.step
		elif self.direction == Direction.UP:
			self.posy -= self.step
		elif self.direction == Direction.DOWN:
			self.posy += self.step

	def animation(self):
		for i in range(0, self.col):
			self.clear()
			self.tmp += 1
			if self.tmp % 10 == 0:
				self.update()
				self.sprite = self.ss.image_at((self.x, self.y, self.x_offset, self.y_offset))

			self.move()
			self.scroll()
			self.display()

	def animationstatic(self):
		for i in range(0, self.col):
			self.clear()
			self.updatestatic()
			self.sprite = self.ss.image_at((self.x, self.y, self.x_offset, self.y_offset))
			self.display()
			self.clear()

		self.clear()
		self.setVisible(False)
		self.display()

	def display(self):
		self.window.blit(self.map.background,[0,0],[GameVar.scroll_x,GameVar.scroll_y,GameVar.screen_width,GameVar.screen_height])

		self.window.blit(self.masktmp,(0,0))

		self.map.update_map_items()

		if self.isVisible == True:
			self.window.blit(self.sprite, [self.posx - GameVar.scroll_x, self.posy - GameVar.scroll_y, 32, 48])

		self.window.blit(self.map.playerLife(), (0, 0))
		
		pygame.display.flip()

	def setVisible(self, visible):
		self.isVisible = visible

	def background_at(self, rectangle):
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert()
		image.blit(self.backgroundtmp, (0, 0), rect)
		return image

	def elipse_at(self, rectangle):
		image = self.masktmp.subsurface([self.posx - GameVar.scroll_x, self.posy - GameVar.scroll_y, 32, 48])
		return image

	def launchmove(self, direction, static = False):
		test = Test(self, direction, static)
		test.start()
		test.join()

	def getX(self):
		return self.posx

	def getY(self):
		return self.posy

	def setX(self, x):
		self.posx = x

	def setY(self, y):
		self.posy = y

	def getXOffset(self):
		return self.x_offset

	def getYOffset(self):
		return self.y_offset

	def scroll(self):    
		if self.posx < 0:
			self.posx = 0
        
		elif self.posx > GameVar.map_width - GameVar.player_width:
			self.posx = GameVar.map_width - GameVar.player_width  

		if self.posx <= GameVar.screen_width / 2:
			GameVar.scroll_x = 0
        
		elif self.posx > GameVar.screen_width / 2:
			GameVar.scroll_x = self.posx - GameVar.screen_width / 2
                
			if GameVar.scroll_x > GameVar.map_width - GameVar.screen_width:
				GameVar.scroll_x = GameVar.map_width - GameVar.screen_width

		if self.posy < 0:
			self.posy = 0
        
		elif self.posy > GameVar.map_height - GameVar.player_height:
			self.posy = GameVar.map_height - GameVar.player_height  

		if self.posy <= GameVar.screen_height / 2:
			GameVar.scroll_y = 0
        
		elif self.posy > GameVar.screen_height / 2:
			GameVar.scroll_y = self.posy - GameVar.screen_height / 2
                
			if GameVar.scroll_y > GameVar.map_height - GameVar.screen_height:
				GameVar.scroll_y = GameVar.map_height - GameVar.screen_height
        

