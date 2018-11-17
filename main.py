# -*- coding:utf-8 -*-
"""
@author:SiriYang
@file:main.py
@time:2018/11/15 15:26
"""

import pygame

from SiriGame import GameObject
from MenuScene import MenuScene

if __name__ == "__main__":
    gameObj = GameObject(384, 512)
    gameObj.setCaption("Flappy Bird (PyGame)")
    gameObj.setIcon(gameObj.source.img_icon)

    menuScene = MenuScene(gameObj)
    menuScene.run()

    gameObj.quit()
