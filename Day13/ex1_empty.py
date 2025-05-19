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
DEFAULT_COLOR = (255, 173, 51)
DEFAULT_RADIUS = 10


def circles(positions, radius=DEFAULT_RADIUS, color=DEFAULT_COLOR):
    for pos in positions:
        if isinstance(pos, list) and len(pos) == 2:
            x, y = int(pos[0]), int(pos[1])
            pygame.gfxdraw.filled_circle(screen, x, y, radius, color)
            pygame.gfxdraw.aacircle(screen, x, y, radius, color)

def squares(positions, radius=DEFAULT_RADIUS, color=DEFAULT_COLOR):
    side = radius * 2
    for pos in positions:
        if isinstance(pos, list) and len(pos) == 2:
            x, y = int(pos[0]), int(pos[1])
            rect = pygame.Rect(x - radius, y - radius, side, side)
            pygame.draw.rect(screen, color, rect)

def triangles(positions, radius=DEFAULT_RADIUS, color=DEFAULT_COLOR):
    for pos in positions:
        if isinstance(pos, list) and len(pos) == 2:
            x, y = pos
            points = [
                (x, y - radius),  # Top
                (x - radius * math.sin(math.radians(60)), y + radius / 2),  # Bottom left
                (x + radius * math.sin(math.radians(60)), y + radius / 2),  # Bottom right
            ]
            pygame.draw.polygon(screen, color, points)



# === Stickman Part Positions ===
head = [[390, 200], [389, 208], [386, 216], [382, 223], [376, 229], [370, 234], [362, 238], [354, 239], [345, 239], [337, 238], [330, 234], [323, 229], [317, 223], [313, 216], [310, 208], [310, 200], [310, 191], [313, 183], [317, 176], [323, 170], [330, 165], [337, 161], [345, 160], [354, 160], [362, 161], [370, 165], [376, 170], [382, 176], [386, 183], [389, 191]]
body = [[350, 240], [350, 250], [350, 260], [350, 270], [350, 280], [350, 290], [350, 300], [350, 310], [350, 320], [350, 330]]
left_leg = [[350, 340], [345, 350], [340, 360], [335, 370], [330, 380], [325, 390], [320, 400], [315, 410], [310, 420], [305, 430]]
right_leg = [[350, 340], [355, 350], [360, 360], [365, 370], [370, 380], [375, 390], [380, 400], [385, 410], [390, 420], [395, 430]]
left_arm = [[350, 240], [344, 245], [338, 250], [332, 255], [326, 260], [320, 265], [314, 270], [308, 275], [302, 280], [296, 285]]
right_arm = [[350, 240], [356, 245], [362, 250], [368, 255], [374, 260], [380, 265], [386, 270], [392, 275], [398, 280], [404, 285]]









def draw():
    ...






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
