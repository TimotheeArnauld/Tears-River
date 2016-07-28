from lxml import etree
import GameVar

class EventData():
	X = 0
	Y = 1
	DIALOG = 2
	TYPE = 3
	NODE = 4

class EventContent():
	def __init__(self, type, dialog, x, y, w, h):
		self.type = type
		self.dialog = dialog
		self.x = int(x)
		self.y = int(y)
		self.w = w
		self.h = h

	def getType(self):
		return self.type

	def getDialog(self):
		return self.dialog

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getW(self):
		return self.w

	def getH(self):
		return self.h

class Event():
	def __init__(self, path):
		self.event = []

		tree = etree.parse("../resources/maps/fullmap.xml")
		for element in tree.xpath("/map/event"):
			if element.get("type") == "text":
				w = h = 32
				self.type__ = "text"
			if element.get("type") == "pnj":
				w = 32
				h = 48
				self.type__ = "pnj"
			if element.get("type") == "weapon":
					w = h = 32
					self.type__ = "weapon"
					self.gamevar_weapon = True
			if element.get("type") == "endofgame":
				w = h = 32
				self.type__ = "endofgame"
			if element.get("type") == "trap":
				w = h = 32
				self.type__ = "trap"
			if element.get("type") == "bonus":
				w = h = 32
				self.type__ = "bonus"
			content = list(element)
			dialog = content[0].text
			x = content[1].text
			y = content[2].text
			event = EventContent(self.type__, dialog, x, y, w, h)
			
			if GameVar.weapon == False:
				self.event.append(event)

	def getEvent(self, data, x, y, w, h):
		for e in self.event:
			for i in range(x, (x + w)):
				for j in range(y, (y + h)):
					if x < e.getX() + e.getW() and x + w > e.getX() and y < e.getY() + e.getH() and h + y > e.getY():
						if data == EventData.TYPE:
							return e.getType()
						elif data == EventData.X:
							return e.getX()
						elif data == EventData.Y:
							return e.getY()
						elif data == EventData.DIALOG:
							return e.getDialog()
						elif data == EventData.NODE:
							return e
		return "nothing"

	def deleteEvent(self, e):
		self.event.remove(e)

	def getPNJ(self):
		pnj = []
		for e in self.event:
			if e.getType() == "pnj":
				pnj.append(e)

		return pnj

	def getWeapon(self):
		weapon = []
		for e in self.event:
			if e.getType() == "weapon":
				weapon.append(e)

		return weapon

	def getBonus(self):
		bonus = []
		for e in self.event:
			if e.getType() == "bonus":
				bonus.append(e)

		return bonus

	def getTrap(self):
		trap = []
		for e in self.event:
			if e.getType() == "trap":
				trap.append(e)

		return trap

	def printText(self, x, y, w, h):
		e = self.getEvent(EventData.NODE, x, y, w, h)
		if(e != "nothing"):
			if e.getType() == "text":
				self.event.remove(e)
			return e.getDialog()
