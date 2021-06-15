from variables import *
import pygame
from pygame.locals import *
from pygame.rect import *
import sys

def up_act():
    global LAST_ACTION
    head = snack_body[-1]
    snack_body.append([head[0], head[1] - SIZE_RECT])
    snack_body.pop(0)
    LAST_ACTION = pygame.K_UP

def down_act():

    head = snack_body[-1]
    snack_body.append([head[0], head[1] + SIZE_RECT])
    snack_body.pop(0)
    LAST_ACTION = pygame.K_DOWN



def left_act():

    head = snack_body[-1]
    snack_body.append([head[0] - SIZE_RECT, head[1]])
    snack_body.pop(0)
    LAST_ACTION = pygame.K_LEFT

def right_act():
    head = snack_body[-1]
    snack_body.append([head[0] + SIZE_RECT, head[1]])
    snack_body.pop(0)
    LAST_ACTION = pygame.K_RIGHT
    

def updae_body():
    if LAST_ACTION == pygame.K_UP:
        up_act()
    if LAST_ACTION == pygame.K_DOWN:
       down_act()
    if LAST_ACTION == pygame.K_RIGHT:
        right_act()
    if LAST_ACTION == pygame.K_LEFT:
        left_act()

