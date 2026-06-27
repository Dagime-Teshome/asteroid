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
    font = pygame.font.SysFont("Arial",30)
    
    clock = pygame.time.Clock()
    dt = 0.0
    surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    background = pygame.image.load("background.jpg").convert()
    background.set_alpha(999)
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots =  pygame.sprite.Group()
    Asteroid.containers=(updatable,drawable,asteroids)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,shots)
    prompt_text = "do you want to keep playing? Y/N"
    AsteroidField()
    continue_round = True
    continue_game = True

    while continue_game:
        player =Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2);
        while continue_round:
            log_state()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            surface.blit(background,(0,0))
            # surface.fill("black");
            updatable.update(dt)
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    log_event("player_hit");
                    print("Game over!")
                    continue_round = False
                for shot in shots:
                    if asteroid.collides_with(shot):
                        log_event("asteroid_shot");
                        asteroid.split()
                        shot.kill()
            dt = clock.tick(60) / 1000
            for sprite in drawable:
                sprite.draw(surface)
            pygame.display.flip()
            surface.blit(background,(0,0))
        text = font.render(prompt_text,False,"white")
        yes_text = font.render("Yes",False,"green")
        No_text = font.render("No",False,"Red")
        surface.blit(text,((SCREEN_WIDTH/2)-200,SCREEN_HEIGHT/2))
        surface.blit(yes_text,((SCREEN_WIDTH/2)-200,(SCREEN_HEIGHT/2) + 200))
        surface.blit(No_text,((SCREEN_WIDTH/2)-200,(SCREEN_HEIGHT/2)+ 300))
        pygame.display.flip()
        # answer = input("do you want to keep playing? Y/N \n");
        # if answer == "Y":

        #     asteroids.empty()
        #     updatable.empty()
        #     drawable.empty()
        #     player.kill()
        #     AsteroidField()
        #     continue_round = True
        #     continue
        # continue_game = False;
if __name__ == "__main__":
    main()
