import pygame
from constants import *
from player import *
def main():
	pygame.init()
	clock = pygame.time.Clock()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	while True:
		dt = clock.tick(60) / 1000
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill((0, 0, 0))
		player.draw(screen)
		player.update(dt)
		pygame.display.flip()


if __name__ == "__main__":
	main()
