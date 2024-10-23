import pygame
import random
from circleshape import *
from constants import *
from main import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Create the image for the sprite with the circle drawn
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (radius, radius), radius, 2)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        random_angel = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angel)
        velocity2 = self.velocity.rotate(-random_angel)
        velocity1 *= 1.2
        velocity2 *= 1.2
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2

        for container in Asteroid.containers:
            container.add(asteroid1, asteroid2)

        self.kill()



    def update(self, dt):
        # Assume self.velocity has been set appropriately on creation
        displacement = self.velocity * dt
        self.position += displacement
        self.rect.center = self.position  # Update position of the rect to reflect movement