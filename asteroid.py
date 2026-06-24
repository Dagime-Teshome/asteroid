import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

from circleshape import CircleShape
from constants import LINE_WIDTH




class Asteroid(CircleShape):

    def __init__(self,x:float , y:float , radius:float)->None:
        super().__init__(x,y,radius)

    def draw(self,surface: pygame.Surface) -> None:
        pygame.draw.circle(surface,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt:float) -> None:
        self.position = self.position + (self.velocity * dt);
    def split (self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        vel_1 = self.velocity.rotate(angle)
        vel_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid_1.velocity += vel_1 * 1.2
        asteroid_2.velocity += vel_2 * 1.2