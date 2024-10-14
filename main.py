import pygame
from constants import *
from player import *
def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	player = Player(2, 2, PLAYER_RADIUS)
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	while 1 > 0:
		screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		black = (0, 0, 0)
		screen.fill(black)
		pygame.display.flip()
		clock.tick(60)
		dt = clock.get_time() / 1000
		player.draw(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		


if __name__ == "__main__":
	main()
