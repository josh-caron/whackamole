import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        def empty_screen():
            screen.fill("light green")
            # Horizontal lines
            for i in range(20):
                pygame.draw.line(screen, "black", (32 * i, 0), (32 * i, 512))
            # Vertical lines
            for j in range(16):
                pygame.draw.line(screen, "black", (0, 32 * j), (640, 32 * j))
        empty_screen()
        screen.blit(mole_image, mole_image.get_rect(topleft=(4, 4)))

        clock = pygame.time.Clock()
        running = True
        x, y = 0, 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                        print(event.pos[0]//32, event.pos[1]//32, x, y)
                        if event.pos[0]//32 == x and event.pos[1]//32 == y:
                            empty_screen()
                            x = random.randrange(0, 21)
                            y = random.randrange(0, 17)
                            screen.blit(mole_image, mole_image.get_rect(topleft=(x*32,y*32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
