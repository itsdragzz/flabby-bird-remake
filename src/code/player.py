import pygame

class Player(pygame.sprite.Sprite):
    """
    Create a player
    """

    def __init__(self):
        super().__init__() 
        pygame.sprite.Sprite.__init__(self)

        # pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load("src/graphics/bird.png").convert_alpha()


        self.image = pygame.transform.scale(self.image, (150, 100))

        self.rect = self.image.get_rect(topleft = (0, 0))

        

        
        



