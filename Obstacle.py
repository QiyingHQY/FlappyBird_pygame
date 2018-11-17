# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:Obstacle.py
@time:2018/11/17 13:53
"""
from random import randint

from pygame.locals import *

from SiriGame import GameEntity, State


class Obstacle(GameEntity):

    def __init__(self, father, x):
        super().__init__(father)

        self.x = x
        self.y = 0
        self.w = 70
        self.h = 250

        self.speed = 2

        """
        obstacle state:
            0:ready
            1:play
            2:dead
        """
        self.state = 0

        self.isPause = True

        state_move = ObstacleStateMove(self)
        state_reset = ObstacleStateReset(self)
        state_pause = ObstacleStatePause(self)
        state_stop = ObstacleStateStop(self)
        self.stateMachine.add_state(state_move)
        self.stateMachine.add_state(state_reset)
        self.stateMachine.add_state(state_pause)
        self.stateMachine.add_state(state_stop)

    def init(self):
        self.state = 0
        self.isPause = True
        self.randPos()

    def event(self, events):

        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                self.mouseDownEvent(event)

    def mouseDownEvent(self, event):

        if event.button == 1:
            if self.state==0:
                self.state = 1
                self.isPause = False
                self.stateMachine.set_state("move")
        elif event.button == 3:
            if self.state == 1:
                self.isPause = not self.isPause

    def render(self):
        self.screen.blit(self.father.source.img_obstacle_up, (self.x, self.y))
        self.screen.blit(self.father.source.img_obstacle_down, (self.x, self.y - 400))

    def randPos(self):
        self.y = randint(0, 200) + 200

    def isIn(self, x, y, w,h):
        if x+w>self.x and x<self.x:
            if y+h/2>self.y or y<self.y-150:
                return True


class ObstacleStateMove(State):

    def __init__(self, obstacle):
        super().__init__("move")
        self.obstacle = obstacle

    def check_conditions(self):
        if self.obstacle.isPause:
            return "pause"

        if self.obstacle.x < -70:
            return "reset"

    def entry_actions(self):
        self.obstacle.state=1

    def do_actions(self):
        self.obstacle.x -= self.obstacle.speed

    def exit_actions(self):
        pass


class ObstacleStateReset(State):

    def __init__(self, obstacle):
        super().__init__("reset")
        self.obstacle = obstacle

    def check_conditions(self):
        return "move"

    def entry_actions(self):
        self.obstacle.x = 650
        self.obstacle.randPos()

    def do_actions(self):
        pass

    def exit_actions(self):
        pass


class ObstacleStatePause(State):

    def __init__(self, obstacle):
        super().__init__("pause")
        self.obstacle = obstacle

    def check_conditions(self):
        if self.obstacle.isPause == False:
            return "move"

    def entry_actions(self):
        pass

    def do_actions(self):
        pass

    def exit_actions(self):
        pass

class ObstacleStateStop(State):

    def __init__(self, obstacle):
        super().__init__("stop")
        self.obstacle = obstacle

    def check_conditions(self):
        pass

    def entry_actions(self):
        self.obstacle.state=2

    def do_actions(self):
        pass

    def exit_actions(self):
        pass
