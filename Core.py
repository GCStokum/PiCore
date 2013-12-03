                                                                               #
#v.0.2.05
# Hello, This is an entry into my own Python based, RPi intended (to start with
# open and free game framework
# and will probably be a start point for a colaborative series.

# also, MIT license <here> :P

#import antigravity
import pygame
import random as r
import Colors as rgb
import Vectors as v

WormGame = False
if WormGame:
    import Worm as w

# Primary Engine Bits
Debug = True
running = True
myMousePos = myMouseClick = (0, 0)
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

pygame.init()

joystick_count = pygame.joystick.get_count()
print ("There is ", joystick_count, "joystick/s")
if joystick_count == 0:
    print ("Error, I did not find any joysticks")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

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

#Game specifics here
if WormGame:
    myW = w.Worm(screen, 400, 300, 0, 200)  # (screen, x, y, z, length)

"BLAH BLAH BLAH"
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
"BLAH BLAH BLAH"


# Let's start doing some stuff
print('Hello.')

while running:
    if WormGame:
        myW.move()
        myW.draw()

    ''' ##################### '''
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

            if WormGame:
                myW.key_event(event)  # CONTROL to WORM

            if event.key == pygame.K_UP:
                print('Up')                
            elif event.key == pygame.K_DOWN:
                print('Down')
            elif event.key == pygame.K_LEFT:
                print('Left')
            elif event.key == pygame.K_RIGHT:
                print('Right')
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button : ", event)
        #elif event.type == pygame.JOYBUTTONUP:
            #print("Joystick button released.")
        else:
            print (event.type)  # What else is going on here?

    clock.tick(50)  # Let our CPU rest and do other things for a few cycles
    ''' INPUT / CONTROL Above '''
    ''' #####################  '''

    ''' ########### '''
    ''' LOGIC Below '''
    if WormGame:
        if myW.crashed or myW.x <= 0 or myW.x >= screenWidth - 1 or myW.y <= 0 or myW.y >= screenHeight - 1:
            print ("Crash!")
            running = False
    ''' LOGIC Above '''
    ''' ########### '''

    ''' ###################### '''
    ''' DISPLAY / OUTPUT Below '''
    screen.fill(bgColour)

    '''
    # Set Pixel Color at point
    x = r.randint(0, screenWidth-1)
    y = r.randint(0, screenHeight-1)
    screen.set_at((x, y), (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)))
    '''

    if Debug:
        pygame.draw.line(screen, (rgb.red), (bottomLeft), (myMousePos),2)
        pygame.draw.line(screen, (rgb.blue), (bottomRight), (myMousePos),2)
        pygame.draw.line(screen, (r.randint(0,255),r.randint(0,255),r.randint(0,255)), (screenWidth / 2, screenHeight), (myMouseClick),3)
    
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
    ''' ###################### '''
