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
deadfont = pygame.font.SysFont('Comic Sans MS', 100)

spawntimer = 0

#editor mode variables
editor = False
xlines = 50
ylines = 50

#window setup
screen = pygame.display.set_mode((1000,800))
screen_rect=screen.get_rect()
pygame.display.set_caption('early pre-alfa')
clock = pygame.time.Clock()

player = Player() #creates the player

#creates play envoirment 
floor = Floor()
wall = Wall(0) #left wall
wall = Wall(995) #right wall

#main game loop
while True:
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN: #handles all keypresses
            if event.key == pygame.K_LEFT: #move left
                player.changespeed(-5)
            elif event.key == pygame.K_RIGHT: #move right
                player.changespeed(5)
            elif event.key == pygame.K_b: #spawn a ball 
                ball = Ball(1,500,70)
            elif event.key == pygame.K_SPACE: #shoot button
                if player.ammo > 0:
                    bullet = Bullet(player.xcord,player.ycord)
                    player.ammo -= 1
            elif event.key == pygame.K_e: #Enables Editor mode
                if editor == True:
                    editor = False
                else:
                    editor = True
            elif event.key == pygame.K_r: #reload
                player.reload()
            elif event.key == pygame.K_p: #spawn a upgrade
                upgrade = Upgrade(2)
        elif event.type == pygame.KEYUP: #handles all key releases
            if event.key == pygame.K_LEFT: #left key release
                player.changespeed(5)
            elif event.key == pygame.K_RIGHT: #right key release
                player.changespeed(-5)

    #GUI text
    scoretext = myfont.render('Score: ' + str(player.score), False, white)
    ammotext = myfont.render('Bullets: ' + str(player.ammo), False, white)
    lifetext = myfont.render('Lives: ' + str(player.lives), False, white)
    deadtext = deadfont.render('U diededed', False, red)
    

    #Game logica

    spawntimer += 1

    if player.ammo == 0: #reload mechanics
        player.reducer = 0.5
        player.ammotimer += 1
        if player.ammotimer == 180:
            player.ammo = 10
            player.reducer = 1
            player.ammotimer = 0
    if player.ammo > 0 and player.ammotimer > 0:
        player.reducer = 1
        player.ammotimer = 0

    for ball in balls:
        hits = pygame.sprite.spritecollide(player, balls, False) #ball on player colisions
        for ball in hits:
            if ball.typenum == 0:
                ball.yspeed = 9.5
            if player.immune == False:
                player.immune = True
                player.lives -= 1
                
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
                player.score += 1
                
    for ball in balls: #ball floor bouncing
        hits = pygame.sprite.spritecollide(floor, balls, False)
        for ball in hits:
            if ball.typenum == 0:
                ball.yspeed = 0
                ball.xspeed /= 10000
                ball.weight /= 10000
                ball.typenum = 1
                ball.ittnum = -1

    for ball in balls: #ball wall bouncing
        hits = pygame.sprite.spritecollide(ball, walls, False)
        for wall in hits:
            if ball.xspeed > 0 and ball.typenum == 1:
                ball.xcord -= 10
            elif ball.xspeed < 0 and ball.typenum == 1:
                ball.xcord += 10
            ball.xspeed *= -1

    for upgrade in upgrades: #stops the upgrades on the floor
        hits = pygame.sprite.spritecollide(floor, upgrades, False)
        for upgrade in hits:
            upgrade.yspeed = 0
            upgrade.detimer = 1

    for bullet in bullets: #shoot the upgrades down
        hits = pygame.sprite.spritecollide(bullet, upgrades, False)
        for upgrade in hits:
            upgrade.yspeed = 5
            upgrade.xspeed = 0
            pygame.sprite.Sprite.kill(bullet)

    for upgrade in upgrades: #runs the powerups
        hits = pygame.sprite.spritecollide(player, upgrades, False)
        for upgrade in hits:
            if upgrade.check == 0: #extera ammo
                player.ammo = 20
                upgrade.vanish()
                pygame.sprite.Sprite.kill(upgrade)
            elif upgrade.check == 1: #speed up
                player.reducerup = 2
                upgrade.vanish()
            elif upgrade.check == 2: #slimes slow
                for ball in balls:
                    if ball.ycord < 700:
                        ball.xspeed = 0
                        ball.yspeed = 0
                        ball.weight = 0
                        ball.launch = 0
                upgrade.vanish()
                                                
    for upgrade in upgrades: #ends the powerups
        if upgrade.timer > 600 and upgrade.check ==1:
                player.reducerup = 1
                pygame.sprites.Sprites.kill(upgrade)

                
    if ((player.score > 2 and len(balls) < 2) or (spawntimer % 1800 == 0) and editor == False): #auto spawns balls
        ball = Ball(1,500,70)

    everything.update()
    #Screen management

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
        player.lives = 42

    #Display tekst    

    screen.blit(scoretext,(12,0))
    screen.blit(ammotext, (400, 0))
    screen.blit(lifetext, (700, 0))
    if player.alive == False:
        screen.blit(deadtext, (200, 300))

    #Flip
    
    pygame.display.flip()
    
    #sets max fps
    clock.tick(60)
