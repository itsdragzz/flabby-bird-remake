import pygame 

class Display():
    
    def __init__(self, image, screen):
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.image_resize = pygame.transform.scale(image, (1280, 720))
        screen.blit(image, self.rect)

        
