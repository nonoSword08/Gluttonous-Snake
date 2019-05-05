# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 20:34
# @Author  : Chensijie
# @Email   :
# @File    : snake_game.py
# @Software: PyCharm

import random
import sys

import pygame
from pygame.locals import *

# 初始化pygame
pygame.init()

# 加载界面和图片
screen = pygame.display.set_mode((640, 640), 0, 0)
pygame.display.set_caption('SnakeGame!!!')
snakehead = pygame.image.load("resource/image/snakehead.png")
snakebody = pygame.image.load("resource/image/snakebody.png")
gameover_img = pygame.image.load("resource/image/gameover.png")
food = pygame.image.load("resource/image/food.png")

# 初始化蛇头的位置
snakehead_x = [0] * 13
snakehead_y = [0] * 13
snakehead_x[0] = 320
snakehead_y[0] = 320

# 初始化蛇的头朝向
tolist = ['up', 'down', 'left', 'right']
snakeface_to = tolist[random.randint(0, 3)]

# 初始化蛇身体
snakebody_list_x = []
snakebody_list_y = []

# 初始化食物位置
food_x = random.randint(20, 620)
food_y = random.randint(20, 620)


def func(list1, val):
    """
    将值插入到列表的第一项并删除列表的最后一项
    :param list1:列表
    :param val:值
    :return: 返回新的列表
    """
    list1.insert(0, val)
    list1.pop()
    return list1


while True:

    # 获取键盘事件
    for event in pygame.event.get():
        # 退出模块
        if event.type == QUIT:
            sys.exit()

        # 根据键盘事件控制运动方向
        if event.type == KEYUP:
            if event.key == K_UP and snakeface_to != tolist[1]:
                snakeface_to = tolist[0]
            elif event.key == K_DOWN and snakeface_to != tolist[0]:
                snakeface_to = tolist[1]
            elif event.key == K_LEFT and snakeface_to != tolist[3]:
                snakeface_to = tolist[2]
            elif event.key == K_RIGHT and snakeface_to != tolist[2]:
                snakeface_to = tolist[3]

    # 判断失败条件
    flag = False
    # 撞墙
    if snakehead_x[0] < 0 or snakehead_x[0] > 640 or snakehead_y[0] < 0 or snakehead_y[0] > 640:
        flag = True
    # 撞自己
    flag1 = False
    flag2 = False
    for i in range(len(snakebody_list_x)):
        # if i == 0 or i == 1:
        #     continue
        # else:
        if -4 < (snakebody_list_x[i][12] - snakehead_x[0]) < 4 and -4 < (snakebody_list_y[i][12] - snakehead_y[0]) < 4:
                flag = True

    if flag:
        break

    # 绘制背景
    screen.fill((200, 200, 200))

    # 绘制蛇头
    screen.blit(snakehead, (snakehead_x[0], snakehead_y[0]))
    if snakeface_to == tolist[0]:
        func(snakehead_x, snakehead_x[0])
        func(snakehead_y, snakehead_y[0] - 1)
    elif snakeface_to == tolist[1]:
        func(snakehead_x, snakehead_x[0])
        func(snakehead_y, snakehead_y[0] + 1)
    elif snakeface_to == tolist[2]:
        func(snakehead_x, snakehead_x[0] - 1)
        func(snakehead_y, snakehead_y[0])
    else:
        func(snakehead_x, snakehead_x[0] + 1)
        func(snakehead_y, snakehead_y[0])

    # 绘制蛇身
    if len(snakebody_list_x) != 0:
        for i in range(len(snakebody_list_x)):
            if i == 0:
                screen.blit(snakebody, (snakehead_x[12], snakehead_y[12]))
                func(snakebody_list_x[i], snakehead_x[12])
                func(snakebody_list_y[i], snakehead_y[12])
            else:
                screen.blit(snakebody, (snakebody_list_x[i - 1][12], snakebody_list_y[i - 1][12]))
                func(snakebody_list_x[i], snakebody_list_x[i - 1][12])
                func(snakebody_list_y[i], snakebody_list_y[i - 1][12])

    # 绘制食物
    screen.blit(food, (food_x, food_y))

    # 如果蛇接近了食物则重置食物位置并让身体加1
    if -10 < snakehead_x[0] - food_x < 10 and -10 < snakehead_y[0] - food_y < 10:
        food_x = random.randint(0, 640)
        food_y = random.randint(0, 640)
        snakebody_list_x.append([0] * 13)
        snakebody_list_y.append([0] * 13)

    # 获取时间对象控制刷新画面频率
    clock = pygame.time.Clock()
    time_passed = clock.tick(100)
    pygame.display.flip()

# 失败画面
pygame.font.init()
font = pygame.font.Font(None, 24)
text = font.render("score: %d !" % len(snakebody_list_x), True, (255, 0, 0))
textRect = text.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery + 24
screen.blit(gameover_img, (0, 80))
screen.blit(text, textRect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()
