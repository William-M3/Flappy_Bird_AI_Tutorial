import pygame
from flappy_bird_game_files.Bird_Class import Bird
from flappy_bird_game_files.Pipe_Class import Pipe
from flappy_bird_game_files.Base_class import Base
import neat
import time
import os
import random



# Screen Size
WIN_WIDTH = 575
WIN_HEIGHT = 800

pygame.font.init()
pygame.display.init()
pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

STAT_FONT = pygame.font.SysFont("comicsans", 50)

# import assets set up
BG_IMGS = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bg.png")).convert_alpha())

def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMGS, (0, 0))
    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10 ))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)

    bird.draw(win)
    pygame.display.update()

def main():

    new_bird = Bird(230, 250)
    new_base = Base(730)
    new_pipes = [Pipe(700)]
    new_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    add_pipe = False
    score = 0
    run = True
    while run:

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #new_bird.move()
        rem = []
        for pipe in new_pipes:
            if pipe.collide(new_bird):
                pass
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < new_bird.x:
                pipe.passed = True
                add_pipe = True

            pipe.move()

        if add_pipe:
            score += 1
            new_pipes.append(Pipe(700))
            add_pipe = False

        for r in rem:
            new_pipes.remove(r)

        if new_bird.y + new_bird.img.get_height() < 0:
            pass

        new_base.move()
        draw_window(win=new_win, bird=new_bird,pipes=new_pipes,base=new_base, score=score)

    pygame.quit()
    quit()

# Main function call
main()
