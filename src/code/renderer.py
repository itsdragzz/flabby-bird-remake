import pygame 

class Display():
    
    '''
    Render images
    '''
    
    def __init__(self, screen, image, image_rect):
        screen.blit(image, image_rect)

        
