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

def hits_left(radius, px, py):
    return px - radius <= 0

def hits_right(radius, px, py):
    return px + radius >= WINDOW_WIDTH

def hits_top(radius, px, py):
    return py - radius <= 0

def hits_bottom(radius, px, py):
    return py + radius >= WINDOW_HEIGHT

def clear():
    screen.fill(BACKGROUND_COLOR)




def at_the_beginning():
    global x, y, sx, sy
    x = 80
    y = 80
    sx = 1
    sy = 1

def every_frame():
    global x, y, sx, sy
    clear()
    draw_circle(50, x, y)
    x += sx
    y += sy

    if hits_bottom(50, x, y):
        sy = -sy
    if hits_top(50, x, y):
        sy = -sy
    if hits_left(50, x, y):
        sx = -sx
    if hits_right(50, x, y):
        sx = -sx




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
