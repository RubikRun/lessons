import pygame
import pygame.gfxdraw
import sys
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

# Colors
BACKGROUND_COLOR = (20, 20, 20)
CIRCLE_COLOR = (255, 173, 51)
CIRCLE_RADIUS = 10

# Function to draw circles at the given list of positions
def circles(positions):
    for pos in positions:
        if isinstance(pos, list) and len(pos) == 2:
            x, y = pos
            pygame.gfxdraw.filled_circle(screen, int(x), int(y), CIRCLE_RADIUS, CIRCLE_COLOR)
            pygame.gfxdraw.aacircle(screen, int(x), int(y), CIRCLE_RADIUS, CIRCLE_COLOR)



# === Stickman Part Positions ===

# Center of the stickman
center_x = WIDTH // 2
center_y = HEIGHT // 2

# Head: a big circle made of points
head = []
head_radius = 40
for angle in range(0, 360, 12):  # 30 points (360/12)
    rad = math.radians(angle)
    x = center_x + math.cos(rad) * head_radius
    y = center_y - 150 + math.sin(rad) * head_radius
    head.append([int(x), int(y)])

# Body: vertical line
body = []
for i in range(10):  # 10 points
    x = center_x
    y = center_y - 110 + i * 10
    body.append([x, y])

# Left Leg: angled line
left_leg = []
for i in range(10):
    x = center_x - i * 5
    y = center_y - 10 + i * 10
    left_leg.append([x, y])

# Right Leg: angled line
right_leg = []
for i in range(10):
    x = center_x + i * 5
    y = center_y - 10 + i * 10
    right_leg.append([x, y])

# Left Arm: angled upward line
left_arm = []
for i in range(10):
    x = center_x - i * 6
    y = center_y - 110 + i * 5
    left_arm.append([x, y])

# Right Arm: angled upward line
right_arm = []
for i in range(10):
    x = center_x + i * 6
    y = center_y - 110 + i * 5
    right_arm.append([x, y])



print(head)
print(body)
print(left_leg)
print(right_leg)
print(left_arm)
print(right_arm)




def draw():
    circles(head)
    circles(body)
    circles(left_leg)
    circles(right_leg)
    circles(left_arm)
    circles(right_arm)






# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
