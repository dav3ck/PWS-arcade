#libraries management
import pygame
pygame.init()
#from classes import *
import fun
import classes 

#predetermined variables
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)

sc_w = 1000 #screen width
sc_h = 800 #screen hight

player = classes.Moving_object()
#ball = classes.Ball()

balls = [] #empty list that'll hold all ze balls

#setsup window
screen = pygame.display.set_mode((sc_w,sc_h))
pygame.display.set_caption('very early pre-alfa')
clock = pygame.time.Clock()

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.xspeed = -5
            elif event.key == pygame.K_RIGHT:
                player.xspeed = 5
            elif event.key == pygame.K_b:
                balls.append(classes.Ball())
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xspeed = 0
            

    #Game logica

    player.xcord += player.xspeed #basic player movement
    player.ycord += player.yspeed

    for i in balls:
        i.yspeed -= i.weight #handles ball bouncing
        i.ycord -= i.yspeed
        if i.ycord >= (sc_h - i.dia):
            i.yspeed = 10

        i.xcord += i.xspeed #handles ball horizontal movement
        if i.xcord >= (sc_w - i.dia) or i.xcord <= (0 + i.dia):
            i.xspeed *= -1
    
    #Screen management
    screen.fill(black)
    
    pygame.draw.rect(screen, green, [sc_w/2-25+player.xcord,sc_h-50+player.ycord,50,50] , 2)
    for i in balls:
        pygame.draw.circle(screen, red, [i.xcord, int(i.ycord)], i.dia, 5)

    pygame.display.flip()
    
    #sets max fps
    clock.tick(60)

