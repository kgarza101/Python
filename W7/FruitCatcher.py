import pygame
from EventHandler import *

pygame.init()

# create a display
disp = pygame.display.set_mode((800, 600))

# Fill the background with (200, 200, 200)
disp.fill((200, 200, 200))

gameClock = pygame.time.Clock()

# Create EventHandler object
handler = EventHandler(disp)

# Create a main loop
while True:
    handler.listen(pygame.event.get())

    pygame.display.update()

    gameClock.tick(20)

