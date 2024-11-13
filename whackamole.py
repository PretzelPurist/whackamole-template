import random
import pygame

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_pix = (0, 0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_pix[0] <= event.pos[0] <= mole_pix[0] + 32 and mole_pix[1] <= event.pos[1] <= mole_pix[1] + 32:
                        mole_pix = (random.randrange(20)*32, random.randrange(16)*32)
            screen.fill("light green")
            for i in range(19):
                pygame.draw.line(screen, "black", (32*(i+1),0), (32*(i+1),512))
            for i in range(15):
                pygame.draw.line(screen, "black", (0, 32*(i+1)), (640, 32*(i+1)))
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pix))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
