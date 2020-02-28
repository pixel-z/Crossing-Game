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
h1_y = 60+10
h2 = 0
h2_y = 60+10
h3 = 0
h3_y = 150+60+10
h4 = 0
h4_y = 300+60+10
h5 = 0
h5_y = 300+60+10
h6 = 0
h6_y = 450+60+10
h7 = 0
h7_y = 600+60+10

x = 400-60  
y = 0
width = 60
height = 60
vel = 1

# increase in vel of a and b after lvls
vel_fox = 0
vel_wolf = 0

collision1 = 0
collision2 = 1

#initialization of var
flag = 100
score_value = 0
lvl_A = 1
lvl_B = 1

#common fonts
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

#score,lvl and timer
def show_score_fox(score_value,lvl_A,dt):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    window.blit(score, (680, 0))
    start = font.render("END", True, (0, 0, 0))
    window.blit(start, (337, 800-22))
    end = font.render("START", True, (0, 0, 0))
    window.blit(end, (363, 0))
    lvl = font.render("LVL: " + str(lvl_A), True, (0, 0, 0))
    window.blit(lvl, (700, 800-22))
    time = font.render("Time: " + str(dt) + " sec", True, (0, 0, 0))
    window.blit(time, (0, 0))

def show_score_wolf(score_value,lvl_B,dt):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    window.blit(score, (680, 0))
    start = font.render("START", True, (0, 0, 0))
    window.blit(start, (337, 800-22))
    end = font.render("END", True, (0, 0, 0))
    window.blit(end, (363, 0))
    lvl = font.render("LVL: " + str(lvl_B), True, (0, 0, 0))
    window.blit(lvl, (700, 800-22))
    time = font.render("Time: " + str(dt) + " sec", True, (0, 0, 0))
    window.blit(time, (0, 0))


def distance(x1, y1, h, h_y):
    dist = math.sqrt(math.pow(x1-h, 2) + math.pow(y1-h_y, 2))
    return dist

#game over
gameover = False

score_A = 0
score_B = 0
def gameover_message(time_A,time_B):
    over = font.render("Game over: E = continue | Q = Quit", True, (0, 0, 0))
    window.blit(over, (200,0))
    if score_A > score_B:
        mess = font.render("Fox wins", True, (0, 0, 0))
        window.blit(mess,(200,200))
    elif score_B > score_A:
        mess = font.render("White Wolf wins", True, (0, 0, 0))
        window.blit(mess,(200,200))
    else:
        if time_A < time_B:
            mess = font.render("Fox wins", True, (0, 0, 0))
            window.blit(mess,(200,200))
        elif time_B < time_A:
            mess = font.render("White Wolf wins", True, (0, 0, 0))
            window.blit(mess,(200,200))
        else:
            tie = font.render("Tie", True, (0, 0, 0))
            print(score_A,score_B)
            window.blit(tie,(200,200))

            
