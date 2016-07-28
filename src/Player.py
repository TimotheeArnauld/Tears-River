import pygame
from pygame.locals import *
import SpriteAnimation
from SpriteAnimation import Direction as Dir
from MapStructure import Direction as mapdir
from Event import EventData
import Font
import MapStructure
import Inventory
import GameVar

class Collide():
	simpleColor  = (255, 0, 0, 255)
	behindColor  = (0, 255, 0, 255)
	endGameColor = (0, 0, 0, 255)
	pnjcolor     = (0, 0, 255, 255)

class Player():
	has_a_weapon = False

	def __init__(self, window, map):
		self.isattacking = False
		self.window = window
		self.map = map
		self.map.getMap().playerLife()
		self.sprite = SpriteAnimation.SpriteAnimation(window, map.getMap(), "sprites/adventurer.png", 0, 0, 4, 4)
		self.actual_direction = Dir.DOWN
		self.attack = SpriteAnimation.SpriteAnimation(self.window, self.map.getMap(), "ui/attack.png", 0, 0, 1, 5, True)

	def moveplayer(self, event):
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				self.isattacking = True
			if event.key == K_DOWN:
				if self.collide(Dir.DOWN) == True:
					self.actual_direction = Dir.DOWN
					self.sprite.launchmove(Dir.DOWN)
			if event.key == K_LEFT:
				if self.collide(Dir.LEFT) == True:
					self.actual_direction = Dir.LEFT
					self.sprite.launchmove(Dir.LEFT)
			if event.key == K_RIGHT:
				if self.collide(Dir.RIGHT) == True:
					self.actual_direction = Dir.RIGHT
					self.sprite.launchmove(Dir.RIGHT)
			if event.key == K_UP:
				if self.collide(Dir.UP) == True:
					self.actual_direction = Dir.UP
					self.sprite.launchmove(Dir.UP)
			if event.key == K_i:
				i = Inventory.Inventory(self.window)
				self.map.getMap().refresh()
				self.map.getMap().playerLife()
				self.sprite.display()
			else:
				return

		if self.isattacking == True:
			if self.has_a_weapon == False:
				f = Font.Font(self.window, self.map.getMap(), "Je ne sais pas me battre...", 0)
				self.isattacking = False
			else:
				if self.actual_direction == Dir.DOWN:
					x = self.sprite.getX() - (self.attack.getXOffset() / 2 - self.sprite.getXOffset() / 2)
					y = self.sprite.getY() + self.sprite.getYOffset()
				elif self.actual_direction == Dir.UP:
					x = self.sprite.getX() - (self.attack.getXOffset() / 2 - self.sprite.getXOffset() / 2)
					y = self.sprite.getY() - self.attack.getYOffset()
				elif self.actual_direction == Dir.LEFT:
					x = self.sprite.getX() - self.attack.getXOffset()
					y = self.sprite.getY() - (self.attack.getYOffset() / 2 - self.sprite.getYOffset() / 2)
				elif self.actual_direction == Dir.RIGHT:
					x = self.sprite.getX() + self.sprite.getXOffset()
					y = self.sprite.getY() - (self.attack.getYOffset() / 2 - self.sprite.getYOffset() / 2)

				self.attack = SpriteAnimation.SpriteAnimation(self.window, self.map.getMap(), "ui/attack.png", x, y, 1, 5, True)
				self.attack.launchmove(Dir.DOWN, True)
				self.map.getMap().playerLife()
				self.sprite.display()
				self.isattacking = False

	def objectDetection(self, direction):
		if direction == Dir.DOWN:
			tmpx = self.sprite.getX()
			tmpy = self.sprite.getY() + 5
		if direction == Dir.UP:
			tmpx = self.sprite.getX()
			tmpy = self.sprite.getY() -  5
		if direction == Dir.LEFT:
			tmpx = self.sprite.getX() - 9
			tmpy = self.sprite.getY()
		if direction == Dir.RIGHT:
			tmpx = self.sprite.getX() + 9
			tmpy = self.sprite.getY()

		"""Detection de PNJ"""
		if self.map.getMap().getEvent(EventData.TYPE, tmpx, tmpy, self.sprite.getXOffset(), self.sprite.getYOffset()) == "pnj":
			text = self.map.getMap().getText(tmpx, tmpy, self.sprite.getXOffset(), self.sprite.getYOffset())
			f = Font.Font(self.window, self.map.getMap(), text, 1)
			self.sprite.display()
			return False

		"""Detection de texte"""
		if self.map.getMap().getEvent(EventData.TYPE, self.sprite.getX(), self.sprite.getY(), self.sprite.getXOffset(), self.sprite.getYOffset()) == "text":
			text = self.map.getMap().getText(self.sprite.getX(), self.sprite.getY(), self.sprite.getXOffset(), self.sprite.getYOffset())
			f = Font.Font(self.window, self.map.getMap(), text, 0)

		"""Detection de la fin du jeu"""
		if self.map.getMap().getEvent(EventData.TYPE, self.sprite.getX(), self.sprite.getY(), self.sprite.getXOffset(), self.sprite.getYOffset()) == "endofgame":
			text = self.map.getMap().getText(self.sprite.getX(), self.sprite.getY(), self.sprite.getXOffset(), self.sprite.getYOffset())
			f = Font.Font(self.window, self.map.getMap(), text, 0)
			exit()

		"""Detection d'un bonus"""
		if self.map.getMap().getEvent(EventData.TYPE, tmpx, tmpy, self.sprite.getXOffset(), self.sprite.getYOffset()) == "bonus":
			text = self.map.getMap().getText(tmpx, tmpy, self.sprite.getXOffset(), self.sprite.getYOffset())
			if text != "none":
				f = Font.Font(self.window, self.map.getMap(), text, 0)
			GameVar.item += 1
			bonus = self.map.getMap().getEvent(EventData.NODE, tmpx, tmpy, self.sprite.getXOffset(), self.sprite.getYOffset())
			self.map.getMap().delete(bonus)
			self.map.getMap().refresh()
			self.map.getMap().update_map_items()
			self.sprite.display()

		"""Detection d'arme"""
		if self.map.getMap().getEvent(EventData.TYPE, tmpx, tmpy, self.sprite.getXOffset(), self.sprite.getYOffset()) == "weapon":
			text = self.map.getMap().getText(tmpx, tmpy, self.sprite.getXOffset(), self.sprite.getYOffset())
			f = Font.Font(self.window, self.map.getMap(), text, 0)
			weapon = self.map.getMap().getEvent(EventData.NODE,tmpx, tmpy, self.sprite.getXOffset(), self.sprite.getYOffset())
			self.map.getMap().delete(weapon)
			GameVar.weapon = True
			self.has_a_weapon = True

		"""Detection de piège"""
		if self.map.getMap().getEvent(EventData.TYPE, tmpx, tmpy, self.sprite.getXOffset(), self.sprite.getYOffset()) == "trap":
			text = self.map.getMap().getText(tmpx, tmpy, self.sprite.getXOffset(), self.sprite.getYOffset())
			if text != "none":
				f = Font.Font(self.window, self.map.getMap(), text, 0)
			GameVar.life -= 1
			self.map.getMap().playerLife()
			self.sprite.display()
			return False

		"""Detection d'objet superposé"""
		if self.map.getMap().testCollide(self.sprite.getX() + self.sprite.getXOffset() / 2, self.sprite.getY() + self.sprite.getYOffset() / 2) == Collide.behindColor:
			self.sprite.setVisible(False)
		else: 
			self.sprite.setVisible(True)

	def collide(self, direction):
		if self.objectDetection(direction) == False:
			return False

		if direction == Dir.DOWN:
			if self.sprite.getY() + self.sprite.getYOffset() < GameVar.map_height:
				for i in range(self.sprite.getX(), self.sprite.getX() + self.sprite.getXOffset()):
					if self.map.getMap().testCollide(i, self.sprite.getY() + self.sprite.getYOffset() + 1) == Collide.simpleColor:
						return False

		if direction == Dir.UP:
			if self.sprite.getY() > 0:
				for i in range(self.sprite.getX(), self.sprite.getX() + self.sprite.getXOffset()):
					if self.map.getMap().testCollide(i, self.sprite.getY() - 1) == Collide.simpleColor:
						return False

		if direction == Dir.LEFT:
			if self.sprite.getX() > 0:
				for i in range(self.sprite.getY(), self.sprite.getY() + self.sprite.getYOffset()):
					if self.map.getMap().testCollide(self.sprite.getX() - 1, i) == Collide.simpleColor:
						return False

		if direction == Dir.RIGHT:
			if self.sprite.getX() + self.sprite.getXOffset() < GameVar.map_width:
				for i in range(self.sprite.getY(), self.sprite.getY() + self.sprite.getYOffset()):
					if self.map.getMap().testCollide(self.sprite.getX() + self.sprite.getXOffset() + 1, i) == Collide.simpleColor:
						return False

		return True
