import pygame
import code

class Player():
    """
    Create a player
    """

    def __init__(self, screen):
        # pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load("src/graphics/bird.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (1280, 720))
        self.rect = self.image.get_rect(topleft = (0, 0))


        code.Display(screen, self.image, self.rect)

            

        def x(self):

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pass
    
