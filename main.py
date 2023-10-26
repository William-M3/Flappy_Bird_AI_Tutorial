import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

# import assets set up
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bird3.png")))]

PIPE_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "pipe.png")))]

BASE_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "base.png")))]
BG_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bg.png")))]

class Bird:
    IMGS = BIRD_IMGS
    MAX_Rotation = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[self.img_count]

    def jump(self):
        self.vel = 10.5