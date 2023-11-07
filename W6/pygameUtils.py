# Event handler 

import pygame 


class EventHandler:
    def __init__(self, display):
        self.display = display
        self.queueOfEvents = []
        self.img = []
    # display = the display we are handling 
    
    def loadImages(self, img):
        self.img.append(img)
    
    def listen(self, events):
        self.queueOfEvents = events
        
        for event in self.queueOfEvents:
            print(event)
            if event.type == pygame.QUIT:
                exit()
                     
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
         
    def mouseEvents(self):
        pass        
    
    def keyEvent(self):
        pass