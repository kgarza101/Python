import pygame 
from Berry import * 

class Bucket(Berry):
    def __init__(self, img):
        super().__init__(img)
        
        self.img = pygame.image.load('C:/Users/xxsco/Downloads/silly ahh goofy/Python/W8/bucket.png')
        self.img = pygame.transform.scale(self.img, (100, 100))
        
        self.rect.x = 0
        self.rect.y = 0
        
    def draw(self, display):
            display.blit(self.img, (self.x, self.y))
            
    def update(self, x1):
        self.rect.x = x1
        
