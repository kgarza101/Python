import pygame 
import random
from pygamePlus import *
from EventHandler import *

class Berry(GameObject):
    def __init__(self, path, width, height, dis_wid, dis_hei):
        super().__init__(path, width, height)
        self.rect.x = random.randint(0, dis_wid - width)
        self.rect.y = 0
        self.drop = 5

    def draw(self, display):
        display.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.drop

    def reload(self):
        self.rect.y = 0
        self.rect.x = random.randint(0, 600 - self.rect.width)

    def increaseDrop(self, increment):
        self.drop += increment