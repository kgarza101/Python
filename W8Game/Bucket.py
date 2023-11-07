import pygame 
from pygamePlus import *
from EventHandler import *


class Bucket(GameObject):
    def __init__(self, path, width, height):
        super().__init__(path, width, height)
        self.rect.x = 0
        self.rect.y = 600 - height

    def draw(self, display):
        display.blit(self.image, self.rect)

    def update(self, new_x):
        self.rect.x = new_x