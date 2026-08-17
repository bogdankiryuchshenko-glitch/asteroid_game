
import pygame
import sys
from player import Player 
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {SCREEN_WIDTH}") 
    print (f"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
        screen.fill((0, 0, 0))
        updatable.update(dt)

        for sprites in asteroids:
            if sprites.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            

        for draws in drawable:
            draws.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

