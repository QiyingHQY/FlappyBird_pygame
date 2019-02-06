# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:GameSource.py
@time:2018/11/15 21:24
"""

import pygame


class GameSource():

    def __init__(self):
        """background"""
        self.img_ground = pygame.image.load("./source/image/background/ground.png").convert_alpha()
        self.img_day = pygame.image.load("./source/image/background/day.png").convert_alpha()
        self.img_night = pygame.image.load("./source/image/background/night.png").convert_alpha()
        self.img_guide_day = pygame.image.load("./source/image/background/guide_day.png").convert_alpha()
        self.img_guide_night = pygame.image.load("./source/image/background/guide_night.png").convert_alpha()

        """button"""
        self.img_button_start = pygame.image.load("./source/image/button/start.png").convert_alpha()
        self.img_button_start_on = pygame.image.load("./source/image/button/start_on.png").convert_alpha()
        self.img_button_start_pressed = pygame.image.load("./source/image/button/start_pressed.png").convert_alpha()

        self.img_button_rank = pygame.image.load("./source/image/button/rank.png").convert_alpha()
        self.img_button_rank_on = pygame.image.load("./source/image/button/rank_on.png").convert_alpha()
        self.img_button_rank_pressed = pygame.image.load("./source/image/button/rank_pressed.png").convert_alpha()

        """bird"""
        """--blue"""
        """----up"""
        self.img_bird_blue_up_up = pygame.image.load("./source/image/bird/blue/20_up.png").convert_alpha()
        self.img_bird_blue_up_mid = pygame.image.load("./source/image/bird/blue/20_mid.png").convert_alpha()
        self.img_bird_blue_up_down = pygame.image.load("./source/image/bird/blue/20_down.png").convert_alpha()

        """----mid"""
        self.img_bird_blue_mid_up = pygame.image.load("./source/image/bird/blue/0_up.png").convert_alpha()
        self.img_bird_blue_mid_mid = pygame.image.load("./source/image/bird/blue/0_mid.png").convert_alpha()
        self.img_bird_blue_mid_down = pygame.image.load("./source/image/bird/blue/0_down.png").convert_alpha()

        """----down"""
        self.img_bird_blue_down_up = pygame.image.load("./source/image/bird/blue/-20_up.png").convert_alpha()
        self.img_bird_blue_down_mid = pygame.image.load("./source/image/bird/blue/-20_mid.png").convert_alpha()
        self.img_bird_blue_down_down = pygame.image.load("./source/image/bird/blue/-20_down.png").convert_alpha()

        """----dead"""
        self.img_bird_blue_dead_up = pygame.image.load("./source/image/bird/blue/-90_up.png").convert_alpha()
        self.img_bird_blue_dead_mid = pygame.image.load("./source/image/bird/blue/-90_mid.png").convert_alpha()
        self.img_bird_blue_dead_down = pygame.image.load("./source/image/bird/blue/-90_down.png").convert_alpha()

        """--green"""
        """----up"""
        self.img_bird_green_up_up = pygame.image.load("./source/image/bird/green/20_up.png").convert_alpha()
        self.img_bird_green_up_mid = pygame.image.load("./source/image/bird/green/20_mid.png").convert_alpha()
        self.img_bird_green_up_down = pygame.image.load("./source/image/bird/green/20_down.png").convert_alpha()

        """----mid"""
        self.img_bird_green_mid_up = pygame.image.load("./source/image/bird/green/0_up.png").convert_alpha()
        self.img_bird_green_mid_mid = pygame.image.load("./source/image/bird/green/0_mid.png").convert_alpha()
        self.img_bird_green_mid_down = pygame.image.load("./source/image/bird/green/0_down.png").convert_alpha()

        """----down"""
        self.img_bird_green_down_up = pygame.image.load("./source/image/bird/green/-20_up.png").convert_alpha()
        self.img_bird_green_down_mid = pygame.image.load("./source/image/bird/green/-20_mid.png").convert_alpha()
        self.img_bird_green_down_down = pygame.image.load("./source/image/bird/green/-20_down.png").convert_alpha()

        """----dead"""
        self.img_bird_green_dead_up = pygame.image.load("./source/image/bird/green/-90_up.png").convert_alpha()
        self.img_bird_green_dead_mid = pygame.image.load("./source/image/bird/green/-90_mid.png").convert_alpha()
        self.img_bird_green_dead_down = pygame.image.load("./source/image/bird/green/-90_down.png").convert_alpha()

        """--red"""
        """----up"""
        self.img_bird_red_up_up = pygame.image.load("./source/image/bird/red/20_up.png").convert_alpha()
        self.img_bird_red_up_mid = pygame.image.load("./source/image/bird/red/20_mid.png").convert_alpha()
        self.img_bird_red_up_down = pygame.image.load("./source/image/bird/red/20_down.png").convert_alpha()

        """----mid"""
        self.img_bird_red_mid_up = pygame.image.load("./source/image/bird/red/0_up.png").convert_alpha()
        self.img_bird_red_mid_mid = pygame.image.load("./source/image/bird/red/0_mid.png").convert_alpha()
        self.img_bird_red_mid_down = pygame.image.load("./source/image/bird/red/0_down.png").convert_alpha()

        """----down"""
        self.img_bird_red_down_up = pygame.image.load("./source/image/bird/red/-20_up.png").convert_alpha()
        self.img_bird_red_down_mid = pygame.image.load("./source/image/bird/red/-20_mid.png").convert_alpha()
        self.img_bird_red_down_down = pygame.image.load("./source/image/bird/red/-20_down.png").convert_alpha()

        """----dead"""
        self.img_bird_red_dead_up = pygame.image.load("./source/image/bird/red/-90_up.png").convert_alpha()
        self.img_bird_red_dead_mid = pygame.image.load("./source/image/bird/red/-90_mid.png").convert_alpha()
        self.img_bird_red_dead_down = pygame.image.load("./source/image/bird/red/-90_down.png").convert_alpha()

        """--yellow"""
        """----up"""
        self.img_bird_yellow_up_up = pygame.image.load("./source/image/bird/yellow/20_up.png").convert_alpha()
        self.img_bird_yellow_up_mid = pygame.image.load("./source/image/bird/yellow/20_mid.png").convert_alpha()
        self.img_bird_yellow_up_down = pygame.image.load("./source/image/bird/yellow/20_down.png").convert_alpha()

        """----mid"""
        self.img_bird_yellow_mid_up = pygame.image.load("./source/image/bird/yellow/0_up.png").convert_alpha()
        self.img_bird_yellow_mid_mid = pygame.image.load("./source/image/bird/yellow/0_mid.png").convert_alpha()
        self.img_bird_yellow_mid_down = pygame.image.load("./source/image/bird/yellow/0_down.png").convert_alpha()

        """----down"""
        self.img_bird_yellow_down_up = pygame.image.load("./source/image/bird/yellow/-20_up.png").convert_alpha()
        self.img_bird_yellow_down_mid = pygame.image.load("./source/image/bird/yellow/-20_mid.png").convert_alpha()
        self.img_bird_yellow_down_down = pygame.image.load("./source/image/bird/yellow/-20_down.png").convert_alpha()

        """----dead"""
        self.img_bird_yellow_dead_up = pygame.image.load("./source/image/bird/yellow/-90_up.png").convert_alpha()
        self.img_bird_yellow_dead_mid = pygame.image.load("./source/image/bird/yellow/-90_mid.png").convert_alpha()
        self.img_bird_yellow_dead_down = pygame.image.load("./source/image/bird/yellow/-90_down.png").convert_alpha()

        """medals"""
        self.img_medals_copper = pygame.image.load("./source/image/medals/copper.png").convert_alpha()
        self.img_medals_sliver = pygame.image.load("./source/image/medals/sliver.png").convert_alpha()
        self.img_medals_gold = pygame.image.load("./source/image/medals/gold.png").convert_alpha()
        self.img_medals_platinum = pygame.image.load("./source/image/medals/platinum.png").convert_alpha()

        """number"""
        """--L"""
        self.img_number_L_0 = pygame.image.load("./source/image/number/L/0.png").convert_alpha()
        self.img_number_L_1 = pygame.image.load("./source/image/number/L/1.png").convert_alpha()
        self.img_number_L_2 = pygame.image.load("./source/image/number/L/2.png").convert_alpha()
        self.img_number_L_3 = pygame.image.load("./source/image/number/L/3.png").convert_alpha()
        self.img_number_L_4 = pygame.image.load("./source/image/number/L/4.png").convert_alpha()
        self.img_number_L_5 = pygame.image.load("./source/image/number/L/5.png").convert_alpha()
        self.img_number_L_6 = pygame.image.load("./source/image/number/L/6.png").convert_alpha()
        self.img_number_L_7 = pygame.image.load("./source/image/number/L/7.png").convert_alpha()
        self.img_number_L_8 = pygame.image.load("./source/image/number/L/8.png").convert_alpha()
        self.img_number_L_9 = pygame.image.load("./source/image/number/L/9.png").convert_alpha()

        """--S"""
        self.img_number_S_0 = pygame.image.load("./source/image/number/S/0.png").convert_alpha()
        self.img_number_S_1 = pygame.image.load("./source/image/number/S/1.png").convert_alpha()
        self.img_number_S_2 = pygame.image.load("./source/image/number/S/2.png").convert_alpha()
        self.img_number_S_3 = pygame.image.load("./source/image/number/S/3.png").convert_alpha()
        self.img_number_S_4 = pygame.image.load("./source/image/number/S/4.png").convert_alpha()
        self.img_number_S_5 = pygame.image.load("./source/image/number/S/5.png").convert_alpha()
        self.img_number_S_6 = pygame.image.load("./source/image/number/S/6.png").convert_alpha()
        self.img_number_S_7 = pygame.image.load("./source/image/number/S/7.png").convert_alpha()
        self.img_number_S_8 = pygame.image.load("./source/image/number/S/8.png").convert_alpha()
        self.img_number_S_9 = pygame.image.load("./source/image/number/S/9.png").convert_alpha()

        """obstacle"""
        self.img_obstacle_up = pygame.image.load("./source/image/obstacle/up.png").convert_alpha()
        self.img_obstacle_down = pygame.image.load("./source/image/obstacle/down.png").convert_alpha()

        """other"""
        self.img_logo = pygame.image.load("./source/image/other/logo.png").convert_alpha()
        self.img_icon = pygame.image.load("./source/image/other/icon.png").convert_alpha()
        self.img_gameover = pygame.image.load("./source/image/other/gameOver.png").convert_alpha()
        self.img_scorecard = pygame.image.load("./source/image/other/scorecard.png").convert_alpha()
