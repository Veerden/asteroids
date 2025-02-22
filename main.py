import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots_group = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)   
	Shot.containers = (shots_group, updatable, drawable)
	player = Player(x, y)
	asteroid_field = AsteroidField()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			dt = clock.tick(60) / 1000
		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.check_collision(player) == True:
				print("Game Over!")
				sys.exit()

		screen.fill((0,0,0))
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()

if __name__ == "__main__":
	main()
