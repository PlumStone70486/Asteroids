import pygame
from circleshape import *
from constants import *
from main import *

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.update_image()

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update_image(self):
        self.image.fill((0, 0, 0, 0))  # Clear with transparent background
        points = [(p.x - self.rect.x, p.y - self.rect.y) for p in self.triangle()]
        pygame.draw.polygon(self.image, "white", points, 2)

    #def draw(self, screen):
        #pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation = (self.rotation + PLAYER_TURN_SPEED * dt) % 360
        self.update_image()

    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction
        self.rect.center = self.position
        self.update_image()
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt, 1)
        if keys[pygame.K_s]:
            self.move(dt, -1)
            
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
        self.rect.center = self.position
