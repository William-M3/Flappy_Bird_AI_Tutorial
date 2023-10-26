import pygame
from flappy_bird_game_files.Bird_Class import Bird
import neat

import time
import os
import random

# Screen Size
WIN_WIDTH = 500
WIN_HEIGHT = 800

# import assets set up
PIPE_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "pipe.png")))]

BASE_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "base.png")))]
BG_IMGS = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bg.png")))

def draw_window(win, bird):
    win.blit(BG_IMGS, (0, 0))
    bird.draw(win)
    pygame.display.update()

def main():

    new_bird = Bird(200, 200)
    new_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        new_bird.move()
        draw_window(win=new_win, bird=new_bird)

    pygame.quit()
    quit()

# Main function call
main()
