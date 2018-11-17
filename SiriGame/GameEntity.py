# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:GameEntity.py
@time:2018/11/16 20:53
"""
from SiriGame.StateMachine import StateMachine


class GameEntity():

    def __init__(self,father):
        self.father=father
        self.father.objList.append(self)
        self.screen=father.screen
        self.stateMachine=StateMachine()

    def event(self,events):
        pass

    def update(self):
        self.stateMachine.update()

    def render(self):
        pass
