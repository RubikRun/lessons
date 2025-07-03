import pygame
import random
import pygame.gfxdraw

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
SPEED_LIMIT = 3
N = 100

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# === Helper Functions ===

def random_circle():
    radius = random.randint(10, 30)
    x = random.randint(radius, WINDOW_WIDTH - radius)
    y = random.randint(radius, WINDOW_HEIGHT - radius)
    sx = random.randint(-SPEED_LIMIT, SPEED_LIMIT)
    sy = random.randint(-SPEED_LIMIT, SPEED_LIMIT)
    color = [random.randint(0, 255) for _ in range(3)]
    return [radius, x, y, sx, sy, color]

def draw_circle(circle):
    radius, x, y, _, _, color = circle
    pygame.gfxdraw.filled_circle(screen, x, y, radius, color)
    pygame.gfxdraw.aacircle(screen, x, y, radius, color)

def hits_left(circle):
    radius, x, _, _, _, _ = circle
    return x - radius <= 0

def hits_right(circle):
    radius, x, _, _, _, _ = circle
    return x + radius >= WINDOW_WIDTH

def hits_top(circle):
    radius, _, y, _, _, _ = circle
    return y - radius <= 0

def hits_bottom(circle):
    radius, _, y, _, _, _ = circle
    return y + radius >= WINDOW_HEIGHT

# === Create the list of circles ===
circles = []

# === Create circles and add them to the "circles" list
for i in range(N):
    ccc = random_circle()
    circles.append(ccc)

# === Main Game Loop ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    # === Draw circles ===
    for i in range(N):
        draw_circle(circles[i])

    # === Move circles ===
    for i in range(N):
        circles[i][1] += circles[i][3]
        circles[i][2] += circles[i][4]

    for i in range(N):
        if hits_left(circles[i]) or hits_right(circles[i]):
            circles[i][3] = -circles[i][3]
        if hits_top(circles[i]) or hits_bottom(circles[i]):
            circles[i][4] = -circles[i][4]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
