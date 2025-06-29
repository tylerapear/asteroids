import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.constainers = (updatable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if player.check_for_collision(asteroid):
                print("Game Over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
