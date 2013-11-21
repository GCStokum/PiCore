                                                                               #
#v.0.0.011
# Hello, This is an entry into my own Python based, RPi intended (to start with
# open and free game framework
# and will probably be a start point for a colaborative series.


# also, MIT license <here> :P

#import antigravity

import pygame
import random
import Colors as rgb

running = True
myMousePos = myMouseClick = (0, 0)
dir = 1

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))

topLeft = (1, 1)
bottomLeft = (1 , screenHeight - 1)
topRight = (screenWidth - 1, 1)
bottomRight = (screenWidth - 1, screenHeight -1)

bgColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

random.seed()


print('Hello.')
while running:

    ''' INPUT '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Goodbye!')
            running = False
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Mouse Click @', event.pos)
            myMouseClick = event.pos
        elif event.type == pygame.MOUSEMOTION:
            print('Mouse @', event.pos)
            myMousePos = event.pos
        else:
            print (event.type)
    '''
    "Old Event Loop"
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        print('Goodbye!')
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print ("Mouse Click @" , event.pos)
        myMouseClick = event.pos
    elif event.type == pygame.MOUSEMOTION:
        print ("Mouse @ " , event.pos)
        myMousePos = event.pos
    '''

    
    ''' DISPLAY '''
    screen.fill(bgColour)

    pygame.draw.line(screen, (rgb.red), (bottomLeft), (myMousePos))
    pygame.draw.line(screen, (rgb.blue), (bottomRight), (myMousePos))
    pygame.draw.line(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (screenWidth / 2, screenHeight), (myMouseClick))

    pygame.display.flip()
    
'''
import pygame
y = 0
dir = 1
running = 1
barheight = 124
screen = pygame.display.set_mode((800, 600));

barcolor = []
for i in range(1, 63):
    barcolor.append((0, 0, i*4))
for i in range(1, 63):
    barcolor.append((0, 0, 255 - i*4))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill((0, 0, 0))
    for i in range(0, barheight):
        pygame.draw.line(screen, barcolor[i], (0, y+i), (799, y+i))

    y += dir
    if y + barheight > 599 or y < 0:
        dir *= -1

    pygame.display.flip()
'''

