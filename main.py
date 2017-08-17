#libraries management
import pygame
pygame.init()
from classes import * #imports all from classes, removes the need for "classes."prepend

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

ammo = 10
ammotimer = 0


editor = False
xlines = 50
ylines = 50

screen = pygame.display.set_mode((1000,800)) #setsup window
screen_rect=screen.get_rect()
pygame.display.set_caption('early pre-alfa')
clock = pygame.time.Clock()

player = Player() #creates the player

floor = Floor()
wall = Wall(0) #left wall
wall = Wall(995) #right wall

#main game loop
while True:
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN: #handles all keypresses
            if event.key == pygame.K_LEFT:
                player.changespeed(-5)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(5)
            elif event.key == pygame.K_b:
                ball = Ball(1,500,70)
            elif event.key == pygame.K_SPACE:
                if player.ammo > 0:
                    bullet = Bullet(player.xcord,player.ycord)
                    player.ammo -= 1
            elif event.key == pygame.K_e: #Enables Editor mode
                if editor == True:
                    editor = False
                else:
                    editor = True
            elif event.key == pygame.K_r:
                player.reload()
        elif event.type == pygame.KEYUP: #handles all key releases
            if event.key == pygame.K_LEFT:
                player.changespeed(5)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-5)

    #GUI text
    scoretext = myfont.render('Score: ' + str(Score), False, white)
    ammotext = myfont.render('Bullets: ' + str(player.ammo), False, white)

    #Game logica

    spawntimer += 1

    if spawntimer == 3:
        upgrade = Upgrade(1)

    if player.ammo == 0:
        player.reducer = 0.5
        ammotimer += 1
    if ammotimer == 180:
        player.ammo = 10
        player.reducer = 1
        ammotimer = 0

    for ball in balls:
        hits = pygame.sprite.spritecollide(player, balls, False) #ball on player colisions
        for ball in hits:
            if ball.typenum == 0:
                ball.yspeed = 9.5
            player.image.fill(white)
                
    for bullet in bullets:
        hits = pygame.sprite.spritecollide(bullet, balls, True) #bullet on ball collisions
        for ball in hits:
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
        hits = pygame.sprite.spritecollide(floor, balls, False)
        for ball in hits:
            if ball.typenum == 0:
                ball.yspeed = 0
                ball.xspeed /= 10000
                ball.weight /= 10000
                ball.typenum = 1
                ball.ittnum = -1

    for ball in balls:
        hits = pygame.sprite.spritecollide(ball, walls, False)
        for wall in hits:
            if ball.xspeed > 0 and ball.typenum == 1:
                ball.xcord -= 10
            elif ball.xspeed < 0 and ball.typenum == 1:
                ball.xcord += 10
            ball.xspeed *= -1

    for player in players:
        hits = pygame.sprite.spritecollide(player, upgrades, False)
        for upgrade in hits:
            if upgrade.check == 0: player.ammo = 20
            elif upgrade.check == 1:
                player.reducerup = 2
                upgrade.timerlim = 1800
                upgrade.vanish()
                
    for upgrade in upgrades:
        if upgrade.timer > 600 and upgrade.check ==1:
                player.reducerup = 1
                
    if ((Score > 2 and len(balls) < 2) or (spawntimer % 1800 == 0) and editor == False): #auto spawns balls
        ball = Ball(1,500,70)

    #Screen management
    everything.update()

    if player.xcord > (withd - 50):
        player.xcord = (withd - 50)
    elif player.xcord < 0:
        player.xcord = 0
        
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
        player.ammo = 666

    #Display tekst    

    screen.blit(scoretext,(12,0))
    screen.blit(ammotext, (400, 0))

    #Flip
    
    pygame.display.flip()
    
    #sets max fps
    clock.tick(60)
