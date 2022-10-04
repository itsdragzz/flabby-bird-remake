import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        super().__init__()

        self.pipe_gap = 150
        self.image = pygame.image.load("src/graphics/pole.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 500))
        
        # position 1 is from the top, -1 is from the bottom
        if (pos == 1):
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(bottomleft = (x, y - int(self.pipe_gap/2)))
        else:
            self.rect = self.image.get_rect(topleft = (x, y + int(self.pipe_gap/2)))
    
    def destroy(self):
        if (self.rect.right < 0):
            self.kill() #kills kevin

    def update(self):
        self.rect.x -= 10 #speed of block
        self.destroy()