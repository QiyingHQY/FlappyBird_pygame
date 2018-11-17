# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:Button.py
@time:2018/11/16 11:24
"""
import pygame
from pygame.locals import *

from SiriGame.GUI.Widget import Widget


class Button(Widget):

    def __init__(self, father, x=0, y=0, w=100, h=30):

        super().__init__(father, x, y, w, h)

        self.border = 3

        self.img_nomal = None
        self.img_on = None
        self.img_pressed = None

        """
        Button state
            0:normal
            1:mouse_on
            2:pressed
        """
        self.state = 0
        self.connect = None

    def event(self, events):

        if not self.isHide:
            if self.isOn():
                if self.state == 0:
                    self.state = 1
                for event in events:
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.state = 3
                            break

                    if event.type == MOUSEBUTTONUP and event.button == 1 and self.state == 3:
                        self.state = 1
                        break
            else:
                self.state = 0

    def update(self):
        if not self.isHide:
            pass

    def render(self):

        if not self.isHide:
            if self.state == 0:
                self.render_normal()
            elif self.state == 1:
                self.render_on()
            else:
                self.render_pressed()

    def render_normal(self):
        if self.img_nomal == None:
            pygame.draw.rect(self.screen, (255, 255, 255), ((self.x, self.y), (self.w, self.h)), 0)
        else:
            self.screen.blit(self.img_nomal, (self.x, self.y))

    def render_on(self):
        if self.img_on == None:
            pygame.draw.rect(self.screen, (0, 255, 255), (
                (self.x - self.border, self.y - self.border), (self.w + self.border * 2, self.h + self.border * 2)), 0)
            pygame.draw.rect(self.screen, (255, 255, 255), ((self.x, self.y), (self.w, self.h)), 0)
        else:
            self.screen.blit(self.img_on, (self.x, self.y))

    def render_pressed(self):
        if self.img_pressed == None:
            pygame.draw.rect(self.screen, (220, 220, 220), ((self.x, self.y), (self.w, self.h)), 0)
        else:
            self.screen.blit(self.img_pressed, (self.x, self.y))

    def isOn(self):
        x, y = pygame.mouse.get_pos()

        if x > self.x and x < self.x + self.w \
                and y > self.y and y < self.y + self.h:
            return True
        return False

    def setBorder(self, arg):
        self.border = arg

    def setImg(self, normal, on=None, pressed=None):
        self.img_nomal = normal

        if on == None:
            self.img_on = normal
        else:
            self.img_on = on

        if pressed == None:
            self.img_pressed = normal
        else:
            self.img_pressed = pressed

    def Connect(self, fun):
        self.connect = fun
