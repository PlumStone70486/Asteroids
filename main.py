import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
	pygame.init()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroid_group = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroid_group, updatable, drawable)
	AsteroidField.containers = (updatable,)
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroidfield = AsteroidField()

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	while True:
		dt = clock.tick(60) / 1000
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill((0, 0, 0))
		updatable.update(dt)
		drawable.draw(screen)
		pygame.display.flip()

		for asteroid in asteroid_group:
			if player.collide(asteroid):
				print("Game over")
				sys.exit()

if __name__ == "__main__":
	main()
