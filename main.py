#libraries management
import pygame
pygame.init()
from classes import * #imports all from classes, removes the need for "classes." prepend

black = (0, 0, 0) #colour variables (MAY NEED TO BE REMOVED AFTER BITMAPS)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)

screen = pygame.display.set_mode((1000,800)) #setsup window
pygame.display.set_caption('very early pre-alfa')
clock = pygame.time.Clock()

player = Player() #creates the player

#main game loop
while True:
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN: #handles all keypresses
            if event.key == pygame.K_LEFT:
                player.xspeed = -5
            elif event.key == pygame.K_RIGHT:
                player.xspeed = 5
            elif event.key == pygame.K_b:
                ball = Ball(1,500,70)
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(player.xcord,player.ycord)
        elif event.type == pygame.KEYUP: #handles all key releases
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xspeed = 0
            

    #Game logica

    everything.update()

    for ball in balls:
        hits = pygame.sprite.spritecollide(player, balls, False) #ball on player colisions
        for ball in hits:
            ball.yspeed = 9.5
            player.image.fill(white)

    for bullet in bullets:
        hits = pygame.sprite.spritecollide(bullet, balls, True) #bullet on ball collisions
        for ball in hits:
            print("hit")
            pygame.sprite.Sprite.kill(bullet)
            if ball.check == 1:
                ball = Ball(2,ball.xcord,ball.ycord)
                ball = Ball(3,ball.xcord,ball.ycord)
            elif ball.check == 2 or ball.check == 3:
                ball = Ball(4,ball.xcord,ball.ycord)
                ball = Ball(5,ball.xcord,ball.ycord)
            else:
                print("here needs to be score code or something")
                
    #Screen management
    screen.fill(black)
    
    everything.draw(screen)
    
    pygame.display.flip()
    
    #sets max fps
    clock.tick(60)
