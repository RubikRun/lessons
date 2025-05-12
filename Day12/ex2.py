import pygame
import pygame.gfxdraw
import sys

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = (30, 30, 30)
CIRCLE_COLOR = (200, 200, 255)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Day 12")
clock = pygame.time.Clock()

# Store all clicked positions
click_positions = []

def circle(x, y, radius):
    pygame.gfxdraw.aacircle(screen, x, y, radius, CIRCLE_COLOR)











def draw(mouseX, mouseY):
    for r in range(20):
        circle(mouseX, mouseY, r*10)











def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                click_positions.append((x, y))

        screen.fill(BACKGROUND_COLOR)

        for pos in click_positions:
            draw(pos[0], pos[1])

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
