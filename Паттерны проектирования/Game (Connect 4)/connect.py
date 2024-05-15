import pygame as pg
import sys
import math
from config import *
from board import *


pg.init()
pg.display.set_caption("Connect 4")

width = COLUMNS * DISC_SIZE
heigth = (ROWS + 1) * DISC_SIZE

size = (width, heigth)
screen = pg.display.set_mode(size)
my_font = pg.font.SysFont("Calibri", 60)

def draw_grid():
    pass