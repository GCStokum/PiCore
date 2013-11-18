                                                                               #
#v.0.0.005
# Hello, This is an entry into my own Python based, RPi intended (to start with
# open and free game framework
# and will probably be a start point for a colaborative series.


# also, MIT license <here> :P

#import antigravity

import pygame
import random

random.seed()
print('Hello.')

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))

topLeft = (1, 1)
bottomLeft = (1 , screenHeight - 1)
topRight = (screenWidth - 1, 1)
bottomRight = (screenWidth - 1, screenHeight -1)

black = (0, 0, 0)
grey50 = (127, 127, 127)
white = (255, 255, 255)
maroon = (127, 0, 0)
red = (255, 0, 0)
green = (0, 127, 0)
lime = (0, 255, 0)
teal = (0, 0, 127)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

running = True

bgColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

y = 0
dir = 1

"Doing some stuff and things"
while running == True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        print('Good bye!')
        running = False

    screen.fill(bgColour)

    x = 0
    while x <= screenWidth:
        pygame.draw.line(screen, (red), (bottomLeft), (x, 0))
        pygame.draw.line(screen, (blue), (bottomRight), (x, 0))
        pygame.draw.line(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (screenWidth / 2, screenHeight), (x, 0))
        x += 2
        pygame.display.flip()

"Done doing stuff and things"
