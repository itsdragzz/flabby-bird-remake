import pygame
import code

class Player():
    """
    Create a player
    """

    def __init__(self, screen):
        # pygame.sprite.Sprite.__init__(self)





        self.image = pygame.image.load("src/graphics/bird.png").convert()
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.image_resize = pygame.transform.scale(self.image, (1280, 720))
        code.Display(self.image, self.rect)

            

        def x(self):

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pass

