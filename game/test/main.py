import pygame
import sys
from pygame.locals import *
from block import *
from const import *

# 初始化pygame
pygame.init()

# 定义屏幕宽度和高度
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 创建显示窗口
DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 创建紫色和青色方块对象
P = Block(BlockType.PURPLE, (200, 300))
C = Block(BlockType.CYAN, (600, 300))

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 处理退出事件
            pygame.quit()
            sys.exit()

    # 更新紫色和青色方块
    P.update()
    C.update()

    # 填充屏幕为黑色
    DISPLAY.fill((0, 0, 0))

    # 绘制紫色和青色方块
    P.draw(DISPLAY)
    C.draw(DISPLAY)

    # 更新显示
    pygame.display.update()
import pygame
import sys
from pygame.locals import *
from block import *
from const import *

# 初始化pygame
pygame.init()

# 定义屏幕宽度和高度
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 创建显示窗口
DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 创建紫色和青色方块对象
P = Block(BlockType.PURPLE, (200, 300))
C = Block(BlockType.CYAN, (600, 300))

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 处理退出事件
            pygame.quit()
            sys.exit()

    # 更新紫色和青色方块
    P.update()
    C.update()

    # 填充屏幕为黑色
    DISPLAY.fill((0, 0, 0))

    # 绘制紫色和青色方块
    P.draw(DISPLAY)
    C.draw(DISPLAY)

    # 更新显示
    pygame.display.update()
