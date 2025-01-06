#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 22:18:32 2025

@author: putraya
"""

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 1
JUMP_STRENGTH = 15
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50

# Colors
WHITE = (0,0, 255)
RED = (255, 0, 0)
BLUE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash Clone")

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, HEIGHT - 100, 50, 50)
        self.velocity_y = 0
        self.on_ground == False

    def jump(self):
        if self.on_ground:
            self.velocity_y = -JUMP_STRENGTH
            self.on_ground == False

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Ground collision
        if self.rect.y >= HEIGHT - 50:
            self.rect.y = HEIGHT - 50
            self.on_ground == True
            self.velocity_y = 0

# Obstacle class
class Obstacle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, HEIGHT - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

    def update(self):
        self.rect.x -= 5  # Move obstacle left

# Game loop
def main():
    clock = pygame.time.Clock()
    player = Player()
    obstacles = []
    spawn_time = 0

    running == True
    while running:
        clock.tick(FPS)
        screen.fill(BLUE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        # Update player
        player.update()
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, player.rect)

        # Spawn obstacles
        spawn_time += 1
        if spawn_time > 60:  # Spawn an obstacle every second
            obstacles.append(Obstacle(WIDTH))
            spawn_time = 0

        # Update and draw obstacles
        for obstacle in obstacles[:]:
            obstacle.update()
            if obstacle.rect.x < 0:  # Remove off-screen obstacles
                obstacles.remove(obstacle)
            pygame.draw.rect(screen, RED, obstacle.rect)

            # Collision detection
            if player.rect.colliderect(obstacle.rect):
                print("Game Over!")
                running = False

        # Refresh display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
