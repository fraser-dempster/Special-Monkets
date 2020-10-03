import pygame
import math

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((1400, 800))


class playerObject(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, display):
        pygame.draw.circle(display, (255, 0, 0), (self.x, self.y), self.radius)


class bullet(object):
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.lifetime = 50
        self.speed = 15
        self.angle = math.atan2(mouse_y-self.y, mouse_x-self.x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.radius = 5

    def draw(self, draw):
        self.x += int(self.x_vel)
        self.y += int(self.y_vel)

        pygame.draw.circle(display, (255, 255, 255), (self.x, self.y), self.radius)
        self.lifetime -= 1




player = playerObject(100, 100, 20)
bullets = []

run = True
while run:
    display.fill((255, 150, 133))

    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullets.append(bullet(player.x, player.y, x, y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 5

    if keys[pygame.K_s]:
        player.y += 5

    if keys[pygame.K_a]:
        player.x -= 5

    if keys[pygame.K_d]:
        player.x += 5

    for bullet_ in bullets:
        if bullet_.lifetime <= 0:
            bullets.pop(bullets.index(bullet_))
        bullet_.draw(display)

    player.draw(display)

    clock.tick(60)
    pygame.display.update()