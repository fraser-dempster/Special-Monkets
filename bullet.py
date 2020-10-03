import math
import pygame

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

    def render(self, display):
        self.x += int(self.x_vel)
        self.y += int(self.y_vel)

        pygame.draw.circle(display, (255, 255, 0), (self.x, self.y), self.radius)
        self.lifetime -= 1
    
    def update(self):
        pass
    
    def isDestroyed(self):
        if self.lifetime <= 0:
             return True