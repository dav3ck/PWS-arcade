import pygame

withd = 1000
height = 800

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((withd,height))
screen_rect=screen.get_rect()
pygame.display.set_caption("Keyboard")
clock = pygame.time.Clock()

capital = False
name = "" #List with your name in it

num = 1 #Variable die aangeeft welke letter we nu op zitten
#Array met alle toetsen erin
alphabet = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y" , "z", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
white = (255, 255, 255)
black = (0, 0, 0)

everything = pygame.sprite.Group() #Your everything group
keyboards = pygame.sprite.Group() #Keyboard sprite group, IDK If necessary
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
        self.image = pygame.image.load(keyboardanimation[1])
        self.rect = self.image.get_rect()
        keyboards.add(self)


keyboard = Keyboard() #Keyboard list IDK if necessary



while True:
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN: #handles all keypresses
            if event.key == pygame.K_LEFT: 
                num -= 1
            elif event.key == pygame.K_RIGHT:
                num += 1
            elif event.key == pygame.K_UP:
                num -= 10
            elif event.key == pygame.K_DOWN:
                num += 10
            if event.key == pygame.K_SPACE:
                if (capital == False and num < 38): 
                    name = name + alphabet[num] #adds letter to list with name 
                elif capital == True and num < 38:
                    name = name + alphabet[num + 37] #adds Capital letter to name list
                    capital = False #Zet capital terug naar false > je print no longer Capitals
                elif num == 38:
                    if capital == False: #Zet capital naar true, tenzij het al true is, dan zet het het terug naar False
                        capital = True
                    else:
                        capital = False
                elif num == 39: #Haalt een letter weg
                    name = name[:-1]
                elif num == 40: #Print je naam/ Dit is de plek waar je de name uitput
                    print(name)

                    
    # DIT KAN DENK IK OOK IN EEN KEYBOARD/ UPDATE CLASS
              
    if num > 40: #Zorgt ervoor dat het tussen de 1 tm 40 blijft
        num = num - 40 
    elif num < 1:
        num = 40 + num
        
    #Handeld alle sprites
    
    if capital == False: 
        keyboard.image = pygame.image.load(keyboardanimation[num])
    elif capital == True:
        keyboard.image = pygame.image.load(keyboardanimation[num + 37])
    keyboard.rect = keyboard.image.get_rect()
        
    #print de text bottom right
    numtext = myfont.render(str(num), False, white)
    nametext = myfont.render(name, False, white)

    #screen management
    screen.fill(black)

    screen.blit(numtext, (400,700))
    screen.blit(nametext, (800, 700))

    everything.draw(screen)
                            
    pygame.display.flip()

    clock.tick(30)

    
        
                
