from circleshape import CircleShape
from constants import (PLAYER_RADIUS,LINE_WIDTH,PLAYER_TURN_SPEED,PLAYER_SPEED,
                       SCREEN_HEIGHT,SCREEN_WIDTH,SHOT_RADIUS,PLAYER_SHOOT_SPEED,
                       PLAYER_SHOOT_COOLDOWN_SECONDS)
from shot import Shot
import pygame
class Player (CircleShape):

    def __init__(self,x:float , y:float ) -> None:
        super().__init__(x,y,PLAYER_RADIUS);
        self.rotation = 0
        self.shoat_rate = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def rotate (self,dt)->None:
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
        self.checkBoundary()
    
    def move (self,dt) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        self.checkBoundary()


    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen,"white",points,LINE_WIDTH);
    
    def shoot(self) -> None:
        if self.shoat_rate > 0:
            return
        self.shoat_rate = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x,self.position.y,SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def checkBoundary(self) ->None:
        if self.position.x - PLAYER_RADIUS < 0:
            self.position.x  = 0 + PLAYER_RADIUS
        elif self.position.x + PLAYER_RADIUS > SCREEN_WIDTH:
            self.position.x  = SCREEN_WIDTH - PLAYER_RADIUS
        elif self.position.y - PLAYER_RADIUS < 0:
            self.position.y  = 0 + PLAYER_RADIUS
        elif self.position.y + PLAYER_RADIUS  > SCREEN_HEIGHT:
            self.position.y = SCREEN_HEIGHT - PLAYER_RADIUS

    def update(self, dt: float) -> None:
        self.shoat_rate = self.shoat_rate - dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()