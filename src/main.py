import pygame
import sys
import code 


def run():

    pygame.init()

    screen_dimension = code.Settings()

    screen = pygame.display.set_mode((screen_dimension.screen_width, screen_dimension.screen_height))


    while True:
        
        code.Blocks()
        code.Player(screen)
        
        code.Player
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    run()