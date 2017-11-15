import pygame

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

screen = pygame.display.set_mode((width,height))
screen_rect=screen.get_rect()
pygame.display.set_caption('Level editor')
clock = pygame.time.Clock()

Level = []
for x in range(100):
    Level.append(0)

  
#vakjes 40p x 40p dus 32 breed en 25 hoog

while True:
    for event in pygame.event.get(): #handles closing the window
        if event.type == pygame.QUIT:
            pygame.quit()


    while xlines < width or ylines < (height - 224):
        pygame.draw.line(screen, white, (xlines, 0), (ylines, (height - 224)))
        if ylines <= 800:
            pygame.draw.line(screen, white, (0, ylines), (width, ylines))
        xlines += 40
        ylines += 40
    xlines = 40
    ylines = 40


    pygame.display.flip()

    clock.tick(60)
