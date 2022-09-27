import pygame, code
from random import randint

class Blocks(pygame.sprite.Sprite):
    def __init__(self, screen):

        self.x_coord = 1000
        self.y_coord = 700

        # Creating image for the block and then scale it
        self.image = pygame.image.load("src/graphics/pole.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 700))

        # Creating rectangles for images (for placement)
        self.rect = self.image.get_rect(center = (self.x_coord,self.y_coord))


        code.Display(screen, self.image, self.rect)