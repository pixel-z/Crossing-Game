import pygame
import math
import time
pygame.init()

pygame.display.set_caption("What does the FOX say?!")
window = pygame.display.set_mode((800, 800))

fox = pygame.image.load("gitlab.png")
fox = pygame.transform.scale(fox, (60, 60))

wolf = pygame.image.load("wolf.png")
wolf = pygame.transform.scale(wolf, (60, 60))

hunter = pygame.image.load("hunter.png")
hunter = pygame.transform.scale(hunter, (60, 60))

obstacle = pygame.image.load("obstacle.png")
obstacle = pygame.transform.scale(obstacle, (60, 60))

# initial posi of hunters
h1 = 0
h1_y = 60 + 10
h2 = 0
h2_y = 60 + 10
h3 = 0
h3_y = 150 + 60 + 10
h4 = 0
h4_y = 300 + 60 + 10
h5 = 0
h5_y = 300 + 60 + 10
h6 = 0
h6_y = 450 + 60 + 10
h7 = 0
h7_y = 600 + 60 + 10

x = 400 - 60
y = 0
width = 60
height = 60
vel = 1

# increase in vel of a and b after lvls
vel_fox = 0
vel_wolf = 0

collision1 = 0
collision2 = 1

# initialization of var
flag = 0
score_value = 0
lvl_A = 1
lvl_B = 1

# common fonts
font = pygame.font.Font('freesansbold.ttf', 22)

# initial time
t0 = time.time()
time_A = 0
time_B = 0

# h1 =x-coordinate & h2=y-coordinate


def hun(h1, h2):
    window.blit(hunter, (h1, h2))


def player_fox(x, y):
    window.blit(fox, (x, y))


def player_wolf(x, y):
    window.blit(wolf, (x, y))


def show_score_fox(score_value, lvl_A, dt):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    window.blit(score, (680, 0))
    start = font.render("END", True, (0, 0, 0))
    window.blit(start, (337, 800 - 22))
    end = font.render("START", True, (0, 0, 0))
    window.blit(end, (363, 0))
    lvl = font.render("LVL: " + str(lvl_A), True, (0, 0, 0))
    window.blit(lvl, (700, 800 - 22))
    time = font.render("Time: " + str(dt) + " sec", True, (0, 0, 0))
    window.blit(time, (0, 0))


def show_score_wolf(score_value, lvl_B, dt):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    window.blit(score, (680, 0))
    start = font.render("START", True, (0, 0, 0))
    window.blit(start, (337, 800 - 22))
    end = font.render("END", True, (0, 0, 0))
    window.blit(end, (363, 0))
    lvl = font.render("LVL: " + str(lvl_B), True, (0, 0, 0))
    window.blit(lvl, (700, 800 - 22))
    time = font.render("Time: " + str(dt) + " sec", True, (0, 0, 0))
    window.blit(time, (0, 0))


def distance(x1, y1, h, h_y):
    dist = math.sqrt(math.pow(x1 - h, 2) + math.pow(y1 - h_y, 2))
    return dist


# game over
gameover = False


def gameover_message(score_A, score_B, time_A, time_B):

    over = font.render("Game over: E = continue | Q = Quit", True, (0, 0, 0))
    window.blit(over, (200, 0))
    if score_A > score_B:
        mess = font.render("Fox wins", True, (0, 0, 0))
        window.blit(mess, (200, 200))
    elif score_B > score_A:
        mess = font.render("White Wolf wins", True, (0, 0, 0))
        window.blit(mess, (200, 200))
    else:
        if time_A < time_B:
            mess = font.render("Fox wins", True, (0, 0, 0))
            window.blit(mess, (200, 200))
        elif time_B < time_A:
            mess = font.render("White Wolf wins", True, (0, 0, 0))
            window.blit(mess, (200, 200))
        else:
            tie = font.render("Tie", True, (0, 0, 0))
            window.blit(tie, (200, 200))
