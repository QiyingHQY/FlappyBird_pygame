# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:Bird.py
@time:2018/11/16 21:00
"""
from random import randint

from pygame.locals import *

from SiriGame import GameEntity, State


class Bird(GameEntity):

    def __init__(self, father):
        super().__init__(father)

        self.x = 0
        self.y = 0
        self.w = 45
        self.h = 45

        self.orgSpeed = -8
        self.speed = 0
        self.acceleration = 0.6

        """
        bird color
            0:blue
            1:red
            2:green
            3:yellow
        """
        self.color = 0
        self.timeCount = 0
        self.countSpeed = 2
        """
        bird state
            0:keep
            1:up
            2:mid
            3:down
            4:dead
        """
        self.state = 0
        self.isPause = False

        state_up = BirdStateUp(self)
        state_mid = BirdStateMid(self)
        state_down = BirdStateDown(self)
        state_keep = BirdStateKeep(self)
        state_dead = BirdStateDead(self)
        state_pause = BirdStatePause(self)
        self.stateMachine.add_state(state_up)
        self.stateMachine.add_state(state_mid)
        self.stateMachine.add_state(state_down)
        self.stateMachine.add_state(state_keep)
        self.stateMachine.add_state(state_dead)
        self.stateMachine.add_state(state_pause)

        self.imgList_up = [[father.source.img_bird_blue_up_up, father.source.img_bird_blue_up_mid,
                            father.source.img_bird_blue_up_down, father.source.img_bird_blue_up_mid],
                           [father.source.img_bird_red_up_up, father.source.img_bird_red_up_mid,
                            father.source.img_bird_red_up_down, father.source.img_bird_red_up_mid],
                           [father.source.img_bird_green_up_up, father.source.img_bird_green_up_mid,
                            father.source.img_bird_green_up_down, father.source.img_bird_green_up_mid],
                           [father.source.img_bird_yellow_up_up, father.source.img_bird_yellow_up_mid,
                            father.source.img_bird_yellow_up_down, father.source.img_bird_yellow_up_mid]]
        self.imgList_mid = [[father.source.img_bird_blue_mid_up, father.source.img_bird_blue_mid_mid,
                             father.source.img_bird_blue_mid_down, father.source.img_bird_blue_mid_mid],
                            [father.source.img_bird_red_mid_up, father.source.img_bird_red_mid_mid,
                             father.source.img_bird_red_mid_down, father.source.img_bird_red_mid_mid],
                            [father.source.img_bird_green_mid_up, father.source.img_bird_green_mid_mid,
                             father.source.img_bird_green_mid_down, father.source.img_bird_green_mid_mid],
                            [father.source.img_bird_yellow_mid_up, father.source.img_bird_yellow_mid_mid,
                             father.source.img_bird_yellow_mid_down, father.source.img_bird_yellow_mid_mid]]
        self.imgList_down = [[father.source.img_bird_blue_down_up, father.source.img_bird_blue_down_mid,
                              father.source.img_bird_blue_down_down, father.source.img_bird_blue_down_mid],
                             [father.source.img_bird_red_down_up, father.source.img_bird_red_down_mid,
                              father.source.img_bird_red_down_down, father.source.img_bird_red_down_mid],
                             [father.source.img_bird_green_down_up, father.source.img_bird_green_down_mid,
                              father.source.img_bird_green_down_down, father.source.img_bird_green_down_mid],
                             [father.source.img_bird_yellow_down_up, father.source.img_bird_yellow_down_mid,
                              father.source.img_bird_yellow_down_down, father.source.img_bird_yellow_down_mid]]
        self.imgList_dead = [[father.source.img_bird_blue_dead_up, father.source.img_bird_blue_dead_mid,
                              father.source.img_bird_blue_dead_down, father.source.img_bird_blue_dead_mid],
                             [father.source.img_bird_red_dead_up, father.source.img_bird_red_dead_mid,
                              father.source.img_bird_red_dead_down, father.source.img_bird_red_dead_mid],
                             [father.source.img_bird_green_dead_up, father.source.img_bird_green_dead_mid,
                              father.source.img_bird_green_dead_down, father.source.img_bird_green_dead_mid],
                             [father.source.img_bird_yellow_dead_up, father.source.img_bird_yellow_dead_mid,
                              father.source.img_bird_yellow_dead_down, father.source.img_bird_yellow_dead_mid]]

    def init(self):
        self.stateMachine.set_state("keep")
        self.randColor()
        self.x = 100
        self.y = 250
        self.speed = self.orgSpeed
        self.state = 0
        self.isPause = False

    def event(self, events):

        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                self.mouseDownEvent(event)

    def mouseDownEvent(self, event):
        if self.state != 0:
            if event.button == 1:
                if self.state != 4:
                    if self.isPause:
                        self.isPause = False
                    self.stateMachine.set_state("up")

            elif event.button == 3:
                if self.state != 0 and self.state != 4:
                    self.isPause = not self.isPause

    def render(self):
        if self.state == 0:
            self.render_keep()
        elif self.state == 1:
            self.render_up()
        elif self.state == 2:
            self.render_mid()
        elif self.state == 3:
            self.render_down()
        elif self.state == 4:
            self.render_dead()

    def render_keep(self):
        self.screen.blit(self.imgList_mid[self.color][int(self.timeCount / 15)], (self.x, self.y))

    def render_up(self):
        self.screen.blit(self.imgList_up[self.color][int(self.timeCount / 15)], (self.x, self.y))

    def render_mid(self):
        self.screen.blit(self.imgList_mid[self.color][int(self.timeCount / 15)], (self.x, self.y))

    def render_down(self):
        self.screen.blit(self.imgList_down[self.color][int(self.timeCount / 15)], (self.x, self.y))

    def render_dead(self):
        self.screen.blit(self.imgList_dead[self.color][int(self.timeCount / 15)], (self.x + 20, self.y))

    def randColor(self):
        self.color = randint(0, 3)


class BirdStateUp(State):

    def __init__(self, bird):
        super().__init__("up")
        self.bird = bird
        self.count = 20

    def check_conditions(self):
        if self.bird.isPause:
            return "pause"
        if self.count <= 0:
            return "mid"

    def entry_actions(self):
        self.bird.state = 1
        self.bird.speed = self.bird.orgSpeed
        self.count = 20

    def do_actions(self):
        self.bird.timeCount += self.bird.countSpeed
        self.bird.timeCount %= 60
        self.bird.speed += self.bird.acceleration
        self.bird.y += self.bird.speed
        self.count -= 1

    def exit_actions(self):
        pass


class BirdStateMid(State):

    def __init__(self, bird):
        super().__init__("mid")
        self.bird = bird
        self.count = 10

    def check_conditions(self):
        if self.bird.isPause:
            return "pause"
        if self.count <= 0:
            return "down"

    def entry_actions(self):
        self.bird.state = 2
        self.count = 10

    def do_actions(self):
        self.bird.timeCount += self.bird.countSpeed
        self.bird.timeCount %= 60
        self.bird.speed += self.bird.acceleration
        self.bird.y += self.bird.speed
        self.count -= 1

    def exit_actions(self):
        pass


class BirdStateDown(State):

    def __init__(self, bird):
        super().__init__("down")
        self.bird = bird

    def check_conditions(self):
        if self.bird.isPause:
            return "pause"

    def entry_actions(self):
        self.bird.state = 3

    def do_actions(self):
        self.bird.timeCount += self.bird.countSpeed
        self.bird.timeCount %= 60
        self.bird.speed += self.bird.acceleration
        self.bird.y += self.bird.speed

    def exit_actions(self):
        pass


class BirdStatePause(State):

    def __init__(self, bird):
        super().__init__("pause")
        self.bird = bird

    def check_conditions(self):
        if self.bird.isPause == False:
            return "up"

    def entry_actions(self):
        pass

    def do_actions(self):
        pass

    def exit_actions(self):
        pass


class BirdStateKeep(State):

    def __init__(self, bird):
        super().__init__("keep")
        self.bird = bird

    def check_conditions(self):
        pass

    def entry_actions(self):
        self.bird.state = 0

    def do_actions(self):
        self.bird.timeCount += self.bird.countSpeed
        self.bird.timeCount %= 60

    def exit_actions(self):
        pass


class BirdStateDead(State):

    def __init__(self, bird):
        super().__init__("dead")
        self.bird = bird
        self.count = 0

    def check_conditions(self):
        pass

    def entry_actions(self):
        self.bird.state = 4
        self.count = 0
        if self.bird.y > 410:
            self.bird.y = 410

    def do_actions(self):

        if self.count < 20:
            self.count += 1
        else:
            if self.bird.y < 410:
                self.bird.timeCount = self.bird.timeCount % 59 + 1
                self.bird.y += 8
            else:
                self.bird.y = 410

    def exit_actions(self):
        pass
