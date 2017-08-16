#libraries management
import pygame
pygame.init()
from classes import * #imports all from classes, removes the need for "classes." prepend

black = (0, 0, 0) #colour variables (MAY NEED TO BE REMOVED AFTER BITMAPS)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)

withd = 1000 #Brete van scherm
height = 800 #Hoogte van scherm

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

Score = 0
spawntimer = 0

editor = False
xlines = 50
ylines = 50

screen = pygame.display.set_mode((1000,800)) #setsup window
pygame.display.set_caption('early pre-alfa')
clock = pygame.time.Clock()

player = Player() #creates the player
surface = Surface()

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
            elif event.key == pygame.K_e: #Enables Editor mode
                editor = True
        elif event.type == pygame.KEYUP: #handles all key releases
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xspeed = 0
            
    #Score tekst
    textsurface = myfont.render('Score: ' + str(Score), False, white)

    #Game logica

    spawntimer += 1

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
                Score += 1
                
    for ball in balls:
        hits = pygame.sprite.spritecollide(surface, balls, False)
        for ball in hits:
            if ball.typenum == 0:
                ball.yspeed = 0
                ball.xspeed = ball.xspeed / 10000
                ball.weight = ball.weight / 10000
                ball.typenum = 1
                ball.ittnum = -1
            
                     
 
            

    if (Score > 2 and len(balls) < 2) or spawntimer > 1800: #auto spawns balls
        ball = Ball(1,500,70)
        spawntimer = 0

    #Screen management
    everything.update()
        
    screen.fill(black)
    
    everything.draw(screen)

    #Editor mode
    if editor == True:
        while xlines < withd or ylines < height:
            pygame.draw.line(screen, white, (xlines, 0), (ylines, height))
            pygame.draw.line(screen, white, (0, ylines), (withd, ylines))
            xlines += 50
            ylines += 50
        xlines = 50
        ylines = 50

    #Display tekst    

    screen.blit(textsurface,(0,0)) 

    #Flip
    
    pygame.display.flip()
    
    #sets max fps
    clock.tick(60)
