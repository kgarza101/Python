import pygame

class EventHandler:
    def __init__(self, display):
        self.display = display
        
    def listen(self, queueOfEvents):
        # check each event in the queue
        for event in queueOfEvents:
            if event.type ==  pygame.QUIT:
                pygame.quit()
                exit()
                
            elif event.type == pygame.KEYDOWN:
                # Check which key is pressed down
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                
            elif event.type == pygame.MOUSEMOTION:
                x = event.pos[0]
                y = event.pos[1]
                print(f"x: {x}\t y: {y}")

# Strawb
    # Load in image

# Bucket