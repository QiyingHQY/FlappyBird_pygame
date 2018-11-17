# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:GameScene.py
@time:2018/11/15 21:23
"""
import pygame
from pygame.locals import *


class GameScene():

    def __init__(self, gameobj):

        self.gameObj = gameobj
        self.screen = gameobj.screen
        self.source = gameobj.source
        self.clock = self.gameObj.clock

        self.FPS = 60
        self.isEnd = False
        self.isQuit = False

        self.objList = []

        self.returnArg=[]

    def init(self,args):
        self.isEnd = False
        self.isQuit = False

    def run(self,args=None):

        self.init(args)

        while (True):

            self.event(pygame.event.get())

            self.update()

            self.render()

            self.delay()

            if self.isend():
                break

        self.quite()
        return self.returnArg

    def delay(self):
        self.clock.tick(self.FPS)

    def event(self, events):
        for event in events:
            if event.type == QUIT:
                self.isQuit = True

        lenth = len(self.objList)
        if lenth > 0:
            for i in range(lenth):
                self.objList[lenth - 1 - i].event(events)


    def update(self):
        pygame.display.update()

        lenth = len(self.objList)
        if lenth > 0:
            for i in range(lenth):
                self.objList[lenth - 1 - i].update()


    def render(self):
        pass

    def isend(self):
        return self.isEnd|self.isQuit

    def quite(self):
        self.returnArg.clear()
        self.returnArg.append(self.isQuit)
