import pygame
import math
import sys

# --- Configuration ---

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
BACKGROUND_COLOR = (255, 255, 255)
POINT_COLOR = (200, 200, 200)
TEXT_COLOR = (200, 200, 200)
CIRCLE_RADIUS = 400
POINT_RADIUS = 2

# N is the number of points
N = 10

if N > 100:
    DO_DRAW_POINTS = False
else:
    DO_DRAW_POINTS = True

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

# --- Calculate circle center ---
center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2

def connect(index1, index2):
    angle1 = 2 * math.pi * index1 / N
    angle2 = 2 * math.pi * index2 / N

    x1 = center_x + int(CIRCLE_RADIUS * math.cos(angle1))
    y1 = center_y + int(CIRCLE_RADIUS * math.sin(angle1))

    x2 = center_x + int(CIRCLE_RADIUS * math.cos(angle2))
    y2 = center_y + int(CIRCLE_RADIUS * math.sin(angle2))

    pygame.draw.aaline(screen, (0, 0, 0), (x1, y1), (x2, y2))






def draw(t):
    connect(3, t)







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
            angle = 2 * math.pi * i / N
            x = center_x + int(CIRCLE_RADIUS * math.cos(angle))
            y = center_y + int(CIRCLE_RADIUS * math.sin(angle))

            # Draw the point
            pygame.draw.circle(screen, POINT_COLOR, (x, y), POINT_RADIUS)

            # Draw the label
            label = font.render(str(i), True, TEXT_COLOR)
            label_rect = label.get_rect(center=(x, y - 15))
            screen.blit(label, label_rect)

    draw(t)

    pygame.display.flip()
    clock.tick(60)
    t += 0.005

pygame.quit()
sys.exit()
