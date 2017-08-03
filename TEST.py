#setsup code
import pygame
pygame.init()

#predetermined variables
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

sc_w = 1000 #screen width
sc_h = 800 #screen hight

x = 50
y = 50
Change_x = 0.333333
Change_y = 0.54314 

#setsup window
screen = pygame.display.set_mode((sc_w,sc_h))
pygame.display.set_caption('very early pre-alfa')
clock = pygame.time.Clock()

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    #Game logica

    #Screen management
    #screen.fill(black)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


    pygame.draw.line(screen,green,[0,0],[sc_w,sc_h],2)
    pygame.draw.line(screen,green,[sc_w,0],[0,sc_h],2)
    
    pygame.draw.rect(screen, white, [x, y, 1, 1])

    if x >= sc_w or x<= 0:   
        Change_x *= -1
    x += Change_x
    if y >= sc_h or y <= 0:
        Change_y *= -1 
    y += Change_y
    
    pygame.display.flip()
    
    #I copied this from the tutorial, dunnow why
    clock.tick(6000000000000000)   

