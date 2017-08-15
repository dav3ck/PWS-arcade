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
lines = pygame.sprite.Group()
everything = pygame.sprite.Group() #list that will hold everything


#class defenitions
class parent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.xcord = 0
        self.ycord = 0
        self.xspeed = 0 #horizontal speed
        self.yspeed = 0 #vertical speed
        everything.add(self)

class Ball(parent):
    def __init__(self,check,x,y):
        super().__init__()
        self.xcord = x
        self.ycord = y
        self.dia = 0 #diameter of the ball
        self.weight = 0 #size of the parabole bigger number smaller parabole
        self.check = check #checks ball type
        if check == 1: #biggest ball
            self.xspeed = 2
            self.dia = 100
            self.weight = 0.1
        elif check == 2: #medium ball right
            self.xspeed = 4
            self.dia = 50
            self.weight = 0.2
        elif check == 3: #medium ball left
            self.xspeed = -4
            self.dia = 50
            self.weight = 0.2
        elif check == 4: #small ball right
            self.xspeed = 7
            self. dia = 25
            self.weight = 0.3
        elif check == 5: #small ball left
            self.xspeed = -7
            self. dia = 25
            self.weight = 0.3
        #self.image = pygame.Surface([self.dia,self.dia])
        #self.image.fill(red)
        self.image = pygame.image.load("Sprites/BIG1.png")
        self.rect = self.image.get_rect()
        balls.add(self)
        

    def update(self):
        self.yspeed -= self.weight #handles ball bouncing
        self.ycord -= self.yspeed
        if self.ycord >= (800 - self.dia): #REPLACE 800 W SCREEN HEIGHT
            self.yspeed = 10

        self.xcord += self.xspeed #handles ball horizontal movement
        if self.xcord >= (1000 - self.dia) or self.xcord <= 0: #REPLACE 100 WITH SCREEN WIDTH
            self.xspeed *= -1
        self.rect.x = self.xcord
        self.rect.y = self.ycord


class Player(parent):
    def __init__(self):
        super().__init__()
        self.xcord = 475 #x coördinate
        self.ycord = 750 #y coördinate
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


        



