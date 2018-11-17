# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:GameObject.py
@time:2018/11/15 15:28
"""

import pygame

from SiriGame.GameSource import GameSource


class GameObject:

    def __init__(self, width=640, hight=480):
        pygame.mixer.pre_init(44100, 16, 2, 1024 * 4)
        pygame.init()

        self.WIN_WIDTH = width
        self.WIN_HIGHT = hight

        self.screen = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HIGHT), 0, 32)
        self.source = GameSource()
        self.clock = pygame.time.Clock()

    def setCaption(self, title):
        pygame.display.set_caption(title)

    def setIcon(self, icon):
        pygame.display.set_icon(icon)

    def quit(self):
        pygame.quit()
