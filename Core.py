                                                                               #
#v.0.1.001
# Hello, This is an entry into my own Python based, RPi intended (to start with
# open and free game framework
# and will probably be a start point for a colaborative series.


# also, MIT license <here> :P

#import antigravity

import pygame
import random as r
import Colors as rgb

# Primary Engine Bits
running = True
myMousePos = myMouseClick = (0, 0)
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

# Secondary 
topLeft = (1, 1)
bottomLeft = (1 , screenHeight - 1)
topRight = (screenWidth - 1, 1)
bottomRight = (screenWidth - 1, screenHeight -1)

bgColour = (r.randint(0,255), r.randint(0,255), r.randint(0,255))

r.seed()


# Let's start doing some stuff
print('Hello.')
while running:

    ''' INPUT '''
    for event in pygame.event.get():  # Poll only on event instead of constantly
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
            print (event.type)  # Whatelse is going on here?

    clock.tick(250)  # Let our CPU rest and do other things for a few cycles

    
    ''' LOGIC '''
    
    ''' DISPLAY / OUTPUT '''
    screen.fill(bgColour)

    x = r.randint(0, screenWidth-1)
    y = r.randint(0, screenHeight-1)
    screen.set_at((x, y), (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))
    

    pygame.draw.line(screen, (rgb.red), (bottomLeft), (myMousePos))
    pygame.draw.line(screen, (rgb.blue), (bottomRight), (myMousePos))
    pygame.draw.line(screen, (r.randint(0,255),r.randint(0,255),r.randint(0,255)), (screenWidth / 2, screenHeight), (myMouseClick))

    pygame.display.flip()
