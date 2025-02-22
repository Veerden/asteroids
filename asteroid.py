import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width = 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    random_angle = random.uniform(20, 50)
    rotated_right = self.velocity.rotate(random_angle)
    rotated_left = self.velocity.rotate(-random_angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    Asteroid(self.position, new_radius, rotated_right * 1.2)
    Asteroid(self.position, new_radius, rotated_left * 1.2)


    