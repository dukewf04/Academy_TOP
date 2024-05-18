import pygame
import sys

# Определяем цвета
BLACK = (0, 0, 0)
BLUE = (0, 152, 236)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Button:
    def __init__(self, pg: pygame, x, y, width, height, screen):
        self.pg = pg
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = BLUE

    def draw(self):
        self.pg.draw.rect(self.screen, self.color, (0, 0, self.width, self.height), border_radius=7)
        label = self.pg.font.SysFont('Calibri', 20, bold=True).render("New Game", 1, BLACK)
        self.screen.blit(label, (5, 10))

    def is_clicked(self, pos):
        x, y = pos
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False