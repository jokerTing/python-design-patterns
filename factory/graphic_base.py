import pygame
from time import sleep

#pygame.init()
windows_dimensions = 800, 600
screen = pygame.display.set_mode(windows_dimensions)

x, y = 100, 100

player_quits = False

while not player_quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_quits = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 4
    if pressed[pygame.K_DOWN]: y += 4
    if pressed[pygame.K_LEFT]: x -= 4
    if pressed[pygame.K_RIGHT]: x += 4

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 34), pygame.Rect(x, y, 20, 20))
    pygame.display.flip()


