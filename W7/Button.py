import pygame

class Button:
    def __init__(self, display) -> None:
        self.myRect = pygame.Rect(50, 50, 80, 20)
        self.disp = display

        self.IDLECOL = (200, 200, 200)
        self.HOVERCOL = (100, 100, 100)
        self.CLICKCOL = (200, 0, 155)

        self.state = "idle"

    def draw(self):
        pygame.draw.rect(self.disp, self.CLICKCOL, self.myRect)
       
        def eventResponse(event):
            pass
        

    
       
            
            
        

