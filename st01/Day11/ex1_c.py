import pygame
import math
import sys

# --- Configuration ---

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
BACKGROUND_COLOR = (255, 255, 255)
POINT_COLOR = (200, 200, 200)
TEXT_COLOR = (200, 200, 200)
POINT_RADIUS = 2

# N is the number of points
N = 500

if N > 30:
    DO_DRAW_POINTS = False
else:
    DO_DRAW_POINTS = True

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

def connect(index1, index2):
    index1 = index1 % (N * 2)
    index2 = index2 % (N * 2)
    if index1 < N:
        x1 = 100
        y1 = 50 + index1 * (WINDOW_HEIGHT - 100) / (N - 1)
    else:
        x1 = WINDOW_WIDTH - 100
        y1 = 50 + (index1 - N) * (WINDOW_HEIGHT - 100) / (N - 1)
    if index2 < N:
        x2 = 100
        y2 = 50 + index2 * (WINDOW_HEIGHT - 100) / (N - 1)
    else:
        x2 = WINDOW_WIDTH - 100
        y2 = 50 + (index2 - N) * (WINDOW_HEIGHT - 100) / (N - 1)

    pygame.draw.aaline(screen, (0, 0, 0), (x1, y1), (x2, y2))






def draw(t):
    for i in range(N):
        connect(i, i*2)







# --- Main loop ---
running = True
t = 2
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    # Draw points and labels
    if DO_DRAW_POINTS:
        for i in range(N):
            x = 100
            y = 50 + i * (WINDOW_HEIGHT - 100) / (N - 1)

            # Draw the point
            pygame.draw.circle(screen, POINT_COLOR, (x, y), POINT_RADIUS)

            # Draw the label
            label = font.render(str(i), True, TEXT_COLOR)
            label_rect = label.get_rect(center=(x, y - 15))
            screen.blit(label, label_rect)
        for i in range(N):
            x = WINDOW_WIDTH - 100
            y = 50 + i * (WINDOW_HEIGHT - 100) / (N - 1)

            # Draw the point
            pygame.draw.circle(screen, POINT_COLOR, (x, y), POINT_RADIUS)

            # Draw the label
            label = font.render(str(i + N), True, TEXT_COLOR)
            label_rect = label.get_rect(center=(x, y - 15))
            screen.blit(label, label_rect)

    draw(t)

    pygame.display.flip()
    clock.tick(60)
    t += 0.01

pygame.quit()
sys.exit()
