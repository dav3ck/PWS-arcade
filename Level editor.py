import pygame
pygame.init()
import math

#Variable

width = 1280
height = 1024

xlines = 40
ylines = 40

name = ''
keyboard = 0
editor_colum = 1


    #Variable Colors

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0,0,255)
yellow = (140, 0,140)

#Screen setup

screen = pygame.display.set_mode((width,height))
screen_rect=screen.get_rect()
pygame.display.set_caption('Level editor')
clock = pygame.time.Clock()

font = pygame.font.Font(None, 32)

#Level array setup
row = []
colum = []
Level = []
for y in range(21):
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
        self.xsize = 160
        self.ysize = 120
        self.color = green
        self.image = pygame.Surface([self.xsize,self.ysize])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.colum = 0
        self.row = 0
        self.blockvalue = 9
        self.blocksize = True
        self.Error = False



    def update(self):


        self.image = pygame.Surface([self.xsize,self.ysize])

        if self.Error == True:
            self.image.fill(red)
        else:
            self.image.fill(blue)

        self.rect = self.image.get_rect()
        
        self.xcord = self.colum * 40
        self.ycord = self.row * 40

        self.rect.y = self.ycord
        self.rect.x = self.xcord
        


class Block(parent):
    def __init__(self, x, y, color, row, colum):
        super().__init__()
        self.xsize = x
        self.ysize = y
        self.row = row
        self.colum = colum
        self.color = color
        self.image = pygame.Surface([self.xsize,self.ysize])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def update(self):

        self.xcord = self.colum * 40
        self.ycord = self.row * 40 

        self.rect.y = self.ycord
        self.rect.x = self.xcord
        

#functies

#Deze functie plaats de code
        
def writearray(value, row, colum):
 
    Level[0][row][colum] = value
    if value == 8:
        for x in range(2):
            for y in range(2):
                if x != 0 or y != 0:
                    Level[0][row + x][colum + y] = 'a'

    elif value == 9:
        for x in range(3):
            for y in range(4):
                if x != 0 or y != 0:
                    Level[0][row + x][colum + y] = 'a'

#Deze functie verwijderd de code

def cleararray(row, colum):
    value = Level[0][row][colum]
    
    if type(value != float):
        Level[0][row][colum] = 0
    
        if value == 8:
            for x in range(2):
                for y in range(2):
                    if x != 0 or y != 0:
                        Level[0][row + x][colum + y] = 0

        elif value == 9:
            for x in range(3):
                for y in range(4):
                    if x != 0 or y != 0:
                        Level[0][row + x][colum + y] = 0
                    
#De check functie checked of iets geplaatst kan worden!

def check(value, row, colum):
    Error = False

    if value == 8:
        for x in range(2):
            for y in range(2):
                if row + x < 0 or colum + y > 31 or type(Level[0][row + x][colum + y]) is str or Level[0][row + x][colum + y] != 0 or Level[0][row + x][colum + y] == 9:
                    Error = True
                    
    elif value == 9:
        for x in range(3):
            for y in range(4):
                if row + x < 0 or colum + y > 31 or type(Level[0][row + x][colum + y]) is str or Level[0][row + x][colum + y] != 0 or Level[0][row + x][colum + y] == 9:
                    Error = True
    else:
        if Level[0][row][colum] != 0:
            Error = True
    return Error


def movement():
    curser.Error = False
    if curser.blockvalue == 8:
        curser.xsize = 80
        curser.ysize = 80
    elif curser.blockvalue == 9:
        curser.xsize = 160
        curser.ysize = 120
    else:
        curser.xsize = 40
        curser.ysize = 40

    if curser.blockvalue >= 7 and curser.blockvalue <= 9:
        curser.color = green
    elif curser.blockvalue == 6:
        curser.color = white
    else:
        curser.color = yellow

    offscreen()
    curser.Error = check(curser.blockvalue, curser.row, curser.colum)
    
def offscreen():
    if curser.row > 21 - int(curser.ysize / 40) :
        curser.row = 0
    elif curser.row < 0:
        curser.row = 21 - int(curser.ysize / 40)
    if curser.colum > 32 - int(curser.xsize / 40):
        curser.colum = 0 
    elif curser.colum < 0:
        curser.colum = 32 - int(curser.xsize / 40)

def editor_value(editor_colum):
    if editor_colum != 0:
        curser.blockvalue = editor_colum

    

#Aanroepingen

curser = Curser()

        
#Echte spel

while True:

    movement()

    if keyboard == 0:
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
                        block = Block(curser.xsize, curser.ysize, curser.color, curser.row, curser.colum)
                elif event.key == pygame.K_p:
                    print(curser.colum, curser.row)
                elif event.key == pygame.K_c:
                    print(curser.Error)
                elif event.key == pygame.K_q:
                    curser.blockvalue += 1
                    print(curser.blockvalue)
                elif event.key == pygame.K_e:
                    keyboard = 1
                    print(curser.blockvalue)
                elif event.key == pygame.K_r:
                    cleararray(curser.row, curser.colum)
                elif event.key == pygame.K_s:
                    with open('Levels.txt', 'a') as f:
                        f.write(name + "\n")
                        for x in range(21):
                            for y in range(32):
                                f.write(str(Level[0][x][y]))
                            f.write("\n")
                            
                            
                        
    elif keyboard == 1:
        for event in pygame.event.get(): #handles closing the window
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    keyboard = 0
                    editor_value(editor_colum)
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_LEFT:
                    editor_colum -= 1
                    print(editor_colum)
                elif event.key == pygame.K_RIGHT:
                    editor_colum += 1
                    print(editor_colum)
                else:
                    if len(name) < 20:
                        name += event.unicode


    
    if editor_colum > 10:
        editor_colum = 0
    elif editor_colum < 0:
        editor_colum = 10


        
                
    

 
                 


    #Unimportant
    
    everything.update()

    screen.fill(black)

    txt_surface = font.render(name, True, red)
    screen.blit(txt_surface, (0, 0))
    
    everything.draw(screen)

    while xlines < width or ylines < (height - 184):
        pygame.draw.line(screen, white, (xlines, 0), (ylines, (height - 184)))
        if ylines <= 840:
            pygame.draw.line(screen, white, (0, ylines), (width, ylines))
        xlines += 40
        ylines += 40
    xlines = 40
    ylines = 40

   
    pygame.display.flip()

    clock.tick(60)
