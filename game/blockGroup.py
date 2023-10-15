import pygame, sys
import random
from pygame.locals import *
from block import *
from const import *


class BlockGroup(object):
    def GenerateBlockGroupConfig(rowIdx, colIdx):
        idx = random.randint(0, len(BLOCK_SHAPE) - 1)
        bType = random.randint(0, BlockType.BLOCKMAX - 1)
        confingList = []
        for x in range(len(BLOCK_SHAPE[idx])):
            config = {
                "BlockType": bType,
                "rowIdx": rowIdx + BLOCK_SHAPE[idx][x][0],
                "colIdx": colIdx + BLOCK_SHAPE[idx][x][1],
            }
            confingList.append(config)
        return confingList

    def __init__(self, blockGroupType ,width, height, blockConfingList, relPos):
        super().__init__()
        self.blocks = []
        self.time = 0
        self.blockGroupType = blockGroupType
        for config in blockConfingList:
            blk = Block(
                config["BlockType"],
                config["rowIdx"],
                config["colIdx"],
                width,
                height,
                relPos,
            )
            self.blocks.append(blk)

    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)

    def update(self):
        self.time += 1
        if self.blockGroupType == BlockGruopType.DROP:
            if self.time >=1000:
                self.time = 0
                for b in self.blocks:
                    b.drop()
