FPS = 60
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

COLOR_RED = (150, 0, 0)
COLOR_TARGET = (120, 20, 0)
COLOR_WHITE = (200, 200, 200)

PLAYER_SIZE = 50

target_x = 135
target_y = 435
x = 375
y = 375










def on_start():
    global x, y
    # You have access to variables x and y.
    # Put your code here:
    ...



def every_frame():
    global x, y
    # You have access to variables x and y.
    # Put your code here:
    ...








import pygame

pygame.init()

on_start()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect((x, y, PLAYER_SIZE, PLAYER_SIZE))
target = pygame.Rect((target_x, target_y, PLAYER_SIZE, PLAYER_SIZE))

run = True
while run:
    screen.fill(COLOR_RED)

    every_frame()
    player.update(x, y, PLAYER_SIZE, PLAYER_SIZE)
    pygame.draw.rect(screen, COLOR_TARGET, target)
    pygame.draw.rect(screen, COLOR_WHITE, player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit
