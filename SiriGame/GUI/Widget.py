# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:Widget.py
@time:2018/11/16 12:31
"""

class Widget():

    def __init__(self,father,x=0,y=0,w=100,h=30):
        self.father=father
        self.father.objList.append(self)
        self.screen=father.screen

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.isHide=False

    def event(self,events):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def setPosition(self,x,y):
        self.x=x
        self.y=y

    def getPosition(self):
        return self.x,self.y

    def setSize(self,w,h):
        self.w=w
        self.h=h

    def getSize(self):
        return self.w,self.h

    def setHide(self,arg):
        self.isHide=arg

    def getHide(self):
        return self.isHide