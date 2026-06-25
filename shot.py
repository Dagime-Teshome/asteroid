import pygame

from constants import SCREEN_HEIGHT,SCREEN_WIDTH

from circleshape import CircleShape
from constants import SHOT_RADIUS,LINE_WIDTH
class Shot(CircleShape):

    def __init__(self,x:float,y:float,radius:float):
        super().__init__(x,y,SHOT_RADIUS);

    def draw(self,surface:pygame.surface) -> None:
        pygame.draw.circle(surface,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt:float)-> None:
        self.position += (self.velocity * dt)
        self.checkBoundary()

    def checkBoundary(self):
        if self.position.x > SCREEN_WIDTH or self.position.x < 0:
            self.kill()
        if self.position.y > SCREEN_HEIGHT or self.position.y < 0:
            self.kill()