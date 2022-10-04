import pygame, sys, code, random

def run():
    pygame.init()


    clock = pygame.time.Clock()

    # Obstacle timer, spawns a new pipe column every second

    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 1000)

    # Declare screen settings from external file
    screen_dimension = code.Settings()
    screen = pygame.display.set_mode((screen_dimension.screen_width, screen_dimension.screen_height))

    # Declare the obstacle group
    obstacle_group = pygame.sprite.Group()

    while True:
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            
            if (event.type == obstacle_timer):
                pipe_height = random.randint(-200,200)
                # Adding a top pipe into the obstacle class
                obstacle_group.add(code.Block(screen_dimension.screen_width, int(screen_dimension.screen_height/2) + pipe_height, 1))
                # Adding a bottom pipe into the obstacle class
                obstacle_group.add(code.Block(screen_dimension.screen_width, int(screen_dimension.screen_height/2) + pipe_height, -1))

        screen.fill('pink')
        obstacle_group.draw(screen)
        obstacle_group.update()

        pygame.display.update()

        clock.tick(60)


    


if __name__ == '__main__':
    
    run()