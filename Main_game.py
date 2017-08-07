#libraries management
import pygame
pygame.init()
import classes

#predetermined variables
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)

sc_w = 1000 #screen width
sc_h = 800 #screen hight

player = classes.moving_object()
ball = classes.ball(50)

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xspeed = 0
            

    #Game logica

    player.xcord += player.xspeed #basic player movement
    player.ycord += player.yspeed

    ball.yspeed -= ball.weight #handles ball bouncing
    ball.ycord -= ball.yspeed
    if ball.ycord >= (sc_h - ball.dia):
        ball.yspeed = 10

    ball.xcord += ball.xspeed #handles ball horizontal movement
    if ball.xcord >= (sc_w - ball.dia) or ball.xcord <= (0 + ball.dia):
        ball.xspeed *= -1
    
    #Screen management
    screen.fill(black)

    pygame.draw.rect(screen, green, [sc_w/2-25+player.xcord,sc_h-50+player.ycord,50,50] , 2)
    pygame.draw.circle(screen, red, [ball.xcord, int(ball.ycord)], ball.dia, 5)

    pygame.display.flip()
    
    #sets max fps
    clock.tick(60)
