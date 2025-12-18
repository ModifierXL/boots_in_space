from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        self.position += unit_vector + self.velocity * dt