import pygame
import random

pygame.init()
dis_wid = 800
dis_hei = 600
display = pygame.display.set_mode((800, 600))

class EventHandler:
    def __init__(self, dis_wid, dis_hei):
        self.berry = Berry("C:/Users/xxsco/Downloads/silly ahh goofy/Python/W8Game./strawberry.png", 100, 100, 800, 600)
        self.bucket = Bucket("C:/Users/xxsco/Downloads/silly ahh goofy/Python/W8Game./bucket.png", 100, 100)
        self.scorecount = 0

    def checkCatch(self):
        if self.bucket.rect.colliderect(self.berry.rect):
            self.scorecount += 1
            self.berry.reload()
            self.berry.increaseDrop(5)

        if self.berry.rect.y > dis_hei:
            print("Your Score:", self.scorecount)
            pygame.quit()
            exit()

class GameObject:
    def __init__(self, path, width, height):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()


class Berry(GameObject):
    def __init__(self, path, width, height, dis_wid, dis_hei):
        super().__init__(path, width, height)
        self.rect.x = random.randint(0, dis_wid - width)
        self.rect.y = 0
        self.drop = 5

    def draw(self, display):
        display.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.drop

    def reload(self):
        self.rect.y = 0
        self.rect.x = random.randint(0, dis_wid - self.rect.width)

    def increaseDrop(self, score):
        self.drop += score


class Bucket(GameObject):
    def __init__(self, path, width, height):
        super().__init__(path, width, height)
        self.rect.x = 0
        self.rect.y = dis_hei - height

    def draw(self, display):
        display.blit(self.image, self.rect)

    def update(self, new_x):
        self.rect.x = new_x


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
