import pygame
from classes import *

#colour variables REMOVE WHEN BITMAPS ARE IMPLEMENTED
black = (0, 0, 0) 
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)

def ammo(player):
    player.ammo = 20
    
class Upgrade(parent):
    def __init__(self):
        self.image = pygame.Surface([50,50])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.y = 200
        self.rect.x = 32
        print("i'm alive!")
        everything.add(self)
