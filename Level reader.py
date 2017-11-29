import pygame
pygame.init()
import math
import random
import classes 
from classes import *

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
line = 1

Level = []
value = 0
blockvalue = 0

screen = pygame.display.set_mode((width,height))
screen_rect=screen.get_rect()
pygame.display.set_caption('Level reader')
clock = pygame.time.Clock()

background = pygame.image.load('Sprites/Extra/Background.png').convert()

#everything = pygame.sprite.Group()

floor = Floor()
wall = Wall(0) #left wall
wall = Wall(1275) #right wall



with open('Levels.txt', 'r') as lines:
    lines = lines.read()
    lines = [line.rstrip('\n') for line in open('Levels.txt')]


'''class parent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.xcord = 0
        self.ycord = 0
        self.xspeed = 0 #horizontal speed
        self.yspeed = 0 #vertical speed
        everything.add(self)

class Block(parent):
    def __init__(self, row, colum, xsize, ysize, color):
        super().__init__()
        self.row = row
        self.xsize = xsize
        self.ysize = ysize
        self.colum = colum
        self.image = pygame.Surface([40 * xsize,40 * ysize])
        self.image.fill(green)
        self.rect = self.image.get_rect()

    def update(self):

        self.xcord = self.colum * 40
        self.ycord = self.row * 40 

        self.rect.y = self.ycord
        self.rect.x = self.xcord'''

def spawnlevel(Level):
    for y in range(21):
        value = lines[y + 1]
        print(value)
        for x in range(32):
            blockvalue = value[x]
            spawnitems(y,x,blockvalue)
            

def spawnitems(y,x, typ):

    y = y * 40
    x = x * 40
    
    if typ == '1':
        player = Player(x,y)
    elif typ == '2':
        block = Block(y,x,1,1,black)
    elif typ == '3':
        block = Block(y,x,1,1,blue)
    elif typ == '4':
        block = Block(y,x,1,1,blue)
    elif typ == '5':
        block = Block(y,x,1,1,green)
    elif typ == '6':
        block = Block(y,x,1,1,white)
    elif typ == '7':
        ball = Ball(4,x,y, True)
    elif typ == '8':
        ball = Ball(2,x,y, True)
    elif typ == '9':
        ball = Ball(1,x,y, True)
        
while True:
   
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(Level)
                spawnlevel(Level)

                

    everything.update()
  
    screen.blit(background,(0,0))
    
    everything.draw(screen)

    pygame.display.flip()

    clock.tick(60)

    
