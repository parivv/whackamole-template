import pygame
import random

"""def draw_grid():
    for i in range(0,640,32):
        pygame.draw.line(screen, (0,0,0), (i, 0), (i, 512))
    for j in range(0, 512, 32):
        pygame.draw.line(screen, (0, 0, 0), (0, j), (640, j))"""


def main():
    try:
        pygame.init()

        def new_pos():
            x = random.randrange(0, cols) * 32
            y = random.randrange(0, rows) * 32
            return x, y

        def draw_grid():
            for i in range(0, 640, 32):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 512))
            for j in range(0, 512, 32):
                pygame.draw.line(screen, (0, 0, 0), (0, j), (640, j))

        rows = 16
        cols = 20
        molx, moly = (0, 0)

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos
                    if(x < (molx + 32)) and (y < (moly + 32)):
                        molx, moly = new_pos()

            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(topleft=(molx, moly)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
