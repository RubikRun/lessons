# exec(open('ninja_console.py').read())

import pygame
import sys
import math
import threading
import pygetwindow
from random import randint

pygame.init()

WINDOW_SIZE = 800
GRID_SIZE = 20
CELL_SIZE = 40
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Ninja')

# Control the position of the Pygame window
def set_window_position(x, y):
    window = pygetwindow.getWindowsWithTitle('Ninja')[0]  # Gets the Pygame window by title
    window.moveTo(x, y)

# Set window position (e.g., top-left corner of the screen at position (100, 100))
set_window_position(20, 20)

running = False
game_thread = None

WHITE = (170, 170, 170)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ninja setup
ninja_image = pygame.image.load("C:/dev/lessons/st02/Day00/ninja/ninja.png") 
ninja_image = pygame.transform.scale(ninja_image, (CELL_SIZE * 1.3, CELL_SIZE * 1.3))
ninja_rect = ninja_image.get_rect()

ninja_angle = 0  # Facing right (0 degrees)
ninja_x, ninja_y = GRID_SIZE // 2, GRID_SIZE // 2  # Center of the grid

# Apple setup
apple_image = pygame.image.load("C:/dev/lessons/st02/Day00/ninja/apple.png")
apple_image = pygame.transform.scale(apple_image, (CELL_SIZE * 0.7, CELL_SIZE * 0.7))
apple_rect = apple_image.get_rect()
apple_rect.center = (4 * CELL_SIZE, 18 * CELL_SIZE)

# Initial apple position and rotation
apple_x, apple_y = 4, 18

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('x = 0    y = 0', True, WHITE, BLACK)
textRect = text.get_rect()
textRect.topleft = (10, 10)

# Draw grid function
def draw_grid():
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, WINDOW_SIZE))
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WINDOW_SIZE, y))

    pygame.draw.circle(screen, WHITE, ((GRID_SIZE // 2) * CELL_SIZE, (GRID_SIZE // 2) * CELL_SIZE), 8)

def update_text():
    global text
    text = font.render( \
        "x = " + str(int(ninja_x - GRID_SIZE // 2)) + "    " + "y = " + str(int(ninja_y - GRID_SIZE // 2)), \
        True, \
        WHITE, \
        BLACK \
    )

# Rotate ninja image based on angle
def rotate_ninja():
    rotated_image = pygame.transform.rotate(ninja_image, ninja_angle)
    rotated_rect = rotated_image.get_rect(center=ninja_rect.center)
    return rotated_image, rotated_rect

# Movement functions
def up(amount):
    global ninja_x, ninja_y, apple_x, apple_y, apple_rect
    rad = math.radians(ninja_angle)
    ninja_x -= amount * math.sin(rad)
    ninja_y -= amount * math.cos(rad)

    if ninja_x == apple_x and ninja_y == apple_y:
        apple_x = randint(1, 19)
        apple_y = randint(1, 19)
        apple_rect.center = (apple_x * CELL_SIZE, apple_y * CELL_SIZE)

def down(amount):
    global ninja_x, ninja_y, apple_x, apple_y, apple_rect
    rad = math.radians(ninja_angle)
    ninja_x += amount * math.sin(rad)
    ninja_y += amount * math.cos(rad)

    if ninja_x == apple_x and ninja_y == apple_y:
        apple_x = randint(1, 19)
        apple_y = randint(1, 19)
        apple_rect.center = (apple_x * CELL_SIZE, apple_y * CELL_SIZE)

def left(amount):
    global ninja_x, ninja_y, apple_x, apple_y, apple_rect
    rad = math.radians(ninja_angle + 90)
    ninja_x -= amount * math.sin(rad)
    ninja_y -= amount * math.cos(rad)

    if ninja_x == apple_x and ninja_y == apple_y:
        apple_x = randint(1, 19)
        apple_y = randint(1, 19)
        apple_rect.center = (apple_x * CELL_SIZE, apple_y * CELL_SIZE)

def right(amount):
    global ninja_x, ninja_y, apple_x, apple_y, apple_rect
    rad = math.radians(ninja_angle - 90)
    ninja_x -= amount * math.sin(rad)
    ninja_y -= amount * math.cos(rad)

    if ninja_x == apple_x and ninja_y == apple_y:
        apple_x = randint(1, 19)
        apple_y = randint(1, 19)
        apple_rect.center = (apple_x * CELL_SIZE, apple_y * CELL_SIZE)

# Rotation functions
def rotateRight():
    global ninja_angle
    ninja_angle -= 90
    if ninja_angle < 0:
        ninja_angle += 360

def rotateLeft():
    global ninja_angle
    ninja_angle += 90
    if ninja_angle >= 360:
        ninja_angle -= 360

# Main game loop, running on a separate thread to keep interactive mode free
def game_loop():
    global running, ninja_x, ninja_y, ninja_angle, apple_x, apple_y
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)  # Clear screen with black
        draw_grid()  # Draw the grid

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Apply rotation and draw the ninja at the new position
        rotated_image, rotated_rect = rotate_ninja()
        rotated_rect.center = (ninja_x * CELL_SIZE,
                               ninja_y * CELL_SIZE)
        screen.blit(rotated_image, rotated_rect)

        screen.blit(apple_image, apple_rect)

        # Draw text
        update_text()
        screen.blit(text, textRect)

        # Update the display
        pygame.display.flip()

        # Frame rate
        clock.tick(30)

    pygame.quit()

# Start the game loop in a separate thread
def start_game():
    global game_thread
    game_thread = threading.Thread(target=game_loop)
    # game_thread.daemon = True  # This allows the thread to exit when the main program exits
    game_thread.start()

# Start the game loop
start_game()