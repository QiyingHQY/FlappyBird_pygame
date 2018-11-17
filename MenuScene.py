# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:MenuScene.py
@time:2018/11/15 21:21
"""
from random import randint

import pygame
from pygame.locals import *

from PlayScene import PlayScene
from SiriGame import GameScene
from SiriGame.GUI import Button


class MenuScene(GameScene):

    def __init__(self, gameobj):

        super().__init__(gameobj)

        self.playScene = PlayScene(gameobj)

        self.btn_start = Button(self, 35, 350, 140, 78)
        self.btn_start.setImg(self.source.img_button_start, self.source.img_button_start_on,
                              self.source.img_button_start_pressed)

        self.btn_rank = Button(self, 210, 350, 140, 78)
        self.btn_rank.setImg(self.source.img_button_rank, self.source.img_button_rank_on,
                             self.source.img_button_rank_pressed)

        self.isDay=True
        self.groundPos = 384

        self.init()

    def init(self,args=None):
        self.dayOrNight()

    def event(self, events):
        super().event(events)

        for event in events:
            if event.type == QUIT:
                self.isQuit = True

            if event.type==KEYDOWN:
                self.keyDownEvent(event)

            if event.type==MOUSEBUTTONDOWN:
                self.mouseDownEvent(event)

    def keyDownEvent(self, event):
        if event.key == K_ESCAPE:
            self.isQuit = True

    def mouseDownEvent(self, event):
        if event.button == 1:
            if self.btn_start.isOn():
                self.isQuit,self.isDay = self.playScene.run(self.isDay)

    def update(self):
        super().update()

        if self.groundPos > 0:
            self.groundPos -= 2
        else:
            self.groundPos = 384

    def render(self):

        if self.isDay:
            self.screen.blit(self.source.img_day, (0, 0))
        else:
            self.screen.blit(self.source.img_night, (0, 0))

        self.screen.blit(self.source.img_logo, (73, 150))

        self.btn_start.render()
        self.btn_rank.render()

        self.screen.blit(self.source.img_ground, (self.groundPos - 384, 448))
        self.screen.blit(self.source.img_ground, (self.groundPos, 448))

    def dayOrNight(self):
        if randint(0, 20)%2==0:
            self.isDay=not self.isDay