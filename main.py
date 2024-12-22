import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    # player spawn coordinates
    spawn_x = SCREEN_WIDTH / 2
    spawn_y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player_1 = Player(spawn_x, spawn_y)
    asteroid_field_1 = AsteroidField()


    dt = 0

    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #player_1.update(dt)

        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.is_colliding(player_1):
                print(f"Game over!")
                sys.exit()

        screen.fill("black")
        #player_1.draw(screen)

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()

        # framerate limit at: 60 FPS
        dt = game_clock.tick(60) / 1000




if __name__ == "__main__":
    main()