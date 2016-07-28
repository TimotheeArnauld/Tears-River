import pygame
from pygame.locals import *
import Player
import MapStructure
import Splashscreen
import intro
import Menu
import Play

import GameVar

def init_game():
	GameVar.weapon = False
	GameVar.life = 3
	GameVar.item = 0

	GameVar.screen_width = 800
	GameVar.screen_height = 480

	GameVar.map_width = 2400
	GameVar.map_height = 1440

	GameVar.player_width = 32
	GameVar.player_height = 48

	GameVar.scroll_x = 0
	GameVar.scroll_y = 0

if __name__ == '__main__':
	pygame.init()
	pygame.display.set_caption("Tears river")

	init_game()

	window = pygame.display.set_mode((GameVar.screen_width, GameVar.screen_height))

	"""s = Splashscreen.Splashscreen(window)"""

	"""menu = Menu.Menu(window)"""
	p = Play.Play(window)
	