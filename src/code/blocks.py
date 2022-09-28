import pygame
from random import randint, seed
from datetime import datetime


class Top_Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.count = 1
        image = pygame.image.load("src/graphics/pole.png").convert_alpha()
        image = pygame.transform.scale(image, (150, 500))
        self.image = pygame.transform.rotozoom(image, 180, 1)

        self.rect = self.image.get_rect(bottomleft = (500, self.x()))
    
    def x(self):
        seed(self.count)
        self.x_coord = randint(100, 400)
        self.count += 1
        return(self.x_coord)

class Bottom_Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image_gap = 100
        a = Top_Block()
        self.x_coord = a.x()

        image = pygame.image.load("src/graphics/pole.png").convert_alpha()
        self.image = pygame.transform.scale(image, (150, 500))
        
        self.rect = self.image.get_rect(topleft = (500, self.x_coord + self.image_gap))