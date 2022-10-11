import pygame
import code
import sys


class Run():
    def __init__(self) -> str:
        screen_dimension = code.Settings()
        screen = pygame.display.set_mode((screen_dimension.screen_width, screen_dimension.screen_height))

        while True:
            
            
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()

            pygame.display.update()