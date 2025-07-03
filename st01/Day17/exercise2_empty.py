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
    global x, y, w, e
    x = 80
    y = 80
    global w, e
    w = 900
    e = 80

def every_frame():
    global x, y, w, e
    clear()
    draw_circle(50, x, y)
    x += 1
    y += 1
    draw_circle(80,w,e, (0,255,0))
    w -= 1
    e += 1

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
