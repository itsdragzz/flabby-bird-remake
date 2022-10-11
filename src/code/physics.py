import pygame
import code

class Falling():
    def __init__(self, player):
        
        self.dx = 0
        self.dy = 0

        self.falling_rate = 5
        
        self.press = False

            


'''
    def gravity(self, dt):
        self.direction += self.gravity * dt
        self.pos.y += self.direction * dt
        self.rect.y = round(self.pos.y)

    def jump(self):
        self.jump_sound.play()
        self.direction = -400
'''