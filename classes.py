import pygame

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
surfaces = pygame.sprite.Group() #lits that will hold all the floors and walls etc

#sprite lists
ballanimation = [] #[size [type [variatie [itteration]]]]

for i in range (3): #size of the ball size 0 = big, 1 = medium, 2 = small
    legacy0 = "Sprites/size" + str(i)
    j1 = []
    k1 = []
    l1 = []
    for j in range (2): #where the ball is in its bounce (type) 0 = in motion, 1 = on the ground
        legacy1 = legacy0 + "/type" + str(j)
        for k in range (1): #wich variation it is
            legacy2 = legacy1 + "/variation" + str(k)
            for l in range (5): #what exact sprite it is (itteration)
                legacy3 = legacy2 + "/itteration" + str(l) +".png"
                #image = pygame.image.load(legacy3)
                l1.append(legacy3)
            k1.append(l1)
        j1.append(k1)
    ballanimation.append(j1)

            
            
            

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
        self.delay = 1 #delays the bounce for animation
        if check == 1: #biggest ball
            self.xspeed = 2
            self.dia = 100
            self.weight = 0.1
            self.image = pygame.image.load("Sprites/size0/type0/variation0/itteration0.png")
        elif check == 2: #medium ball right
            self.xspeed = 4
            self.dia = 50
            self.weight = 0.2
            self.sizenum = 1
            self.image = pygame.image.load("Sprites/size1/type0/variation0/itteration0.png")
        elif check == 3: #medium ball left
            self.xspeed = -4
            self.dia = 50
            self.weight = 0.2
            self.sizenum = 1
            self.image = pygame.image.load("Sprites/size1/type0/variation0/itteration0.png")
        elif check == 4: #small ball right
            self.xspeed = 7
            self. dia = 25
            self.weight = 0.3
            self.sizenum = 2
            self.image = pygame.image.load("Sprites/size2/type0/variation0/itteration0.png")
        elif check == 5: #small ball left
            self.xspeed = -7
            self. dia = 25
            self.weight = 0.3
            self.sizenum = 2
            self.image = pygame.image.load("Sprites/size2/type0/variation0/itteration0.png")
            
        self.rect = self.image.get_rect()
        balls.add(self)
        

    def update(self):
        self.xcord += self.xspeed #handles ball horizontal movement
        if self.xcord >= (1000 - self.dia) or self.xcord <= 0: #REPLACE 100 WITH SCREEN WIDTH
            self.xspeed *= -1

        if self.typenum == 1:
            self.delay = 0.5
        else:
            self.delay = 1

        self.yspeed -= self.delay * self.weight #handles ball bouncing
        self.ycord -= self.delay * self.yspeed

        self.timer += 1
        if self.timer > (self.delay * 30):
            self.ittnum += 1
            self.timer = 0
            if self.ittnum > 4: #CHANGE THIS TO MATCH AMMOUNT OF FRAMES PER CYCLE -1
                self.ittnum = 0
                self.typenum = 0

        self.image = pygame.image.load(ballanimation[self.sizenum][self.typenum][0][self.ittnum])
        self.rect = self.image.get_rect()
        self.rect.x = self.xcord
        self.rect.y = self.ycord


class Player(parent):
    def __init__(self):
        super().__init__()
        self.xcord = 475 #x coördinate
        self.ycord = 700 #y coördinate
        self.image = pygame.Surface([50,50])
        self.image.fill(green)
        self.rect = self.image.get_rect()

    def update(self):
        self.xcord += self.xspeed #basic player movement
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

class Surface(parent):
    def __init__(self):
        super().__init__()
        self.ycord = 750
        self.image = pygame.Surface([1000,50])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.y = self.ycord
        self.rect.x = self.xcord



