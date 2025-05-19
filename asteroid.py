import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):

        # It's Dead Jim!  Kill the Asteroid!
        self.kill()

        # Check to see if it was the smallest size allowed
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Damn...cold shit.  It be DEAD DEAD!

        # HUZZAH!  Two more to defeat you foul PLAYER!
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = a * 1.2

        asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid.velocity = b * 1.2
