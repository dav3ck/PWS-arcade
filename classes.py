import pygame
import random

#colour variables REMOVE WHEN BITMAPS ARE IMPLEMENTED
black = (0, 0, 0) 
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)

#lists
bullets = pygame.sprite.Group() #list that will hold all the bullets
balls = pygame.sprite.Group() #list that will hold all ze balls
lines = pygame.sprite.Group() #list that holds all the lines in editor mode
everything = pygame.sprite.Group() #list that will hold everything
walls = pygame.sprite.Group() #lits that will hold all the floors and walls etc
players = pygame.sprite.Group()
upgrades = pygame.sprite.Group()

#sprite lists
ballanimation = [] #[size[type[variation[itteration]]]]
l1 = []
k1 = []
j1 = []

for i in range (3): #size of the ball size 0 = big, 1 = medium, 2 = small
    legacy0 = "Sprites/balls/size" + str(i)
    for j in range (2): #where the ball is in its bounce (type) 0 = in motion, 1 = on the ground
        legacy1 = legacy0 + "/type" + str(j)
        for k in range (3): #wich variation it is
            legacy2 = legacy1 + "/variation" + str(k)
            for l in range (5): #what exact sprite it is (itteration)
                legacy3 = legacy2 + "/itteration" + str(l) +".png"
                #image = pygame.image.load(legacy3)
                l1.append(legacy3)
            k1.append(l1)
            l1 = []
        j1.append(k1)
        k1 = []
    ballanimation.append(j1)
    j1 = []

#class defenitions
class parent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.xcord = 0
        self.ycord = 0
        self.xspeed = 0 #horizontal speed
        self.yspeed = 0 #vertical speed
        self.timer = 0 #timer to alternate bitmaps
        everything.add(self)

class Ball(parent):
    def __init__(self,check,x,y):
        super().__init__()
        self.xcord = x
        self.ycord = y
        self.dia = 0 #diameter of the ball
        self.weight = 0 #size of the parabole bigger number smaller parabole
        self.check = check #checks ball type
        self.sizenum = 0 #ball size number for animation
        self.typenum = 0 #the type of the ball
        self.ittnum = 0 #what itteration ball animation is on
        self.launch = 10
        if check == 1: #biggest ball
            self.xspeed = -2
            self.dia = 100
            self.weight = 0.1
            self.image = pygame.image.load("Sprites/balls/size0/type0/variation0/itteration0.png")
        elif check == 2: #medium ball right
            self.xspeed = 4
            self.dia = 50
            self.weight = 0.2
            self.sizenum = 1
            self.image = pygame.image.load("Sprites/balls/size1/type0/variation0/itteration0.png")
        elif check == 3: #medium ball left
            self.xspeed = -4
            self.dia = 50
            self.weight = 0.2
            self.sizenum = 1
            self.image = pygame.image.load("Sprites/balls/size1/type0/variation0/itteration0.png")
        elif check == 4: #small ball right
            self.xspeed = 7
            self.dia = 25
            self.weight = 0.3
            self.sizenum = 2
            self.image = pygame.image.load("Sprites/balls/size2/type0/variation0/itteration0.png")
        elif check == 5: #small ball left
            self.xspeed = -7
            self.dia = 25
            self.weight = 0.3
            self.sizenum = 2
            self.image = pygame.image.load("Sprites/balls/size2/type0/variation0/itteration0.png")
            
        self.rect = self.image.get_rect()
        balls.add(self)
        

    def update(self):
        self.xcord += self.xspeed #handles ball horizontal movement

        self.timer += 1
        if self.timer > 30 and self.typenum == 0:
            self.ittnum += 1
            self.timer = 0
            if self.ittnum > 4: #CHANGE THIS TO MATCH AMMOUNT OF FRAMES PER CYCLE -1
                self.ittnum = -1
        if self.timer > 3 and self.typenum == 1:
            self.ittnum += 1
            self.timer = 0
            if self.ittnum == 4:
                self.yspeed = self.launch
                self.xspeed *= 10000
                self.weight *= 10000
                self.ittnum = -1
                self.typenum = 0

        self.yspeed -= self.weight #handles ball bouncing
        self.ycord -= self.yspeed

        self.image = pygame.image.load(ballanimation[self.sizenum][self.typenum][0][self.ittnum])
        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.y = self.ycord

