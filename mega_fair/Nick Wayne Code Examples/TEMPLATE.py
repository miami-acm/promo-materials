import pygame

def run():
    pygame.init()

    size = (640, 480)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    done = False

    while not done:
        time_passed_seconds = clock.tick(120)/1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True


        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    run()