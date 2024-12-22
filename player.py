import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Left and Right rotation
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            #print("input: left")
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            #print("input: right")
            self.rotate(dt)

        # Up and Down movement
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            #print("input: down")
            self.move(-dt)
        if keys[pygame.K_z] or keys[pygame.K_UP]:
            #print("input: up")
            self.move(dt)

        # Shooting
        if keys[pygame.K_SPACE]:
            #print("shooting")
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        print(f"shooting from {self.position.x}, {self.position.y}")
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS, self.rotation)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED