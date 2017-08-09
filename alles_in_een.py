#libraries management
import pygame
pygame.init()
import fun

#predetermined variables
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)

sc_w = 1000 #screen width
sc_h = 800 #screen hight


#setsup window
screen = pygame.display.set_mode((sc_w,sc_h))
pygame.display.set_caption('very early pre-alfa')
clock = pygame.time.Clock()

#ball variable
class Ball(pygame.sprite.Sprite):
    def __init__(self,check,x,y):
        super().__init__()
        self.xcord = x
        self.xspeed = 0
        self.yspeed = 0
        self.ycord = y
        self.dia = 0 #diameter of the ball
        self.weight = 0 #size of the parabole bigger number smaller parabole
        self.check = check #checks ball type
        if check == 1: #biggest ball
            self.xspeed = 3
            self.dia = 100
            self.weight = 0.1
        elif check == 2:
            self.xspeed = 6
            self.dia = 50
            self.weight = 0.2
        elif check == 3:
            self.xspeed = -6
            self.dia = 50
            self.weight = 0.2
        elif check == 4:
            self.xspeed = 10
            self. dia = 25
            self.weight = 0.3
        elif check == 5:
            self.xspeed = -10
            self. dia = 25
            self.weight = 0.3
        self.image = pygame.Surface([self.dia,self.dia])
        self.image.fill(red)
        self.rect = self.image.get_rect() 

    def update(self):
        self.yspeed -= self.weight #handles ball bouncing
        self.ycord -= self.yspeed
        if self.ycord >= (sc_h - self.dia):
            self.yspeed = 10

        self.xcord += self.xspeed #handles ball horizontal movement
        if self.xcord >= (sc_w - self.dia) or self.xcord <= 0:
            self.xspeed *= -1
        self.rect.x = self.xcord
        self.rect.y = self.ycord                         
            

#general moving class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.xspeed = 0 #horizontal speed
        self.yspeed = 0 #vertical speed
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

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.xcord = x + 25
        self.ycord = y
        self.yspeed = 10
        self.image = pygame.Surface([3,10])
        self.image.fill(white)
        self.rect = self.image.get_rect()

    def update(self):
        self.ycord -= self.yspeed
        self.rect.y = self.ycord
        self.rect.x = self.xcord
        if self.ycord < -10:
            pygame.sprite.Sprite.kill(self) 

player = Player()

bullets = pygame.sprite.Group() #empty list that'll hold all ze bullets
balls = pygame.sprite.Group() #empty list that'll hold all ze balls
everything = pygame.sprite.Group()

everything.add(player)

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
            elif event.key == pygame.K_b:
                ball = Ball(1,500,70)
                balls.add(ball)
                everything.add(ball)
            elif event.key == pygame.K_n: #WARNING balls.add(ball) missing
                ball = Ball(2)
                everything.add(ball)
            elif event.key == pygame.K_m: #WARNING balls.add(ball) missing
                ball = Ball(4)
                everything.add(ball)
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(player.xcord,player.ycord)
                everything.add(bullet)
                bullets.add(bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.xspeed = 0
            

    #Game logica

    everything.update()
    for ball in balls:
        hits = pygame.sprite.spritecollide(player, balls, False)
        for ball in hits:
            ball.yspeed = 9.5
            player.image.fill(white)

    for bullet in bullets:
        collide = pygame.sprite.spritecollide(bullet, balls, True) 
        for ball in collide:
            print("hit")
            pygame.sprite.Sprite.kill(bullet)
            if ball.check == 1:
                ball = Ball(2,ball.xcord,ball.ycord)
                balls.add(ball)
                everything.add(ball)
                ball = Ball(3,ball.xcord,ball.ycord)
                balls.add(ball)
                everything.add(ball)
            elif ball.check == 2 or ball.check == 3:
                ball = Ball(4,ball.xcord,ball.ycord)
                balls.add(ball)
                everything.add(ball)
                ball = Ball(5,ball.xcord,ball.ycord)
                balls.add(ball)
                everything.add(ball)
            else:
                print("here needs to be score code or something")
                
            
        


    
    #Screen management
    screen.fill(black)
    
    everything.draw(screen)
    
    pygame.display.flip()
    
    #sets max fps
    clock.tick(60)