running = True
while running:

    #game over
    while gameover == True:
        window.fill((255,255,255))
        gameover_message(time_A,time_B)
        pygame.display.update()

        for event in pygame.event.get():    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameover = False
                    running = False
                if event.key == pygame.K_e:
                    gameover = False

    window.fill((0, 0, 255))

    # adding slabs
    pygame.draw.rect(window, (0, 255, 0), (0, 0, 800, height))
    pygame.draw.rect(window, (0, 255, 0), (0, 150, 800, height))
    pygame.draw.rect(window, (0, 255, 0), (0, 300, 800, height))
    pygame.draw.rect(window, (0, 255, 0), (0, 450, 800, height))
    pygame.draw.rect(window, (0, 255, 0), (0, 600, 800, height))
    pygame.draw.rect(window, (0, 255, 0), (0, 750, 800, height))

    # fixed obstacles
    window.blit(obstacle, (150, 600))
    window.blit(obstacle, (650, 600))
    window.blit(obstacle, (40, 450))
    window.blit(obstacle, (400, 450))
    window.blit(obstacle, (650, 300))
    window.blit(obstacle, (250, 300))
    window.blit(obstacle, (200, 150))
    window.blit(obstacle, (500, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #timer
    t1 = time.time()
    dt = math.floor(t1 - t0) 

    ##################################################################################################################

    if collision2 == 1:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 800 - vel - width:
            x += vel
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 800 - height - vel:
            y += vel

        # speed of hunters and repetition of them
        h1 += 1 + vel_fox
        if h1 > 800:
            h1 = 0
        h2 -= 1 + vel_fox
        if h2 < -60:
            h2 = 800
        h3 -= 0.8 + vel_fox
        if h3 < -60:
            h3 = 800
        h4 += 0.9 + vel_fox
        if h4 > 800:
            h4 = 0
        h5 += 0.5 + vel_fox
        if h5 > 800:
            h5 = 0
        h6 += 0.7 + vel_fox
        if h6 > 800:
            h6 = 0
        h7 += 0.5 + vel_fox
        if h7 > 800:
            h7 = 0

        hun(h1, h1_y)         # hunter in 1
        hun(h2, h2_y)         # hunter in 1
        hun(h3, h3_y)         # hunter in 2
        hun(h4, h4_y)         # hunter in 3
        hun(h5, h5_y)         # hunter in 3
        hun(h6, h6_y)         # hunter in 4
        hun(h7, h7_y)         # hunter in 5
        player_fox(x, y)      # function for player_fox


        # score
        if y > 30 and flag < 1:
            flag = 1
            score_value += 10
        elif y > 75+30 and flag < 2:
            flag = 2
            score_value += 10
        elif y > 150+30 and flag < 3:
            flag = 3
            score_value += 10
        elif y > 150+75+30 and flag < 4:
            flag = 4
            score_value += 10
        elif y > 300+30 and flag < 5:
            flag = 5
            score_value += 10
        elif y > 375+30 and flag < 6:
            flag = 6
            score_value += 10
        elif y > 450+30 and flag < 7:
            flag = 7
            score_value += 10
        elif y > 450+75+30 and flag < 8:
            flag = 8
            score_value += 10
        elif y > 600+30 and flag < 9:
            flag = 9
            score_value += 10
        elif y > 675+30 and flag < 10:
            flag = 10
            score_value += 10

        #end point
        if y > 800-90:
            x = 400-60
            y = 800-60
            collision1 = 1
            collision2 = 0
            score_A = score_value
            score_value = 0 
            vel_fox += 0.2
            lvl_A += 1
            t0 = t1
            time_A = t1 - t0

        # collision
        x1 = x + 30
        y1 = y + 30
        if distance(x1, y1, h1+30, h1_y+30) < 51 or distance(x1, y1, h2+30, h2_y+30) < 51 or distance(x1, y1, h3+30, h3_y+30) < 51:
            x = 400-60
            y = 800-60
            collision1 = 1
            collision2 = 0
            score_A = score_value
            score_value = 0 
            vel_fox = 0
            lvl_A = 1
            t0 = t1
            time_A = t1 - t0

        if distance(x1, y1, h4+30, h4_y+30) < 51 or distance(x1, y1, h5+30, h5_y+30) < 51 or distance(x1, y1, h6+30, h6_y+30) < 51:
            x = 400-60
            y = 800-60
            collision1 = 1
            collision2 = 0
            score_A = score_value
            score_value = 0 
            vel_fox = 0
            lvl_A = 1
            t0 = t1
            time_A = t1 - t0
            
        if distance(x1, y1, h7+30, h7_y+30) < 51 or distance(x1, y1, 150+30, 600+30) < 51 or distance(x1, y1, 650+30, 600+30) < 51:
            x = 400-60
            y = 800-60
            collision1 = 1
            collision2 = 0
            score_A = score_value
            score_value = 0 
            vel_fox = 0
            lvl_A = 1
            t0 = t1
        if distance(x1, y1, 40+30, 450+30) < 51 or distance(x1, y1, 400+30, 450+30) < 51 or distance(x1, y1, 650+30, 300+30) < 51:
            x = 400-60
            y = 800-60
            collision1 = 1
            collision2 = 0
            score_A = score_value
            score_value = 0 
            vel_fox = 0
            lvl_A = 1
            t0 = t1
            time_A = t1 - t0
        if distance(x1, y1, 250+30, 300+30) < 51 or distance(x1, y1, 200+30, 150+30) < 51 or distance(x1, y1, 500+30, 150+30) < 51:
            x = 400-60
            y = 800-60
            collision1 = 1
            collision2 = 0
            score_A = score_value
            score_value = 0 
            vel_fox = 0
            lvl_A = 1
            t0 = t1
            time_A = t1 - t0

        show_score_fox(score_value,lvl_A,dt)

#################################################################################################################################

    if collision1 == 1:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and x > vel:
            x -= vel
        if keys[pygame.K_d] and x < 800 - vel - width:
            x += vel
        if keys[pygame.K_w] and y > vel:
            y -= vel
        if keys[pygame.K_s] and y < 800 - height - vel:
            y += vel

        # speed of hunters and repetition of them
        h1 += 1 + vel_wolf
        if h1 > 800:
            h1 = 0
        h2 -= 1 + vel_wolf
        if h2 < -60:
            h2 = 800
        h3 -= 0.8 + vel_wolf
        if h3 < -60:
            h3 = 800
        h4 += 0.9 + vel_wolf
        if h4 > 800:
            h4 = 0
        h5 += 0.5 + vel_wolf
        if h5 > 800:
            h5 = 0
        h6 += 0.7 + vel_wolf
        if h6 > 800:
            h6 = 0
        h7 += 0.5 + vel_wolf
        if h7 > 800:
            h7 = 0

        player_wolf(x, y)     # function for player_wolf
        hun(h1, h1_y)         # hunter in 1
        hun(h2, h2_y)         # hunter in 1
        hun(h3, h3_y)         # hunter in 2
        hun(h4, h4_y)         # hunter in 3
        hun(h5, h5_y)         # hunter in 3
        hun(h6, h6_y)         # hunter in 4
        hun(h7, h7_y)         # hunter in 5

        # score
        if y < 30 and flag > 1:
            flag = 1
            score_value += 10
        elif y < 75+30 and flag > 2:
            flag = 2
            score_value += 10
        elif y < 150+30 and flag > 3:
            flag = 3
            score_value += 10
        elif y < 150+75+30 and flag > 4:
            flag = 4
            score_value += 10
        elif y < 300+30 and flag > 5:
            flag = 5
            score_value += 10
        elif y < 375+30 and flag > 6:
            flag = 6
            score_value += 10
        elif y < 450+30 and flag > 7:
            flag = 7
            score_value += 10
        elif y < 450+75+30 and flag > 8:
            flag = 8
            score_value += 10
        elif y < 600+30 and flag > 9:
            flag = 9
            score_value += 10
        elif y < 675+30 and flag > 10:
            flag = 10
            score_value += 10

        # end point
        if y <= 30:
            x = 400-60
            y = 0
            collision1 = 0
            collision2 = 1
            score_value = 0 
            vel_wolf += 0.2
            lvl_B += 1
            t0 = t1
            gameover = True
            time_B = t1 - t0
            score_B = score_value

        # collision
        x1 = x + 30
        y1 = y + 30
        if distance(x1, y1, h1+30, h1_y+30) < 51 or distance(x1, y1, h2+30, h2_y+30) < 51 or distance(x1, y1, h3+30, h3_y+30) < 51:
            x = 400-60
            y = 0
            collision2 = 1
            collision1 = 0
            score_B = score_value
            score_value = 0 
            vel_wolf = 0
            lvl_B = 1
            t0 = t1
            gameover = True
            time_B = t1 - t0
        if distance(x1, y1, h4+30, h4_y+30) < 51 or distance(x1, y1, h5+30, h5_y+30) < 51 or distance(x1, y1, h6+30, h6_y+30) < 51:
            x = 400-60
            y = 0
            collision2 = 1
            collision1 = 0
            score_B = score_value
            score_value = 0 
            vel_wolf = 0
            lvl_B = 1
            t0 = t1
            gameover = True
            time_B = t1 - t0
        if distance(x1, y1, h7+30, h7_y+30) < 51 or distance(x1, y1, 150+30, 600+30) < 51 or distance(x1, y1, 650+30, 600+30) < 51:
            x = 400-60
            y = 0
            collision2 = 1
            collision1 = 0
            score_B = score_value
            score_value = 0 
            vel_wolf = 0
            lvl_B = 1
            t0 = t1
            gameover = True
            time_B = t1 - t0
        if distance(x1, y1, 40+30, 450+30) < 51 or distance(x1, y1, 400+30, 450+30) < 51 or distance(x1, y1, 650+30, 300+30) < 51:
            x = 400-60
            y = 0
            collision2 = 1
            collision1 = 0
            score_B = score_value
            score_value = 0 
            vel_wolf = 0
            lvl_B = 1
            t0 = t1
            gameover = True
            time_B = t1 - t0
        if distance(x1, y1, 250+30, 300+30) < 51 or distance(x1, y1, 200+30, 150+30) < 51 or distance(x1, y1, 500+30, 150+30) < 51:
            x = 400-60
            y = 0
            collision2 = 1
            collision1 = 0
            score_B = score_value
            score_value = 0 
            vel_wolf = 0
            lvl_B = 1
            t0 = t1
            gameover = True
            time_B = t1 - t0

        show_score_wolf(score_value,lvl_B,dt)
    pygame.display.update()
