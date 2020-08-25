#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: lesson3.py 
@time: 2020/08/26
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import pygame
from pygame.locals import *

if __name__ == '__main__':
    pygame.init()
    f = 0
    screen = pygame.display.set_mode((640, 480), f, 32)
    background = pygame.image.load('fugu.png').convert()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                f ^= FULLSCREEN
                screen = pygame.display.set_mode((640, 480), f, 32)
        screen.blit(background, (0, 0))
        pygame.display.update()
