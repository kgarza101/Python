# Intro to pygame
import pygame
from pygameUtils import *

# 1. Initialize pygame
pygame.init()

# Initialize a display
mainDisp = pygame.display.set_mode((800, 600))

# Fill display with a background (RGB)
mainDisp.fill((200, 0, 100))

# Make clock object
gameclock = pygame.time.Clock()

# Load a local image file
myImg = pygame.image.load('C:/Users/xxsco/Downloads/silly ahh goofy/Python/W6/TBH.jpg')
#Img2 = pygame.image.load('C:/Users/xxsco/Downloads/silly ahh goofy/Python/W6/Img2.jpg')
# Draw the image to the screen
mainDisp.blit(myImg, (50,50))

handler = EventHandler(mainDisp)
handler = EventHandler(myImg)
# Wrtie a loop that will run forever until we exit  
while True:
    handler.listen(pygame.event.get() )
    # listen for events    
    # for event in pygame.event.get():
    #     print(event)
    #     if event.type == pygame.QUIT:
    #         print("Exiting now!")
    #         exit()
            
        # elif event.type == pygame.MOUSEBUTTONUP:
        #         pos = pygame.mouse.get_pos()
        #         print(pos)
                
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     # Cover old image
        #     mainDisp.fill((200, 0, 100))
        #     mainDisp.blit(Img2, (50, 50))
        
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     mainDisp.blit(myImg, (50,50))
    
    pygame.display.update()
    
    gameclock.tick(20)
    
    
    
    
        