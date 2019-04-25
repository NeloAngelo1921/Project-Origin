# -*- coding: UTF-8 -*-
# 我的第一个python游戏

import pygame
from pygame.locals import *
from sys import exit

# 定义窗口的分辨率
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

# 计数
ticks = 0

# 初始化游戏
pygame.init()   # 初始化pygame
# 初始化一个用来显示的窗口
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# 设置窗口标题
pygame.display.set_caption("打飞机")
#载入背景图片
background = pygame.image.load('E:/wx/python/test/game/images/xkbg2.png')

# 载入资源图片
shoot_img = pygame.image.load('E:/wx/python/test/game/images/fj.png')
# 用subsurface剪切读入的图片
hero1_rect = pygame.Rect(0, 0, 0, 126)
hero2_rect = pygame.Rect(0, 0, 0, 126)
hero1 = shoot_img.subsurface(hero1_rect)
hero2 = shoot_img.subsurface(hero2_rect)
hero_pos = [200, 500]
# 事件循环
while True:

    # 绘制背景
    screen.blit(background,(0,0))
    # 更新屏幕
    pygame.display.update()

    # 绘制飞机
    if ticks % 50 < 25:
        screen.blit(hero1, hero_pos)
    else:
        screen.blit(hero2, hero_pos)
        ticks += 1

    # 处理游戏退出
    # 从消息队列中循环获取
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()