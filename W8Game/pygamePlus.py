import pygame
import random
from Berry import *
from Bucket import *
from EventHandler import *

pygame.init()

dis_wid = 800
dis_hei = 600
display = pygame.display.set_mode((800, 600))
display = pygame.display.set_mode((800, 600))


class GameObject:
    def __init__(self, path, width, height):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()


event_handler = EventHandler(dis_wid, dis_hei)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("LEFT")
                event_handler.bucket.update(event_handler.bucket.rect.x - 20)
                
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                event_handler.bucket.update(event_handler.bucket.rect.x + 20)
                
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            print("X:", x, "Y:", y)
            event_handler.bucket.update(x)

    display.fill((200, 200, 200)) 

    event_handler.berry.update()
    event_handler.berry.draw(display)

    event_handler.bucket.draw(display)

    event_handler.checkCatch()

    pygame.display.update()
    clock.tick(20) 
