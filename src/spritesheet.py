import pygame
import os

BLACK = (0,0,0,0)
 
class spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(os.path.join("../resources/", filename)).convert()

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.set_colorkey(BLACK)
        image.blit(self.sheet, (0, 0), rect)
        return image

    def getXOffset(self, col):
    	return int(self.sheet.get_width() / col)

    def getYOffset(self, row):
    	return int(self.sheet.get_height() / row)
