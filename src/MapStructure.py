from lxml import etree
import Map
import Animation

class Direction():
	INIT = 0
	LEFT = 1
	RIGHT = 2
	UP = 3
	DOWN = 4

class Row():
	def __init__(self):
		self.paths = []

	def ap(self, path):
		self.paths.append(path)

	def getMap(self):
		return self.paths

class MapStructure():
	rows = []
	actual = ""

	def __init__(self, window):
		self.window = window
		tree = etree.parse("../resources/maps/fullmap.xml")

		for element in tree.xpath("/maps/row"):
			row = Row()
			content = list(element)

			for c in content:
				mappath = c[0].text
				row.ap(mappath)

			self.rows.append(row)

		self.map = Map.Map(window, self.changeMap(Direction.INIT))

	def changeMap(self, direction):
		i = j = 0
		for m in self.getRows():
			try:
				j = m.getMap().index(self.actual)
			except:
				j = -1
			if j != -1:
				break
			i += 1

		if direction == Direction.INIT:
			"""self.actual = self.getRows()[0].getMap()[0]"""
			a = Animation.Animation(self.window, "../resources/maps/fullmap.png", 5)
			a.fadein()
			self.map = Map.Map(self.window, self.actual)

		if direction == Direction.LEFT:
			if j == 0:
				return False
			self.actual = self.getRows()[i].getMap()[j - 1]
			self.map = Map.Map(self.window, self.actual)
				
		if direction == Direction.RIGHT:
			try:
				self.actual = self.getRows()[i].getMap()[j + 1]
				self.map = Map.Map(self.window, self.actual)
			except:
				return False
			
		if direction == Direction.UP:
			if i == 0:
				return False 

			self.actual = self.getRows()[i - 1].getMap()[j]
			self.map = Map.Map(self.window, self.actual)
			
		if direction == Direction.DOWN:
			try:
				self.actual = self.getRows()[i + 1].getMap()[j]
				self.map = Map.Map(self.window, self.actual)
			except:
				return False

		return self.actual


	def getRows(self):
		return self.rows

	def getMap(self):
		return self.map

