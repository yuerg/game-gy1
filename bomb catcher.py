# coding=utf-8

import pygame
from pygame.locals import *
import sys, random, time, math

pygame.init()

def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('懒得看技术的李开复')
font1 = pygame.font.Font(None, 24)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220, 50, 50
yellow = 230,230,230
black = 0,0,0

lives = 3
score = 0
game_over = True
mouse_x = mouse_y = 0
pos_x = 0
pos_y = 560
bomb_x = 3
bomb_y = 5
vel_y = 4
vel_x = 4
count = 1


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            move_x, move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = 3
                score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    screen.fill((0,0,100))
    if game_over:
        bomb_x = 1
        bomb_y = 5
        print_text(font1, 100, 200, "<click to play>")
    else:
        # move the bomb


        bomb_y += vel_y
        bomb_x += vel_x
        # if (bomb_x + bomb_x + 12) / 2 >= pos_x and (bomb_x + bomb_x + 12) / 2 < pos_x + 120:
        #     filter = True
        # else:
        #     filter = False
        #     game_over = True
        #     lives = -1
        #     if lives == 0:
        #         game_over = True


        if bomb_y >= 520:
            if (bomb_x + bomb_x + 12) / 2 >= pos_x and (bomb_x + bomb_x + 12) / 2 < pos_x + 120:
                filter = True
                score += 10
                count += 1
            else:
                filter = False
                game_over = True

        if count % 3 == 0:
            vel_x += (math.log(count, 10) + 1)
            vel_y += (math.log(count, 10) + 1)
        if (bomb_y > 520 or bomb_y <= 4):
            # bomb_x = random.randint(0, 500)
            vel_y = -vel_y

        if (bomb_x < 0 or bomb_x > 750):
            vel_x = - vel_x

        # if bomb_y > 560:
        #     if bomb_x > pos_x and bomb_x < pos_x + 120:
        #         score += 10
        #         bomb_x = random.randint(0, 500)
        #         bomb_y = -50

        pygame.draw.circle(screen, black, (int(bomb_x)-4,int(bomb_y-4)), 30, 0)
        pygame.draw.circle(screen, yellow, (int(bomb_x),int(bomb_y)), 30, 0)

        if keys[K_LSHIFT]:
            shift = 2
        else:
            shift = 1
        if keys[K_LEFT]:
            pos_x -= 6 / shift
        if keys[K_RIGHT]:
            pos_x += 6 / shift
        # pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 600:
            pos_x = 600
        pygame.draw.rect(screen, black, (pos_x-4,pos_y-4,120,40), 0)
        pygame.draw.rect(screen, red, (pos_x,pos_y,120, 40), 0)
    print_text(font1, 0, 0, "LIVES: " + str(lives))
    print_text(font1, 500, 0, "SCORES: " + str(score))

    pygame.display.update()