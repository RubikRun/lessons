import pygame
import sys

# --- Configuration ---

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (238, 17, 17)

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()



def draw_square(color, x, y, size):
    """
    Draw a square on a pygame surface.

    Args:
        surface: The pygame surface to draw on.
        color: RGB tuple, e.g. (255, 0, 0)
        x, y: Top-left corner of the square
        size: Length of each side
        width: Line thickness. 0 = filled square
    """
    rect = pygame.Rect(x, y, size, size)
    pygame.draw.rect(screen, color, rect, 0)

def sPressed():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_s]

def dPressed():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_d]

def wPressed():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_w]

def aPressed():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_a]


# TO-DO list:
# - Fix the lag of pressing keys

x=50
y=50
j=50
i=70

dirX=0
dirY=20

def draw():
    global x, y, dirX, dirY, i, j

    if sPressed():
        dirY=20
        dirX=0
        j=x
        i=y-20

    if dPressed():
        dirX=20
        dirY=0
        j=x-20
        i=y

    if wPressed():
        dirY=-20
        dirX=0
        j=x
        i=y+20
    
    if aPressed():
        dirX=-20
        dirY=0
        j=x+20
        i=y
    

    x += dirX
    y += dirY
    j += dirX
    i += dirY

    draw_square( (17, 111, 238), x, y, 20)
    draw_square( (17, 111, 238), j, i, 20)




# --- Main loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    draw()

    pygame.display.flip()
    clock.tick(1)

pygame.quit()
sys.exit()