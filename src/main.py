import pygame
import sys
import code 


def run():
    pygame.init()

    screen_dimension = code.Settings()
    screen = pygame.display.set_mode((screen_dimension.screen_width, screen_dimension.screen_height))


    obstacle_group = pygame.sprite.Group()
    obstacle_group.add(code.Top_Block())
    obstacle_group.add(code.Bottom_Block())


    while True:
        
        obstacle_group.draw(screen)
        obstacle_group.update()
        # code.Player(screen)
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()


        pygame.display.update()


if __name__ == '__main__':
    run()