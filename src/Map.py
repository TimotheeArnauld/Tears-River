import pygame
from PIL import Image, ImageDraw 
import SpriteAnimation
import Event
from Event import EventData
import Lifes
import os
import Gameover
import GameVar

class Map():
	def __init__(self, window, path):
		self.window = window
		self.path = path
		self.background = pygame.image.load("../resources/maps/fullmap.png").convert()
		self.mask = pygame.image.load(os.path.join('../resources/ui/', "mask_2.png")).convert_alpha()

		self.e = Event.Event(self.path)
		self.Lifes = Lifes.Lifes(self.window, "")

		im = Image.open(self.getCollideMap())
		self.pix = im.load()
		self.d = ImageDraw.Draw(im)

		self.refresh()

	def getCollide(self):
		return self.collide

	def playerLife(self):
		if GameVar.life == 0:
			g = Gameover.Gameover(self.window)
		if GameVar.life > 3:
			GameVar.life = 3
		return self.Lifes.update(GameVar.life)
		

	def getEvent(self, type_, x, y, xoffset, yoffset):
		return self.e.getEvent(type_, x, y, xoffset, yoffset)

	def getText(self, x, y, xoffset, yoffset):
		return self.e.printText(x, y, xoffset, yoffset)

	def getBackgroundMap(self):
		return "../resources/maps/fullmap.png"

	def getCollideMap(self):
		return "../resources/maps/fullcollide.png"

	def testCollide(self, x, y):
		return self.pix[x, y]

	def delete(self, event):
		self.e.deleteEvent(event)
		self.refresh()

	def refresh(self):
		self.items = []

		pnj = self.e.getPNJ()
		for p in pnj:
			self.sprite = SpriteAnimation.SpriteAnimation(self.window, self, "sprites/man.png", p.getX(), p.getY(), 4, 4)
			self.items.append(self.sprite)

		bonus = self.e.getBonus()
		for p in bonus:
			self.sprite = SpriteAnimation.SpriteAnimation(self.window, self, "ui/heart.png", p.getX(), p.getY(), 1, 1)
			self.items.append(self.sprite)
		
		weapon = self.e.getWeapon()
		for p in weapon:
			self.sprite = SpriteAnimation.SpriteAnimation(self.window, self, "ui/book.png", p.getX(), p.getY(), 1, 1)
			self.items.append(self.sprite)

		trap = self.e.getTrap()
		for p in trap:
			self.sprite = SpriteAnimation.SpriteAnimation(self.window, self, "ui/trap.png", p.getX(), p.getY(), 1, 1)
			self.items.append(self.sprite)

	def update_map_items(self):
		for it in self.items:
			self.window.blit(it.sprite, [it.getX() - GameVar.scroll_x, it.getY() - GameVar.scroll_y, 32, 32])

