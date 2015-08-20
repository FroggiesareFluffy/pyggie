import pygame

import mobiles
from gamesprite import GameSprite

class Static(GameSprite):
    """Object that doesn't move"""
    def __init__(self,game,pos,image):
        GameSprite.__init__(self,game)
        self.pos = pos
        self.image = image
        self.rect = self.image.get_rect()

class Block(Static):
    def update(self):
        self.update_block()
    def update_block(self):
        for s in self.game:
            if s is self:
                continue
            if s.rect.colliderect(self.rect):
                if isinstance(s,mobiles.PathFollower):
                    s.ppos -= 1
                elif isinstance(s,mobiles.Controlled):
                    if s.xspeed > 0:
                        xchange = float(s.rect.right - self.rect.left)/s.xspeed
                    else:
                        xchange = float(self.rect.right - s.rect.left)/s.xspeed
                    if s.yspeed > 0:
                        ychange = float(s.rect.bottom - self.rect.top)/s.yspeed
                    else:
                        ychange = float(self.rect.bottom - s.rect.top)/s.yspeed
                    if xchange > ychange:
                        if s.xspeed > 0:
                            s.rect.right = self.rect.left
                        else:
                            s.rect.left = self.rect.right
                    else:
                        if s.yspeed > 0:
                            s.rect.bottom = self.rect.top
                        else:
                            s.rect.top = self.rect.bottom
        
