                                                                               #
#v.0.1.015
# Hello, This is an entry into my own Python based, RPi intended (to start with
# open and free game framework
# and will probably be a start point for a colaborative series.


# also, MIT license <here> :P

#import antigravity

import pygame
import random as r
import Colors as rgb
import Vectors as v

import Worm

# Primary Engine Bits
Debug = True
running = True
myMousePos = myMouseClick = (0, 0)
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

pygame.font.init()  # Needed if no pygame.init() safe to call multiple times
# Select the font to use. Default font, 25 pt size.
font = pygame.font.Font(None, 25)

# Secondary
Up = (0, -1)
Down = (0, 1)
Left = (-1, 0)
Right = (1, 0)

topLeft = (1, 1)
bottomLeft = (1 , screenHeight - 1)
topRight = (screenWidth - 1, 1)
bottomRight = (screenWidth - 1, screenHeight -1)

bgColour = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))

r.seed()


# TODO : define entity (enemy / player)  this will then be transfered to Entity.py or some such file
class entity:
    def __init__(self):pass

    def feed(self, e):
        # self is now +e's nutrition etc.
        print('Nom!')

    def purge(self, e):
        print('Burp!')
        
    def die(self):
        print('Goodbye Cruel World!')


def kill(e):
    if e is entity:
        e.die()


def draw(entity):
    # Blah
    pass

# Let's start doing some stuff
print('Hello.')
while running:

    ''' INPUT / CONTROL Below '''
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('Up')                
            elif event.key == pygame.K_DOWN:
                print('Down')
            elif event.key == pygame.K_LEFT:
                print('Left')
            elif event.key == pygame.K_RIGHT:
                print('Right')
        else:
            print (event.type)  # Whatelse is going on here?

    clock.tick(250)  # Let our CPU rest and do other things for a few cycles
    ''' INPUT / CONTROL Above '''

    
    ''' LOGIC Below '''

    ''' LOGIC Above '''

    
    ''' DISPLAY / OUTPUT Below '''
    screen.fill(bgColour)

    '''
    # Set Pixel Color at point
    x = r.randint(0, screenWidth-1)
    y = r.randint(0, screenHeight-1)
    screen.set_at((x, y), (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))
    '''

    pygame.draw.line(screen, (rgb.red), (bottomLeft), (myMousePos),2)
    pygame.draw.line(screen, (rgb.blue), (bottomRight), (myMousePos),2)
    pygame.draw.line(screen, (r.randint(0,255),r.randint(0,255),r.randint(0,255)), (screenWidth / 2, screenHeight), (myMouseClick),3)

    if Debug == True:
        # Render the text. "True" means anti-aliased text. 
        # Black is the color. This creates an image of the 
        # letters, but does not put it on the screen
        text = font.render("Pointer @ " + str(myMousePos), True, rgb.yellow)
        # this is how to concatinate string bits :
        # text = font.render("Score: "+str(score),True,black)

        # Put the image of the text on the screen at x and y
        screen.blit(text, [5,5])
    
        text = font.render("Clicked @ " + str(myMouseClick), True, rgb.yellow)
        screen.blit(text, [5,30])

    # Blit the screen as final part of Display
    pygame.display.flip()
    ''' DISPLAY / OUTPUT Above '''
