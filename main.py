import pygame
from constants import *
from player import *
def main():
	pygame.init()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable) 
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

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

if __name__ == "__main__":
	main()
