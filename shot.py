import pygame
from circleshape import *
from constants import *
from main import *

class Shot(CircleShape):
    def __init__(self, x, y, rotation, speed):
        super().__init__(x, y, SHOT_RADIUS)

        # Create the image for the sprite with the circle drawn
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS, 2)
        self.rect = self.image.get_rect(center=(x, y))

        self.velocity = pygame.Vector2(0, 1)
        self.velocity.rotate_ip(rotation)
        self.velocity *= speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position