import pygame
import sys
import math

pygame.init()

WINDOW_SIZE = 800
GRID_SIZE = 20
CELL_SIZE = 40
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Ninja')

WHITE = (170, 170, 170)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Sprite setup
sprite_image = pygame.image.load("ninja/ninja.png")  # Replace with your image path
sprite_image = pygame.transform.scale(sprite_image, (CELL_SIZE * 1.3, CELL_SIZE * 1.3))  # Resize to fit the grid
sprite_rect = sprite_image.get_rect()

# Initial sprite position and rotation
sprite_x, sprite_y = GRID_SIZE // 2, GRID_SIZE // 2  # Center of the grid
sprite_angle = 0  # Facing right (0 degrees)


font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('x = 0    y = 0', True, WHITE, BLACK)
textRect = text.get_rect()
textRect.topleft = (10, 10)

FRAMES_BETWEEN_MOVES = 10
frames_since_last_move = FRAMES_BETWEEN_MOVES

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
        "x = " + str(int(sprite_x - GRID_SIZE // 2)) + "    " + "y = " + str(int(sprite_y - GRID_SIZE // 2)), \
        True, \
        WHITE, \
        BLACK \
    )

# Rotate sprite image based on angle
def rotate_sprite():
    rotated_image = pygame.transform.rotate(sprite_image, sprite_angle)
    rotated_rect = rotated_image.get_rect(center=sprite_rect.center)
    return rotated_image, rotated_rect

# Movement functions
def move_up(amount):
    global sprite_x, sprite_y
    rad = math.radians(sprite_angle)
    sprite_x -= amount * math.sin(rad)
    sprite_y -= amount * math.cos(rad)

def move_down(amount):
    global sprite_x, sprite_y
    rad = math.radians(sprite_angle)
    sprite_x += amount * math.sin(rad)
    sprite_y += amount * math.cos(rad)

def move_left(amount):
    global sprite_x, sprite_y
    rad = math.radians(sprite_angle + 90)
    sprite_x -= amount * math.sin(rad)
    sprite_y -= amount * math.cos(rad)

def move_right(amount):
    global sprite_x, sprite_y
    rad = math.radians(sprite_angle - 90)
    sprite_x -= amount * math.sin(rad)
    sprite_y -= amount * math.cos(rad)

# Rotation functions
def rotate_right():
    global sprite_angle
    sprite_angle -= 90
    if sprite_angle < 0:
        sprite_angle += 360

def rotate_left():
    global sprite_angle
    sprite_angle += 90
    if sprite_angle >= 360:
        sprite_angle -= 360

# Main game loop
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

    # Handle key presses for movement
    keys = pygame.key.get_pressed()

    if frames_since_last_move > FRAMES_BETWEEN_MOVES:
        if keys[pygame.K_UP]:  # Move up
            move_up(1)
            frames_since_last_move = 0
        if keys[pygame.K_DOWN]:  # Move down
            move_down(1)
            frames_since_last_move = 0
        if keys[pygame.K_LEFT]:  # Move left
            move_left(1)
            frames_since_last_move = 0
        if keys[pygame.K_RIGHT]:  # Move right
            move_right(1)
            frames_since_last_move = 0

        if keys[pygame.K_a]:  # Rotate left
            rotate_left()
            frames_since_last_move = 0
        if keys[pygame.K_d]:  # Rotate right
            rotate_right()
            frames_since_last_move = 0

    # Apply rotation and draw the sprite at the new position
    rotated_image, rotated_rect = rotate_sprite()
    rotated_rect.center = (sprite_x * CELL_SIZE,
                           sprite_y * CELL_SIZE)
    
    screen.blit(rotated_image, rotated_rect)

    # Draw text
    update_text()
    screen.blit(text, textRect)

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

    frames_since_last_move += 1

pygame.quit()
sys.exit()
