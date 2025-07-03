import pygame
import random
import pygame.gfxdraw

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SPEED_LIMIT = 3
N = 100

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()








# === Helper Functions ===


# Creates a random circle.
# How to use? Do this:
#     c = random_circle()
# and now the variable "c" will contain a random circle.
#
# What exactly is that circle?
# It's a list of 6 elements:
#         0     1  2  3   4     5
#     [ radius, x, y, sx, sy, color ]
# "sx" and "sy" are the x-speed and y-speed of the circle
def random_circle():
    radius = random.randint(10, 30)
    x = random.randint(radius, WINDOW_WIDTH - radius)
    y = random.randint(radius, WINDOW_HEIGHT - radius)
    sx = random.randint(-SPEED_LIMIT, SPEED_LIMIT)
    sy = random.randint(-SPEED_LIMIT, SPEED_LIMIT)
    color = [random.randint(0, 255) for _ in range(3)]
    return [radius, x, y, sx, sy, color]

# Draws a circle on the screen.
# How to use? If you have a variable "c" that contains a circle, you can do this:
#     draw_circle(c)
# and the circle will appear on the screen.
def draw_circle(circle):
    radius, x, y, _, _, color = circle
    pygame.gfxdraw.filled_circle(screen, x, y, radius, color)
    pygame.gfxdraw.aacircle(screen, x, y, radius, color)

# Checks if a circle hits the left edge of the window.
# How to use? If you have a variable "c" that contains a circle, you can do this:
#     if hits_left(c):
#         ...
# and the "..." code will happen only if the circle hits the left edge.
def hits_left(circle):
    radius, x, _, _, _, _ = circle
    return x - radius <= 0

# Same as above
def hits_right(circle):
    radius, x, _, _, _, _ = circle
    return x + radius >= WINDOW_WIDTH

# Same as above
def hits_top(circle):
    radius, _, y, _, _, _ = circle
    return y - radius <= 0

# Same as above
def hits_bottom(circle):
    radius, _, y, _, _, _ = circle
    return y + radius >= WINDOW_HEIGHT





# You need to fill this section
def at_the_beginning():
    global circles
    circles = []

    # === Create circles and add them to the "circles" list
    # FILL HERE

# You need to fill this section
def every_frame():
    global circles
    # === Draw circles ===
    # FILL HERE

    # === Move circles ===
    # FILL HERE

    # === Handle bouncing ===
    # FILL HERE







at_the_beginning()

# === Main Game Loop ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    every_frame()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
