#libraries management
import pygame
import math
import random
pygame.init()
from classes import * #imports all from classes, removes the need for "classes."prepend

black = (0, 0, 0) #defines the colour black

withd = 1280 #Brete van scherm
height = 1024 #Hoogte van scherm

pygame.font.init()
myfont = pygame.font.Font('Sprites/Font/Arcade.ttf', 60)
myfontsmall = pygame.font.Font("Sprites/Font/Arcade.ttf", 40)

spawntimer = 0

globaltimer = 0

spawninterval = 0

gamestart = False

highscore = Highscore()

#window setup
screen = pygame.display.set_mode((1280,1024))#, pygame.FULLSCREEN)
screen_rect=screen.get_rect()
pygame.display.set_caption('Sticky Icky beta')
clock = pygame.time.Clock()

background = pygame.image.load('Sprites/Extra/Background.png').convert()

pygame.mouse.set_visible(0) #Removed mouse

player = Player() #creates the player

#creates play envoirment 
floor = Floor()
wall = Wall(0) #left wall
wall = Wall(1275) #right wall
flashart = Flashart("Sprites/Extra/Flash.png", 0, 0)


#main game loop
while True:
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN: #handles all keypresses
            if event.key == pygame.K_LEFT: #move left
                if player.alive == True and gamestart == True:
                    player.changespeed(-5)
                elif len(keyboards) == 1:
                    keyboard.num -= 1
            elif event.key == pygame.K_RIGHT: #move right
                if player.alive == True and gamestart == True:
                    player.changespeed(5)
                elif len(keyboards) == 1:
                    keyboard.num += 1
            elif event.key == pygame.K_UP:
                if player.alive == True:
                    print("there seems to be nothing here...")
                elif len(keyboards) == 1:
                    keyboard.num -= 10
            elif event.key == pygame.K_DOWN:
                if player.alive == True:
                    print("there seems to be nothing here...")
                elif len(keyboards) == 1:
                    keyboard.num += 10
            elif event.key == pygame.K_SPACE: #shoot button
                if gamestart == False:
                    gamestart = True
                    ball = Ball(1,500,70)
                    pygame.sprite.Sprite.kill(flashart)
                if player.alive == True:
                    if player.ammo > 0 and spawntimer > 0:
                        bullet = Bullet(player.xcord,player.ycord)
                        player.ammo -= 1
                        player.fire = True
                elif len(keyboards) == 1:
                    if textbox.ittnum < 5:
                        if (keyboard.capital == False and keyboard.num < 38): 
                            keyboard.name = keyboard.name + keyboard.alphabet[keyboard.num] #adds letter to list with name
                            letter = Letter(textbox.ittnum,keyboard.num,False)
                            textbox.ittnum += 1
                        elif keyboard.capital == True and keyboard.num < 38:
                            keyboard.name = keyboard.name + keyboard.alphabet[keyboard.num + 37] #adds Capital letter to name list
                            keyboard.capital = False  #Zet capital terug naar false > je print no longer Capitals
                            letter = Letter(textbox.ittnum,keyboard.num,True)
                            textbox.ittnum += 1
                    if keyboard.num == 38:
                        if keyboard.capital == False: #Zet capital naar true, tenzij het al true is, dan zet het het terug naar False
                            keyboard.capital = True
                        else:
                            keyboard.capital = False
                    elif keyboard.num == 39 and textbox.ittnum != 0: #Haalt een letter weg
                        keyboard.name = keyboard.name[:-1]
                        textbox.ittnum -= 1
                        for letter in letters:
                            if textbox.ittnum == letter.ittnum:
                                 pygame.sprite.Sprite.kill(letter)
                            if textbox.ittnum < 0:
                                textbox.ittnum = 0
                    elif keyboard.num == 40: #submits score and resets game
                        if len(keyboard.name) != 0:
                            with open('highscores.txt','a') as f:
                                f.write(scoredisp + " - " + keyboard.name + "\n")
                        for sprite in everything:
                            pygame.sprite.Sprite.kill(sprite)
                        highscores = []
                        with open('highscores.txt', 'r') as r:
                            for line in sorted(r):
                                highscores.insert(0, line)
                        gamestart = False
                        player = Player()
                        floor = Floor()
                        wall = Wall(0)
                        wall = Wall(1275)
                        highscore = Highscore()
                        flashart = Flashart("Sprites/Extra/Flash.png", 0, 0)
            elif event.key == pygame.K_r: #reload
                player.reload()
            elif event.key == pygame.K_m:
                screen = pygame.display.set_mode((1280,1024), pygame.FULLSCREEN)
            elif event.key == pygame.K_n:
                screen = pygame.display.set_mode((1280,1024))
                pygame.mouse.set_visible(1)
        elif event.type == pygame.KEYUP: #handles all key releases
            if event.key == pygame.K_LEFT: #left key release
                if player.alive == True and gamestart == True:
                    player.changespeed(5)
            elif event.key == pygame.K_RIGHT: #right key release
                if player.alive == True and gamestart == True:
                    player.changespeed(-5)

    #GUI text
    prescore = str(int(player.killcount * 100))
    zeros = 6 - len(prescore)
    scoredisp = '0' * zeros + prescore
    
    scoretext = myfont.render(scoredisp, False, black)
    ammotext = myfont.render(str(player.ammo), False, black)
    lifetext = myfont.render(str(player.lives), False, black)    

    #Game logica
    spawntimer += 1

    globaltimer += 1

    if player.alive == False and player.once == 1:
        flashart = Flashart("Sprites/Extra/GameOver.png", 414 , 50)
        player.deathtimer = 1

    if player.alive == False and player.deathtimer > 180 and len(keyboards) == 0: #Dit load na 3 seconde textbox in
        keyboard = Keyboard()
        textbox = Textbox()
        
    if player.ammo == 0: #reload mechanics
        player.reducer = 0.5
        player.ammotimer += 1
        if player.ammotimer == 120:
            player.ammo = 10
            player.reducer = 1
            player.ammotimer = 0
    if player.ammo > 0 and player.ammotimer > 0: #alowss abortion of reloading
        player.reducer = 1
        player.ammotimer = 0

    #colisions
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
            if ball.ycord > 50:
                pygame.sprite.Sprite.kill(bullet)
                if ball.check == 1:
                    ball = Ball(2,ball.xcord,ball.ycord)
                    ball = Ball(3,ball.xcord,ball.ycord)
                    player.killcount += 1
                elif ball.check == 2 or ball.check == 3:
                    ball = Ball(4,ball.xcord,ball.ycord)
                    ball = Ball(5,ball.xcord,ball.ycord)
                    player.killcount += 1
                else:
                    player.killcount += 3
                
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
            if player.alive == True:
                ball.xspeed *= -1

    for upgrade in upgrades: #stops the upgrades on the floor
        hits = pygame.sprite.spritecollide(floor, upgrades, False)
        for upgrade in hits:
            if upgrade.type == 1:
                upgrade.yspeed = 0
                upgrade.detimer = 1
                upgrade.ycord += 92
                upgrade.type = 2

    for upgrade in upgrades: #shoot the upgrades down
        hits = pygame.sprite.spritecollide(upgrade, bullets, False)
        for bullet in hits:
            upgrade.yspeed = 5
            upgrade.xspeed = 0
            upgrade.type = 1
            pygame.sprite.Sprite.kill(bullet)

    for upgrade in upgrades: #runs the powerups
        hits = pygame.sprite.spritecollide(upgrade, players, False)
        for player in hits:
            upgrade.yspeed = 0
            upgrade.powerup(player,ball,balls)
            player.killcount += 0.5
                                                
    for upgrade in upgrades: #ends the powerups
        upgrade.powerdown(player,ball,balls)

    #spawning                
    if globaltimer < 3600:
        spawninterval = int(-1 / 14400 * math.sqrt(globaltimer) + 1800)
    else:
        spawninterval = 900

    if ((player.killcount > 12 and len(balls) < 2) or spawntimer == spawninterval): #auto spawns balls
        ball = Ball(1,500,70)
        spawntimer = 0

    if globaltimer % 900 == 0: 
        if globaltimer % 2700 == 0:
            upgrade = Upgrade(random.randrange(3,6))
        else:
            upgrade = Upgrade(random.randrange(3))

    everything.update()
    
    #Screen management

    if player.xcord > (withd - 50):
        player.xcord = (withd - 50)
    elif player.xcord < 0:
        player.xcord = 0
        
    screen.blit(background,(0,0))
    
    everything.draw(screen)

    #Display tekst    

    screen.blit(scoretext,(880,950))
    screen.blit(ammotext, (380, 950))
    screen.blit(lifetext, (205, 950))
    
    if player.alive == False and player.once > 2:
        globaltimer = 0
        spawntimer = 0
    if gamestart == False:
        globaltimer = 0
        spawntimer = 0
        for i in range(10):
            screen.blit(myfontsmall.render(str(i + 1) + ". " + str(highscores[i]).replace("\n",""), False, black), (highscore.xcord, highscore.tempy))
            highscore.tempy += 40
            
    #Flip
    
    pygame.display.flip()
    
    #sets max fps
    clock.tick(60)
