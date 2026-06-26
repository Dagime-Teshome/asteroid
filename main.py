import sys

import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # background = pygame.image.load("background.jpg").convert()
    # background.set_alpha(999)
    # background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots =  pygame.sprite.Group()
    Asteroid.containers=(updatable,drawable,asteroids)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,shots)
    player =Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2);
    AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # surface.blit(background,(0,0))
        surface.fill("black");
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit");
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot");
                    asteroid.split()
                    shot.kill()
        dt = clock.tick(60) / 1000
        for sprite in drawable:
            sprite.draw(surface)
        pygame.display.flip()
        # surface.blit(background,(0,0))
if __name__ == "__main__":
    main()
