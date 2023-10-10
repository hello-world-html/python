import random
import pygame, sys
from pygame.locals import *
from block import *
from const import *

class BlockblockGroup(object):
    def GenerateBlockGroupConfig(rowIdx, colIdx):
        idx = random.randint(0, len(BLOCK_SHAPE)-1)
        bType = random.randint(0, BlockType.BLOCKMAX-1)
        confingList = []
        for x in range(len (BLOCK_SHAPE [idx] ) ):
            config = {
                'BlockType' : bType,
                'rowIdx' : rowIdx + BLOCK_SHAPE[idx][x][0],
                'colIdx' : colIdx + BLOCK_SHAPE[idx][x][1]
                }
            confingList.append(config)
        return confingList
    def __init__(self, width, height, blockConfingList, relPos):
        super().__init__()
        self.blocks = []
        for config in blockConfingList:
            blk = Block(config['BlockType'], config['rowIdx'], config['colIdx'], width, height, relPos)
            self.blocks.append(blk)
    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)