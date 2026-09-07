import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)
            new_vector = self.velocity.rotate(new_angle)
            new_second_vector = self.velocity.rotate(-new_angle)
            New_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x,self.position.y, New_radius)
            new_asteroid2 = Asteroid(self.position.x,self.position.y, New_radius)
            new_asteroid1.velocity = new_vector * 1.2 
            new_asteroid2.velocity = new_second_vector * 1.2 