class Wall(parent):
    def __init__(self, x):
        super().__init__()
        self.xcord = x
        self.image = pygame.Surface([5,800])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.y = self.ycord
        self.rect.x = self.xcord
        walls.add(self)       

class Player(parent):
    def __init__(self):
        super().__init__()
        self.reducer = 1
        self.reducerup = 1
        self.xcord = 475 #x coördinate
        self.ycord = 700 #y coördinate
        self.ammo = 10
        self.lives = 3
        self.score = 0
        self.ammotimer = 0
        self.immune = False
        self.immunetimer = 0
        self.alive = True
        self.image = pygame.Surface([50,50])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        players.add(self)

    def changespeed(self,x):
        self.xspeed += x

    def reload(self):
        self.ammo = 0
        print("reloading")

    def update(self):
        if self.immune == True:
            self.immunetimer += 1
            if self.immunetimer % 20 == 0:
                self.image.fill(red)
            elif self.immunetimer % 20 == 10:
                self.image.fill(white)
            if self.immunetimer > 120:
                self.immune = False
                self.image.fill(green)
                self.immunetimer = 0
            if self.lives <= 0:
                self.alive = False
        if self.alive == False:
            self.xspeed = 0
            self.yspeed = 0
            self.image.fill(red)
            self.lives = 0
        self.xcord += (self.xspeed * (self.reducer * self.reducerup)) #basic player movement
        self.ycord += self.yspeed        
        self.rect.x = self.xcord
        self.rect.y = self.ycord


class Bullet(parent):
    def __init__(self, x,y):
        super().__init__()
        self.xcord = x + 25
        self.ycord = y
        self.yspeed = 10
        self.image = pygame.Surface([3,10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        bullets.add(self)

    def update(self):
        self.ycord -= self.yspeed #moving the ball up
        self.rect.y = self.ycord
        self.rect.x = self.xcord
        if self.ycord < -10:
            pygame.sprite.Sprite.kill(self)

class Floor(parent):
    def __init__(self):
        super().__init__()
        self.ycord = 750
        self.image = pygame.Surface([1000,50])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.y = self.ycord
        self.rect.x = self.xcord


    



        

#Powerups 

class Upgrade(parent):
    def __init__(self,check):
        super().__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.ycord = random.randrange(20,400)
        self.despawn = 0 # These two are for
        self.detimer = 0 # despawning on the floor
        self.active = False
        if random.randrange(2) == 1:
            self.xcord = 1000
            self.xspeed = -1
        else:
            self.xcord = -50
            self.xspeed = 1
        self.timer = 0
        self.check = check
        upgrades.add(self)

    def powerup(self,player,ball,balls):
        self.detimer = 0
        self.active = True
        #zwakke powerups
        if self.check == 0: #extera ammo
            player.ammo = 20
            pygame.sprite.Sprite.kill(self)
        elif self.check == 1: #speed up
            player.reducerup = 1.5
            self.timer = 0
            self.vanish()
        elif self.check == 2: #extera life
            player.lives += 1
            pygame.sprite.Sprite.kill(self)
        
        #sterke powerups
        elif self.check == 100: #slimes slow
            for ball in balls:
                if ball.ycord < 700:
                    ball.xspeed /= 1000
                    ball.yspeed /= 1000
                    ball.weight /= 1000
                    ball.launch = 0
                    self.timer = 0
            self.vanish()

    def powerdown(self,player,ball,balls):
        if self.active == True:
            if self.timer > 600 and self.check ==1:
                player.reducerup = 1
                pygame.sprite.Sprite.kill(self)
            if self.timer > 1800 and self.check == 2:
                ball.xspeed *= 1000
                ball.yspeed *= 1000
                ball.weight *= 1000
                ball.launch = 10

    def vanish(self):
        self.image = pygame.Surface([0,0])
        self.xcord = -10
        self.ycord = 0

    def update(self):
        self.timer += 1
        self.despawn += self.detimer
        self.xcord += self.xspeed
        self.ycord += self.yspeed
        self.rect.y = self.ycord
        self.rect.x = self.xcord
        if self.xcord < -100 or self.xcord > 1100 or self.despawn > 300:
            pygame.sprite.Sprite.kill(self)
