import pygame

withd = 1000
height = 800

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((withd,height))
screen_rect=screen.get_rect()
pygame.display.set_caption("Keyboard")
clock = pygame.time.Clock()

#Array met alle toetsen erin
white = (255, 255, 255)
black = (0, 0, 0)

everything = pygame.sprite.Group() #Your everything group

keyboardanimation = [] #Array met alle Keyboard sprites erin

for i in range(81): #Zelfde als voor slime animatie sprites alleen dit keer kleiner 
    legacy0 = "Sprites/Keyboard/Itteration" + str(i) + ".png"
    keyboardanimation.append(legacy0)

class parent(pygame.sprite.Sprite): #Jouw standaard parent class
    def __init__(self):
         super().__init__()
         self.xcord = 0
         self.ycord = 0
         everything.add(self)

class Keyboard(parent): #Keyboard class
    def __init__(self):
        super().__init__()
        self.xcord = 200
        self.ycord = 200
        self.num = 1
        self.image = pygame.image.load(keyboardanimation[1])
        self.rect = self.image.get_rect()
        self.capital = False
        self.name = ""
        self.alphabet = (" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y" , "z", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

    def update(self):
        if self.num > 40: #Zorgt ervoor dat het tussen de 1 tm 40 blijft
            self.num = self.num - 40 
        elif self.num < 1:
            self.num = 40 + self.num
        if self.capital == False: 
            keyboard.image = pygame.image.load(keyboardanimation[self.num])
        elif self.capital == True:
            keyboard.image = pygame.image.load(keyboardanimation[self.num + 37])


keyboard = Keyboard() #Initiates keyboard



while True:
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN: #handles all keypresses
            if event.key == pygame.K_LEFT: 
                keyboard.num -= 1
            elif event.key == pygame.K_RIGHT:
                keyboard.num += 1
            elif event.key == pygame.K_UP:
                keyboard.num -= 10
            elif event.key == pygame.K_DOWN:
                keyboard.num += 10
            if event.key == pygame.K_SPACE:
                if (keyboard.capital == False and keyboard.num < 38): 
                    keyboard.name = keyboard.name + keyboard.alphabet[keyboard.num] #adds letter to list with name 
                elif keyboard.capital == True and keyboard.num < 38:
                    keyboard.name = keyboard.name + keyboard.alphabet[keyboard.num + 37] #adds Capital letter to name list
                    capital = False #Zet capital terug naar false > je print no longer Capitals
                elif keyboard.num == 38:
                    if keyboard.capital == False: #Zet capital naar true, tenzij het al true is, dan zet het het terug naar False
                        keyboard.capital = True
                    else:
                        keyboard.capital = False
                elif keyboard.num == 39: #Haalt een letter weg
                    keyboard.name = keyboard.name[:-1]
                elif keyboard.num == 40: #Print je naam/ Dit is de plek waar je de name uitput
                    print(keyboard.name)

                    


    everything.update()
        
    #print de text bottom right
    numtext = myfont.render(str(keyboard.num), False, white) #this is just a check
    nametext = myfont.render(keyboard.name, False, white) #prints the name

    #screen management
    screen.fill(black)

    screen.blit(numtext, (400,700))
    screen.blit(nametext, (800, 700))

    everything.draw(screen)
                            
    pygame.display.flip()

    clock.tick(30)

    
        
                
