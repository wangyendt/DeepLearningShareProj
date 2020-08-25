#!/usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:  wangye
@file: lesson5.py 
@time: 2020/08/26
@contact: wangye.hope@gmail.com
@site:  
@software: PyCharm 
"""

import pygame
from pygame.locals import *
from sys import exit


def demo1():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))

    all_colors = pygame.Surface((4096, 4096), depth=24)

    for r in range(256):
        print(r + 1, "out of 256")
        x = (r & 15) * 256
        y = (r >> 4) * 256
        for g in range(256):
            for b in range(256):
                all_colors.set_at((x + g, y + b), (r, g, b))

    pygame.image.save(all_colors, "allcolors.bmp")


def demo2():
    pygame.init()

    screen = pygame.display.set_mode((640, 480), 0, 32)

    def create_scales(height):
        red_scale_surface = pygame.surface.Surface((640, height))
        green_scale_surface = pygame.surface.Surface((640, height))
        blue_scale_surface = pygame.surface.Surface((640, height))
        for x in range(640):
            c = int((x / 640.) * 255.)
            red = (c, 0, 0)
            green = (0, c, 0)
            blue = (0, 0, c)
            line_rect = Rect(x, 0, 1, height)
            pygame.draw.rect(red_scale_surface, red, line_rect)
            pygame.draw.rect(green_scale_surface, green, line_rect)
            pygame.draw.rect(blue_scale_surface, blue, line_rect)
        return red_scale_surface, green_scale_surface, blue_scale_surface

    red_scale, green_scale, blue_scale = create_scales(80)

    color = [127, 127, 127]

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        screen.fill((0, 0, 0))

        screen.blit(red_scale, (0, 00))
        screen.blit(green_scale, (0, 80))
        screen.blit(blue_scale, (0, 160))

        x, y = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            for component in range(3):
                if y > component * 80 and y < (component + 1) * 80:
                    color[component] = int((x / 639.) * 255.)
            pygame.display.set_caption("PyGame Color Test - " + str(tuple(color)))

        for component in range(3):
            pos = (int((color[component] / 255.) * 639), component * 80 + 40)
            pygame.draw.circle(screen, (255, 255, 255), pos, 20)

        pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))

        pygame.display.update()


def demo3():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)

    color1 = (221, 99, 20)
    color2 = (96, 130, 51)
    factor = 0.

    def blend_color(color1, color2, blend_factor):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        r = r1 + (r2 - r1) * blend_factor
        g = g1 + (g2 - g1) * blend_factor
        b = b1 + (b2 - b1) * blend_factor
        return int(r), int(g), int(b)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        screen.fill((255, 255, 255))

        tri = [(0, 120), (639, 100), (639, 140)]
        pygame.draw.polygon(screen, (0, 255, 0), tri)
        pygame.draw.circle(screen, (0, 0, 0), (int(factor * 639.0), 120), 10)

        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            factor = x / 639.0
            pygame.display.set_caption("Pygame Color Blend Test - %.3f" % factor)

        color = blend_color(color1, color2, factor)
        pygame.draw.rect(screen, color, (0, 240, 640, 240))

        pygame.display.update()


# demo1()
# demo2()
demo3()
