import pygame

pygame.init()
WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Exercise 1")

def square(posX, posY, size, color = (255, 0, 0)):
    pygame.draw.rect(screen, color, (posX, posY, size, size))











def draw():
    for i in range(40):
        if i % 4 != 3:
            square(i * 20, 100, 15)










draw()
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
