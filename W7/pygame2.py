# Initialize a new pygame application
    # any color background
    # handle simple events
import pygame
from Button import *

# initializing pygame
pygame.init()

disp = pygame.display.set_mode((800, 600))
disp.fill((70, 50, 150))

# create a new rectangle object
    # any size, location, color
    # set_color() RGB
shape = pygame.Rect(50, 50, 80, 20)
# draw rectangle with color on disp 

##pygame.draw.rect(disp, (200, 200, 200), shape)

myButton = Button(disp)

# ctrate block object
gameClock = pygame.time.Clock()

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        myButton.eventResponse(event)
        myButton.draw()   
                 
    pygame.display.update()
    gameClock.tick(20)
    

