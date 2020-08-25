#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: lesson2.py
@time: 2020/08/25
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import pygame
from pygame.locals import *


def demo1():
    pygame.init()
    SCREEN_SIZE = (640, 480)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    font = pygame.font.SysFont('arial', 16)
    font_height = font.get_linesize()
    event_text = []
    pygame.event.set_blocked(MOUSEBUTTONUP)
    pygame.event.set_blocked(MOUSEBUTTONDOWN)
    while True:
        event = pygame.event.wait()
        event_text.append(str(event))
        event_text = event_text[-SCREEN_SIZE[1] // font_height:]
        if event.type == QUIT:
            exit()
        screen.fill((255, 255, 255))
        y = SCREEN_SIZE[1] - font_height
        for text in reversed(event_text):
            screen.blit(font.render(text, True, (0, 0, 0)), (0, y))
            y -= font_height
        pygame.display.update()


def demo2():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    background = pygame.image.load('fugu.png').convert()
    x, y = 0, 0
    mx, my = 0, 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    mx -= 1
                elif event.key == K_RIGHT:
                    mx += 1
                elif event.key == K_UP:
                    my -= 1
                elif event.key == K_DOWN:
                    my += 1
            elif event.type == K_UP:
                mx, my = 0, 0
        x += mx
        y += my
        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))
        pygame.display.update()


if __name__ == '__main__':
    # demo1()
    demo2()
