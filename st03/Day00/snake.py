WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FPS = 60

COLOR_BACKGROUND = (0, 0, 0)
COLOR_SNAKE = (60, 160, 20)
COLOR_FRUIT = (200, 90, 30)

SNAKE_SIZE = 50
FRUIT_SIZE = 30

SPEED_INCREASE_FRUITS = 2

INITIAL_SPEED = 3
INITIAL_SNAKE_POSITION_X = int(WINDOW_WIDTH * 0.5)
INITIAL_SNAKE_POSITION_Y = int(WINDOW_HEIGHT * 0.5)

import pygame
from copy import deepcopy
from random import randint

def is_time_for_move():
    return frames_count % int(FPS / speed) == 0

def generate_fruit():
    global fruit
    fruit = pygame.Rect((randint(FRUIT_SIZE, WINDOW_WIDTH - FRUIT_SIZE * 2), randint(FRUIT_SIZE, WINDOW_HEIGHT - FRUIT_SIZE * 2), FRUIT_SIZE, FRUIT_SIZE))

def grow_snake():
    snake.append(deepcopy(snake[-1]))

def init():
    pygame.init()

    global screen, clock, frames_count
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    frames_count = 0

    global snake, fruit, speed, dirx, diry, score, bounds
    snake = [
        pygame.Rect((INITIAL_SNAKE_POSITION_X - 0 * SNAKE_SIZE, INITIAL_SNAKE_POSITION_Y, SNAKE_SIZE, SNAKE_SIZE)),
        pygame.Rect((INITIAL_SNAKE_POSITION_X - 1 * SNAKE_SIZE, INITIAL_SNAKE_POSITION_Y, SNAKE_SIZE, SNAKE_SIZE)),
        pygame.Rect((INITIAL_SNAKE_POSITION_X - 2 * SNAKE_SIZE, INITIAL_SNAKE_POSITION_Y, SNAKE_SIZE, SNAKE_SIZE)),
        pygame.Rect((INITIAL_SNAKE_POSITION_X - 3 * SNAKE_SIZE, INITIAL_SNAKE_POSITION_Y, SNAKE_SIZE, SNAKE_SIZE)),
        pygame.Rect((INITIAL_SNAKE_POSITION_X - 4 * SNAKE_SIZE, INITIAL_SNAKE_POSITION_Y, SNAKE_SIZE, SNAKE_SIZE))
    ]
    bounds = [
        pygame.Rect((-10, -10, 10, WINDOW_HEIGHT + 20)),
        pygame.Rect((WINDOW_WIDTH, -10, 10, WINDOW_HEIGHT + 20)),
        pygame.Rect((-10, -10, WINDOW_WIDTH + 20, 10)),
        pygame.Rect((-10, WINDOW_HEIGHT, WINDOW_WIDTH + 20, 10))
    ]
    generate_fruit()
    speed = INITIAL_SPEED
    dirx = 1
    diry = 0
    score = 0

def draw():
    screen.fill(COLOR_BACKGROUND)
    for part in snake:  
        pygame.draw.rect(screen, COLOR_SNAKE, part)
    pygame.draw.rect(screen, COLOR_FRUIT, fruit)

def handle_events():
    global dirx, diry
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                dirx = 0
                diry = -1
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                dirx = 0
                diry = 1
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                dirx = -1
                diry = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                dirx = 1
                diry = 0

    return True

def update(running):
    global frames_count, speed, score, bounds
    if not handle_events():
        return "quit"
    if not running:
        return "ok"

    if is_time_for_move():
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = deepcopy(snake[i - 1])
        snake[0].move_ip(dirx * SNAKE_SIZE, diry * SNAKE_SIZE)

        for part in snake[1:]:
            if part == snake[0]:
                return "gameover"
            
        if snake[0].colliderect(bounds[0]) or snake[0].colliderect(bounds[1]) or snake[0].colliderect(bounds[2]) or snake[0].colliderect(bounds[3]):
            return "gameover"

        if snake[0].colliderect(fruit):
            score += 1
            generate_fruit()
            grow_snake()
            if score % SPEED_INCREASE_FRUITS == 0:
                speed += 1

    pygame.display.update()
    clock.tick(FPS)
    frames_count += 1

    return "ok"

def run():
    running = True
    while True:
        draw()
        state = update(running)
        if state == "quit":
            break
        elif state == "gameover":
            running = False


def quit():
    pygame.quit()

init()
run()
quit()