import pygame
from pygame.locals import *


class Agent:
    def __init__(
        self,
        screen,
        start_position,
        width,
        color=(255, 255, 0),
        speed=1,
        player=False,
        state="ACTIVE",
    ):
        self.color = color
        self.speed = speed
        self.state = state
        self.screen = screen
        self.player = player
        self.x, self.y = start_position
        self.rect = Rect(self.x - (width / 2), self.y - (width / 2), width, width)

    def activate(self):
        self.state = "ACTIVE"

    def deactivate(self):
        self.state = "INACTIVE"

    def move_up(self, walls):
        if self.state == "ACTIVE":
            wall_rects = [wall.rect for wall in walls]
            step = self.rect.copy()
            step.center = (self.x, self.y - self.speed)
            if step.collidelist(wall_rects) == -1 and (self.y - self.speed) > 0:
                self.y -= self.speed

            self.rect.center = (self.x, self.y)

    def move_down(self, walls):
        if self.state == "ACTIVE":
            wall_rects = [wall.rect for wall in walls]
            step = self.rect.copy()
            step.center = (self.x, self.y + self.speed)
            if (
                step.collidelist(wall_rects) == -1
                and (self.y + self.speed) < self.screen.get_height()
            ):
                self.y += self.speed

            self.rect.center = (self.x, self.y)

    def move_left(self, walls):
        if self.state == "ACTIVE":
            wall_rects = [wall.rect for wall in walls]
            step = self.rect.copy()
            step.center = (self.x - self.speed, self.y)
            if step.collidelist(wall_rects) == -1 and (self.x - self.speed) > 0:
                self.x -= self.speed

            self.rect.center = (self.x, self.y)

    def move_right(self, walls):
        if self.state == "ACTIVE":
            wall_rects = [wall.rect for wall in walls]
            step = self.rect.copy()
            step.center = (self.x + self.speed, self.y)
            if (
                step.collidelist(wall_rects) == -1
                and (self.x + self.speed) < self.screen.get_width()
            ):
                self.x += self.speed

            self.rect.center = (self.x, self.y)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
