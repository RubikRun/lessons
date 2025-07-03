import pygame
import random
import pygame.gfxdraw

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
BACKGROUND_COLOR = [30, 30, 30]

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# === Helper Functions ===

def draw_circle(radius, px, py, color = [255, 0, 0]):
    pygame.gfxdraw.filled_circle(screen, px, py, radius, color)
    pygame.gfxdraw.aacircle(screen, px, py, radius, color)

def hits_left(circle):
    radius, px, _, _, _, _ = circle
    return px - radius <= 0

def hits_right(circle):
    radius, px, _, _, _, _ = circle
    return px + radius >= WINDOW_WIDTH

def hits_top(circle):
    radius, _, py, _, _, _ = circle
    return py - radius <= 0

def hits_bottom(circle):
    radius, _, py, _, _, _ = circle
    return py + radius >= WINDOW_HEIGHT

def clear():
    screen.fill(BACKGROUND_COLOR)




def at_the_beginning():
    ...

def every_frame():
    ...




at_the_beginning()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    every_frame()

    pygame.display.flip()
    clock.tick(60)




pygame.quit()
