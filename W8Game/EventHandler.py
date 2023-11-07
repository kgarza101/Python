import pygame
from pygamePlus import *
from Berry import *
from Bucket import *

class EventHandler:
    def __init__(self, dis_wid, dis_hei):
        self.berry = Berry("C:/Users/xxsco/Downloads/silly ahh goofy/Python/W8Game./strawberry.png", 100, 100, 800, 600)
        self.bucket = Bucket("C:/Users/xxsco/Downloads/silly ahh goofy/Python/W8Game./bucket.png", 100, 100)
        self.playerScore = 0

    def checkCatch(self):
        if self.bucket.rect.colliderect(self.berry.rect):
            self.playerScore += 1
            self.berry.reload()
            self.berry.increaseDrop(5)

        if self.berry.rect.y > 600:
            print("Your Score:", self.playerScore)
            pygame.quit()
            quit()