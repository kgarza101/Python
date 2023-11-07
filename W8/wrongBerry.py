import pygame 
import random

class GameObject:
    def __init__(self, img_path):
        self.imamge = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        
class Berry(GameObject):
    def __init__(self, img_path, dis_wid, dis_hei):
        super().__init__(img_path)
        
        self.img = pygame.image.load('C:/Users/xxsco/Downloads/silly ahh goofy/Python/W8/strawberry.png')
        self.img = pygame.transform.scale(self.img, (100, 100))
        
        self.rect = self.img.get_rect()
        self.x = 1
        self.y = 0
        self.drop = 5
        
    def draw(self, display):
        display.blit(self.img, (self.x, self.y))
        
    def update(self):
        self.y += self.drop
        self.rect.y = self.y
        
    def reload(self):
         self.x = random.randint(0, 800)
         self.y = 0 
         self.rect.x = self.x
         