#libraries management
import pygame
import math
import random
pygame.init()
from classes import * #imports all from classes, removes the need for "classes."prepend

black = (0, 0, 0) #colour variables (MAY NEED TO BE REMOVED AFTER BITMAPS)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)
lightblue = (82, 219, 255)

withd = 1280 #Brete van scherm
height = 1024 #Hoogte van scherm

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
deadfont = pygame.font.SysFont('Comic Sans MS', 100)

spawntimer = 0

spawninterval = 0

gamestart = False

highscoredisp = False #change this to something life related

highscore = Highscore()


#editor mode variables
editor = False
xlines = 50
ylines = 50

#window setup
screen = pygame.display.set_mode((1280,1024))
screen_rect=screen.get_rect()
pygame.display.set_caption('early alfa')
clock = pygame.time.Clock()

player = Player() #creates the player

#creates play envoirment 
floor = Floor()
wall = Wall(0) #left wall
wall = Wall(1275) #right wall

#main game loop
while True:
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN: #handles all keypresses
            if gamestart == False:
                gamestart = True
                ball = Ball(1,500,70)
            if event.key == pygame.K_LEFT: #move left
                if player.alive == True:
                    player.changespeed(-5)
                else:
                    keyboard.num -= 1
            elif event.key == pygame.K_RIGHT: #move right
                if player.alive == True:
                    player.changespeed(5)
                else:
                    keyboard.num += 1
            elif event.key == pygame.K_UP:
                if player.alive == True:
                    print("there seems to be nothing here...")
                else:
                    keyboard.num -= 10
            elif event.key == pygame.K_DOWN:
                if player.alive == True:
                    print("there seems to be nothing here...")
                else:
                    keyboard.num += 10
            elif event.key == pygame.K_b: #spawn a ball 
                ball = Ball(1,640,70)
            elif event.key == pygame.K_k: #kills self
                player.alive = False
            elif event.key == pygame.K_SPACE: #shoot button
                if player.alive == True:
                    if player.ammo > 0 and spawntimer > 0:
                        bullet = Bullet(player.xcord,player.ycord)
                        player.ammo -= 1
                        player.fire = True
                else:
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
                    elif keyboard.num == 39: #Haalt een letter weg
                        keyboard.name = keyboard.name[:-1]
                        textbox.ittnum -= 1
                        print(textbox.ittnum)
                        for letter in letters:
                            if textbox.ittnum == letter.ittnum:
                                 pygame.sprite.Sprite.kill(letter)
                            if textbox.ittnum < 0:
                                textbox.ittnum = 0
                    elif keyboard.num == 40:
                        with open('highscores.txt','a') as f:
                            f.write(str(player.killcount) + " - " + keyboard.name + "\n")
                        for sprite in everything:
                            pygame.sprite.Sprite.kill(sprite)
                        gamestart = False
                        player = Player()
                        floor = Floor()
                        wall = Wall(0)
                        wall = Wall(1275)
            elif event.key == pygame.K_e: #Enables Editor mode
                if editor == True:
                    editor = False
                else:
                    editor = True
            elif event.key == pygame.K_r: #reload
                player.reload()
            elif event.key == pygame.K_p: #spawn a upgrade
                upgrade = Upgrade(100)
            elif event.key == pygame.K_q: #reset
                for sprite in everything:
                    pygame.sprite.Sprite.kill(sprite)
                player = Player()
                floor = Floor()
                wall = Wall(0)
                wall = Wall(1275)
        elif event.type == pygame.KEYUP: #handles all key releases
            if event.key == pygame.K_LEFT: #left key release
                if player.alive == True:
                    player.changespeed(5)
            elif event.key == pygame.K_RIGHT: #right key release
                if player.alive == True:
                    player.changespeed(-5)

    #GUI text
    scoretext = myfont.render('Score: ' + str(player.killcount), False, white)
    ammotext = myfont.render('Bullets: ' + str(player.ammo), False, white)
    lifetext = myfont.render('Lives: ' + str(player.lives), False, white)
    deadtext = deadfont.render('U diededed', False, red)
    playtext = myfont.render('Press any button to play', False, white)
    #if player.alive == False and player.once > 1:
        #nametext = myfont.render(keyboard.name,False, green)
    

    #Game logica
    if player.alive == False and player.once == 1:
        keyboard = Keyboard()
        textbox = Textbox()
        
    
    spawntimer += 1
    

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
                elif ball.check == 2 or ball.check == 3:
                    ball = Ball(4,ball.xcord,ball.ycord)
                    ball = Ball(5,ball.xcord,ball.ycord)
                else:
                    player.killcount += 1
                
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
                                                
    for upgrade in upgrades: #ends the powerups
        upgrade.powerdown(player,ball,balls)

    #spawning                
    if player.killcount < 40:
        spawninterval = int(-142 * math.sqrt(player.killcount) + 1800)
    else:
        spawninterval = 900

    if ((player.killcount > 2 and len(balls) < 2) or spawntimer % spawninterval == 0 and editor == False): #auto spawns balls
        ball = Ball(1,500,70)

    if spawntimer % 900 == 0: 
        if spawntimer % 2700 == 0:
            upgrade = Upgrade(random.randrange(100,102))
        else:
            upgrade = Upgrade(random.randrange(3))

    everything.update()
    
    #Screen management

    if player.xcord > (withd - 50):
        player.xcord = (withd - 50)
    elif player.xcord < 0:
        player.xcord = 0
        
    screen.fill(lightblue)
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
        player.killcount = 40

    #Display tekst    

    screen.blit(scoretext,(12,0))
    screen.blit(ammotext, (400, 0))
    screen.blit(lifetext, (700, 0))
    if player.alive == False and player.once > 2:
        screen.blit(deadtext, (380, 70))
        spawntimer = 0
    if gamestart == False:
        screen.blit(playtext, (490,400))
        spawntimer = 0
        for i in range(10):
            screen.blit(myfont.render(str(i + 1) + ". " + str(highscores[i]).replace("\n",""), False, white), (highscore.xcord, highscore.tempy))
            highscore.tempy += 40
            
    #Flip
    
    pygame.display.flip()
    
    #sets max fps
    clock.tick(60)
