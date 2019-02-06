# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:PlayScene.py
@time:2018/11/16 19:45
"""
import time
from random import randint

from pygame.locals import *

from Bird import Bird
from Obstacle import Obstacle
from SiriGame import GameScene
from SiriGame.GUI import Button

from DB import DB


class PlayScene(GameScene):

    def __init__(self, gameobj):

        super().__init__(gameobj)

        self.bird = Bird(self)

        self.obstacleList = [Obstacle(self, 700), Obstacle(self, 940), Obstacle(self, 1180)]

        self.btn_start = Button(self, 35, 350, 140, 78)
        self.btn_start.setImg(self.source.img_button_start, self.source.img_button_start_on,
                              self.source.img_button_start_pressed)

        self.btn_rank = Button(self, 210, 350, 140, 78)
        self.btn_rank.setImg(self.source.img_button_rank, self.source.img_button_rank_on,
                             self.source.img_button_rank_pressed)

        self.img_num = [[self.source.img_number_S_0, self.source.img_number_S_1, self.source.img_number_S_2,
                         self.source.img_number_S_3,
                         self.source.img_number_S_4, self.source.img_number_S_5, self.source.img_number_S_6,
                         self.source.img_number_S_7,
                         self.source.img_number_S_8, self.source.img_number_S_9, ],
                        [self.source.img_number_L_0, self.source.img_number_L_1, self.source.img_number_L_2,
                         self.source.img_number_L_3,
                         self.source.img_number_L_4, self.source.img_number_L_5, self.source.img_number_L_6,
                         self.source.img_number_L_7,
                         self.source.img_number_L_8, self.source.img_number_L_9, ]]

        """
        Game state
            0:resady
            1:playing
            2:dead
        """
        self.state = 0

        self.score = 0
        self.maxscore = 0

        self.deadCount = 0

        self.isPause = False
        self.isDay = True
        self.groundPos = 384

    def init(self, args=None):
        self.groundPos = 384
        self.isEnd = False
        self.isQuit = False

        self.init_game(args)

    def init_game(self, args=None):
        self.readScore()
        print(self.get_time())
        self.state = 0
        self.score = 0
        self.maxscore = 0

        self.btn_start.y = 350
        self.btn_rank.y = 350

        self.bird.init()

        for i in range(len(self.obstacleList)):
            self.obstacleList[i].x = 700 + i * 240
            self.obstacleList[i].init()

        if args != None:
            self.isDay = args
        else:
            self.init_dayOrNight()

    def init_dayOrNight(self):
        if randint(0, 20) % 2 == 0:
            self.isDay = not self.isDay

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
                    i.stateMachine.set_state('move')
                self.bird.stateMachine.set_state('up')

            if self.state == 1:
                if self.isPause:
                    self.isPause = False

            if self.state == 2:
                if self.btn_start.isOn():
                    print(1)
                    self.init_game()

        elif event.button == 3:
            self.event_pause()

    def event_pause(self):
        if self.state == 1:
            self.isPause = not self.isPause

    def update(self):
        super().update()

        if self.state == 1:
            if not self.isPause:
                self.update_score()

                if self.isDead():
                    self.bird.stateMachine.set_state("dead")
                    for i in self.obstacleList:
                        i.stateMachine.set_state("stop")
                    self.state = 2
                    self.deadCount = 0
                    self.maxscore=self.getMaxScore()
                    if self.score>0:
                        self.saveScore()
        elif self.state == 2:
            self.update_dead()

        self.update_ground()

    def update_score(self):
        for i in self.obstacleList:
            if i.x == 30:
                self.score += 1

    def update_dead(self):
        if self.bird.y == 410:
            if self.deadCount < 500:
                self.deadCount += 5

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

        if self.state == 1:
            self.render_score(192, 50, self.score, 1, True)

        self.screen.blit(self.source.img_ground, (self.groundPos - 384, 448))
        self.screen.blit(self.source.img_ground, (self.groundPos, 448))

        if self.state == 2:
            self.render_dead()

    def render_guide(self):

        if self.isDay:
            self.screen.blit(self.source.img_guide_day, (0, 0))
        else:
            self.screen.blit(self.source.img_guide_night, (0, 0))

    def render_score(self, x, y, value, size=0, center=False):
        if size == 0:
            w = 21
        else:
            w = 38

        string = str(value)
        length = len(string)

        if center:
            x -= int((length * w) / 2)

        for i in range(length):
            self.screen.blit(self.img_num[size][int(string[i])], (x + i * w, y))

    def render_background(self):

        if self.isDay:
            self.screen.blit(self.source.img_day, (0, 0))
        else:
            self.screen.blit(self.source.img_night, (0, 0))

    def render_dead(self):
        if self.deadCount > 0:
            if self.deadCount < 500:
                self.screen.blit(self.source.img_gameover, (64, 70 - 500 + self.deadCount))
                self.screen.blit(self.source.img_scorecard, (42, 170 - 500 + self.deadCount))
                self.render_score(285, 215 - 500 + self.deadCount, self.score, 0, True)
                self.render_score(285, 270 - 500 + self.deadCount, self.maxscore, 0, True)
                if self.score > 200:
                    self.screen.blit(self.source.img_medals_platinum, (80, 230 - 500 + self.deadCount))
                elif self.score > 150:
                    self.screen.blit(self.source.img_medals_gold, (80, 230 - 500 + self.deadCount))
                elif self.score > 80:
                    self.screen.blit(self.source.img_medals_sliver, (80, 230 - 500 + self.deadCount))
                elif self.score > 20:
                    self.screen.blit(self.source.img_medals_copper, (80, 230 - 500 + self.deadCount))
                self.btn_start.y = 850 - self.deadCount
                self.btn_rank.y = 850 - self.deadCount
            else:
                self.screen.blit(self.source.img_gameover, (64, 70))
                self.screen.blit(self.source.img_scorecard, (42, 170))
                self.render_score(285, 215, self.score, 0, True)
                self.render_score(285, 270, self.maxscore, 0, True)
                if self.score > 200:
                    self.screen.blit(self.source.img_medals_platinum, (80, 230))
                elif self.score > 150:
                    self.screen.blit(self.source.img_medals_gold, (80, 230))
                elif self.score > 80:
                    self.screen.blit(self.source.img_medals_sliver, (80, 230))
                elif self.score > 20:
                    self.screen.blit(self.source.img_medals_copper, (80, 230))

            self.btn_start.render()
            self.btn_rank.render()

    def isDead(self):
        if self.bird.y >= 410:
            return True
        for i in self.obstacleList:
            if i.isIn(self.bird.x, self.bird.y, self.bird.w, self.bird.h):
                return True

    def quite(self):
        super().quite()

        self.returnArg.append(self.isDay)

    def readScore(self):
        db = DB()
        return db.selectRecord()

    def getMaxScore(self):

        record=self.readScore()

        if len(record)==0:
            return 0
        else:
            return record[0][1]

    def saveScore(self):
        db = DB()
        db.insertRecord(self.score)


    def get_time(self):
        nowTime = time.localtime(time.time())
        timeStr = "{year}.{month}.{day} {hour}:{min}:{sec}".format(year=nowTime.tm_year, month=nowTime.tm_mon,
                                                                   day=nowTime.tm_mday, hour=nowTime.tm_hour,
                                                                   min=nowTime.tm_min, sec=nowTime.tm_sec)
        return timeStr
