from turtle import width

import pygame
import random
import math

from pygame.rect import Rect

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((1400, 800))

run = True

class playerObject(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, display):
        pygame.draw.circle(display, (255, 0, 0), (self.x, self.y), self.radius)

player = playerObject(random.randint(0, 500), random.randint(0, 500), 20)

class enemyObject(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.width = width

    def draw(self, display):
        self.rect = pygame.Rect(100, 100, 20, 20)
        pygame.draw.rect(display, (0, 255, 0), self.rect, 50)

    def move_towards_player(self, player):
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        dirvect.normalize()
        dirvect.scale_to_length(5)
        self.rect.move_ip(dirvect)

enemy = enemyObject(300, 300, 20)

while run:
    display.fill((255, 150, 133))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 5

    if keys[pygame.K_s]:
        player.y += 5

    if keys[pygame.K_a]:
        player.x -= 5

    if keys[pygame.K_d]:
        player.x += 5

    # print(player.x)
    # print(player.y)
    #
    # print(enemy.x)
    # print(enemy.y)
    #
    #
    # angle = math.atan2(enemy.y - player.y, enemy.x - player.x)
    # degrees = math.degrees(angle)
    # print(angle)
    # print(degrees)

    # enemy.move_towards_player(player)
    enemy.draw(display)
    player.draw(display)
    clock.tick(60)
    pygame.display.update()