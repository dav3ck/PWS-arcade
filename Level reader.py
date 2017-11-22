import pygame
pygame.init()
import math

width = 1280
height = 1024

    #Variable Colors

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)
yellow = (140, 0,140)

#Screen setup

Level = []
value = 0

screen = pygame.display.set_mode((width,height))
screen_rect=screen.get_rect()
pygame.display.set_caption('Level reader')
clock = pygame.time.Clock()

everything = pygame.sprite.Group()

class parent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.xcord = 0
        self.ycord = 0
        self.xspeed = 0 #horizontal speed
        self.yspeed = 0 #vertical speed
        everything.add(self)

class Block(parent):
    def __init__(self, row, colum):
        super().__init__()
        self.row = row
        self.colum = colum
        self.color = color
        self.image = pygame.Surface([40,40])
        self.image.fill(green)
        self.rect = self.image.get_rect()

    def update(self):

        self.xcord = self.colum * 40
        self.ycord = self.row * 40 

        self.rect.y = self.ycord
        self.rect.x = self.xcord

def spawnlevel():
    for y in range(20):
        for x in range(32):
             value = Level[0][y][x]
             block = Block(x, y) 
             
        
while True:
   
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spawnlevel()
                

    everything.update()

    screen.fill(black)
    everything.draw(screen)

    pygame.display.flip()

    clock.tick(60)

    
