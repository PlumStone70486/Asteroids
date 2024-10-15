import pygame
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

    def update(self, dt):
        # Assume self.velocity has been set appropriately on creation
        displacement = self.velocity * dt
        self.position += displacement
        self.rect.center = self.position  # Update position of the rect to reflect movement