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
name = ""

num = 1
#collum = 0
alphabet = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y" , "z", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
white = (255, 255, 255)
black = (0, 0, 0)

everything = pygame.sprite.Group()
keyboards = pygame.sprite.Group()
keyboardanimation = []

for i in range(81):
    legacy0 = "Sprites/Keyboard/Itteration" + str(i) + ".png"
    keyboardanimation.append(legacy0)

class parent(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()
         self.xcord = 0
         self.ycord = 0
         everything.add(self)

class Keyboard(parent):
    def __init__(self):
        super().__init__()
        self.xcord = 200
        self.ycord = 200
        self.image = pygame.image.load(keyboardanimation[1])
        self.rect = self.image.get_rect()
        keyboards.add(self)


keyboard = Keyboard()



while True:
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN: #handles all keypresses
            if event.key == pygame.K_LEFT: #move left
                num -= 1
            elif event.key == pygame.K_RIGHT: #move right
                num += 1
            elif event.key == pygame.K_UP:
                num -= 10
            elif event.key == pygame.K_DOWN:
                num += 10
            if event.key == pygame.K_SPACE:
                if (capital == False and num < 38):
                    name = name + alphabet[num]
                elif capital == True and num < 38:
                    name = name + alphabet[num + 37]
                    capital = False
                elif num == 38:
                    if capital == False:
                        capital = True
                    else:
                        capital = False
                elif num == 39:
                    name = name[:-1]
                elif num == 40:
                    print(name)

              
    if num > 40:
        num = num - 40 
    elif num < 1:
        num = 40 + num

    if capital == False:
        keyboard.image = pygame.image.load(keyboardanimation[num])
    elif capital == True:
        keyboard.image = pygame.image.load(keyboardanimation[num + 27])
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

    
        
                
