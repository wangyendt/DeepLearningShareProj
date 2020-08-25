#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: lesson1.py
@time: 2020/08/25
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import pygame
from pygame.locals import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480), RESIZABLE, 32)
    pygame.display.set_caption('Hello World!')
    background = pygame.image.load('sushiplate.jpg').convert()
    mouse_cursor = pygame.image.load('fugu.png').convert_alpha()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.blit(background, (0, 0))
        x, y = pygame.mouse.get_pos()
        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2
        screen.blit(mouse_cursor, (x, y))
        pygame.display.update()
