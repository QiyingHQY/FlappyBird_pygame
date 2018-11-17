# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:PlayScene.py
@time:2018/11/16 19:45
"""
from random import randint

import pygame
from pygame.locals import *

from Bird import Bird
from Obstacle import Obstacle
from SiriGame import GameScene


class PlayScene(GameScene):

    def __init__(self, gameobj):

        super().__init__(gameobj)

        self.bird = Bird(self)

        self.obstacleList = [Obstacle(self, 700), Obstacle(self, 940), Obstacle(self, 1180)]

        """
        Game state
            0:resady
            1:playing
            2:dead
        """
        self.state = 0

        self.score=0

        self.isPause = False
        self.isDay = True
        self.groundPos = 384

    def init(self, args=None):
        self.groundPos = 384
        self.isEnd = False
        self.isQuit = False

        if args != None:
            self.isDay = args
        else:
            self.dayOrNight()

        self.initGame()

    def initGame(self):
        self.state = 0
        self.score = 0

        self.bird.init()

        for i in range(len(self.obstacleList)):
            self.obstacleList[i].x = 700 + i * 240
            self.obstacleList[i].init()

    def event(self, events):
        super().event(events)

        for event in events:
            if event.type == QUIT:
                self.isQuit = True

            if event.type == KEYDOWN:
                self.keyDownEvent(event)

            if event.type == MOUSEBUTTONDOWN:
                self.mouseDownEvent(event)

    def keyDownEvent(self, event):
        if event.key == K_ESCAPE:
            self.isEnd = True

    def mouseDownEvent(self, event):
        if event.button == 1:
            if self.state == 0:
                self.state = 1
                for i in self.obstacleList:
                    i.isPause = False
            if self.state == 1:
                if self.isPause:
                    self.isPause = False
        elif event.button == 3:
            self.event_pause()

    def event_pause(self):
        if self.state == 1:
            self.isPause = not self.isPause

    def update(self):
        super().update()

        if self.state == 1:
            if self.isDead():
                self.bird.stateMachine.set_state("dead")
                for i in self.obstacleList:
                    i.stateMachine.set_state("stop")
                self.state = 2
        elif self.state == 2:
            self.update_dead()

        self.update_ground()

    def update_dead(self):
        if self.bird.y == 410:
            pass

    def update_ground(self):
        if self.state != 2:
            if not self.isPause:
                if self.groundPos > 0:
                    self.groundPos -= 2
                else:
                    self.groundPos = 384

    def render(self):

        if self.state == 0:
            self.render_guide()
        else:
            self.render_background()

        for i in self.obstacleList:
            i.render()

        self.bird.render()

        self.screen.blit(self.source.img_ground, (self.groundPos - 384, 448))
        self.screen.blit(self.source.img_ground, (self.groundPos, 448))

    def render_guide(self):

        if self.isDay:
            self.screen.blit(self.source.img_guide_day, (0, 0))
        else:
            self.screen.blit(self.source.img_guide_night, (0, 0))

    def render_background(self):

        if self.isDay:
            self.screen.blit(self.source.img_day, (0, 0))
        else:
            self.screen.blit(self.source.img_night, (0, 0))

    def dayOrNight(self):
        if randint(0, 20) % 2 == 0:
            self.isDay = not self.isDay

    def isDead(self):
        if self.bird.y >= 410:
            return True
        for i in self.obstacleList:
            if i.isIn(self.bird.x, self.bird.y, self.bird.w, self.bird.h):
                return True

    def quite(self):
        super().quite()

        self.returnArg.append(self.isDay)
