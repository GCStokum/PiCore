#v.0.1.0

'''
ALMOST a self contained "Worm" or Tron like game that's implemented in CORE
'''

import pygame
import Colors as rgb

class Worm:
    ''' A Worm '''

    def __init__(self, surface, x, y, z, length):
        self.surface = surface
        self.x = x
        self.y = y
        self.z = 0
        self.length = length
        self.dir_x = 0
        self.dir_y = 0
        self.dir_z = 0
        self.body = []
        self.crashed = False

    def key_event(self, event):  # Handle key events that affect the worm entity
        if event.key == pygame.K_UP:  # OR controller Up
            self.dir_x = self.dir_z = 0
            self.dir_y = -1  # Y at -1 is "Up" on screen
        elif event.key == pygame.K_RIGHT:  # OR controller Right
            self.dir_x = 1  # X at +1 is "Right" on screen
            self.dir_y = self.dir_z = 0
        elif event.key == pygame.K_DOWN:  # OR controller Down
            self.dir_x = self.dir_Z = 0
            self.dir_y = 1  # Y at +1 is "Down" on screen
        elif event.key == pygame.K_LEFT:  # OR controller Left
            self.dir_x = -1  # X at -1 is "Right" on screen
            self.dir_y = self.dir_z = 0
        elif event.key == pygame.K_a:
            self.dir_x = self.dir_y = 0
            self.dir_z = 0 # 1 or -1 once z implemented, for now "Pauses" move
        elif event.key == pygame.K_z:
            self.dir_x = self.dir_y = 0
            self.dir_z = 0 # 1 or -1 once z implemented, for now "Pauses" move
            
    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y
        self.z += self.dir_z

        if (self.x, self.y, self.z) in self.body:
            self.crashed = True

        self.body.insert(0, (self.x, self.y))  # TODO self.z

        if len(self.body) > self.length:
            self.body.pop()

    def draw(self):
        for x, y in self.body:
            self.surface.set_at((x, y), (rgb.black))
            self.surface.set_at((x+1, y), (rgb.black))
            self.surface.set_at((x-1, y), (rgb.black))
            self.surface.set_at((x, y+1), (rgb.black))
            self.surface.set_at((x, y-1), (rgb.black))
            #pygame.display.flip()
