import pygame 

pygame.init()

display = pygame.display.set_mode((800, 600))
display.fill((200, 200, 200))
clock = pygame.time.Clock()

class EventHandler:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print("LEFT")

                    elif event.key == pygame.K_RIGHT:
                        print("RIGHT")
                        
                elif event.type == pygame.MOUSEMOTION:
                    x = event.pos[0]
                    y = event.pos[1]
                    print(f"x: {x}\t y: {y}")
                    event_handler.bucket.update(x)
                    
        

                
    
