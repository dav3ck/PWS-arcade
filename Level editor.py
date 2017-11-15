import pygame
pygame.init()
import math

#Variable

width = 1280
height = 1024

xlines = 40
ylines = 40


    #Variable Colors

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)

#Screen setup

screen = pygame.display.set_mode((width,height))
screen_rect=screen.get_rect()
pygame.display.set_caption('Level editor')
clock = pygame.time.Clock()

#Level array setup
row = []
colum = []
Level = []
for y in range(20):
    for x in range(32):
        colum.append(0)
    row.append(colum)
    colum = []
Level.append(row)


  
#vakjes 40p x 40p dus 32 breed en 25 hoog

everything = pygame.sprite.Group() #list that will hold everything

class parent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.xcord = 0
        self.ycord = 0
        self.xspeed = 0 #horizontal speed
        self.yspeed = 0 #vertical speed
        everything.add(self)

class Curser(parent):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.colum = 0
        self.row = 0
        self.blockvalue = 9
        self.blocksize = True
        self.Error = False


    def update(self):

        if self.Error == True:
            self.image.fill(red)
        else:
            self.image.fill(blue)
        
        self.xcord = self.colum * 40
        self.ycord = self.row * 40

        self.rect.y = self.ycord
        self.rect.x = self.xcord
        


class Block(parent):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill(red)
        self.rect = self.image.get_rect()

#functies

#Deze functie plaats de code
        
def writearray(value, row, colum):
 
    Level[0][row][colum] = value
    if value == 8:
        for x in range(2):
            for y in range(2):
                if x != 0 or y != 0:
                    Level[0][row - x][colum + y] = 8.5

    elif value == 9:
        for x in range(3):
            for y in range(4):
                if x != 0 or y != 0:
                    Level[0][row - x][colum + y] = 9.5

#Deze functie verwijderd de code

def cleararray(row, colum):
    value = Level[0][row][colum]
    
    if type(value != float):
        Level[0][row][colum] = 0
    
        if value == 8:
            for x in range(2):
                for y in range(2):
                    if x != 0 or y != 0:
                        Level[0][row - x][colum + y] = 0

        elif value == 9:
            for x in range(3):
                for y in range(4):
                    if x != 0 or y != 0:
                        Level[0][row - x][colum + y] = 0
                    
#De check functie checked of iets geplaatst kan worden!

def check(value, row, colum):
    Error = False

    if value == 8:
        for x in range(2):
            for y in range(2):
                if row - x < 0 or colum + y > 31 or type(Level[0][row - x][colum + y]) is float or Level[0][row - x][colum + y] == 8 or Level[0][row - x][colum + y] == 9:
                    Error = True
                    
    elif value == 9:
        for x in range(3):
            for y in range(4):
                if row - x < 0 or colum + y > 31 or type(Level[0][row - x][colum + y]) is float or Level[0][row - x][colum + y] == 8 or Level[0][row - x][colum + y] == 9:
                    Error = True
    else:
        if Level[0][row][colum] != 0:
            Error = True
    return Error


#Aanroepingen

curser = Curser()

        
#Echte spel

while True:

    curser.Error = check(curser.blockvalue, curser.row, curser.colum)
    
    
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN: #handles all keypresses
            if event.key == pygame.K_LEFT:
                curser.colum -= 1
            elif event.key == pygame.K_RIGHT:
                curser.colum += 1
            elif event.key == pygame.K_UP:
                curser.row -= 1
            elif event.key == pygame.K_DOWN:
                curser.row += 1
            elif event.key == pygame.K_SPACE:
                print(curser.row, curser.colum)
                if curser.Error != True:
                    writearray(curser.blockvalue, curser.row, curser.colum)
            elif event.key == pygame.K_p:
                print(Level)
            elif event.key == pygame.K_c:
                print(curser.Error)
            elif event.key == pygame.K_q:
                curser.blockvalue += 1
            elif event.key == pygame.K_e:
                curser.blockvalue -= 1
            elif event.key == pygame.K_r:
                cleararray(curser.row, curser.colum)
                 
        
    if curser.row >= 20:
        curser.row = 0
    elif curser.row < 0:
        curser.row = 19

    if curser.colum >= 32:
        curser.colum = 0
    elif curser.colum < 0:
        curser.colum = 31


        
    
    




    #Unimportant
    
    everything.update()

    screen.fill(black)
    everything.draw(screen)

    while xlines < width or ylines < (height - 224):
        pygame.draw.line(screen, white, (xlines, 0), (ylines, (height - 224)))
        if ylines <= 800:
            pygame.draw.line(screen, white, (0, ylines), (width, ylines))
        xlines += 40
        ylines += 40
    xlines = 40
    ylines = 40

    curser.Error = False
    
    pygame.display.flip()

    clock.tick(60)
