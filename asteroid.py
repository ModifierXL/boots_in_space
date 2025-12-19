from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
import random

from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        self.position += unit_vector + self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        first_angle = self.velocity.rotate(new_angle)
        second_angle = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = first_angle * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = second_angle * 1.2