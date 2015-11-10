import pygame


class Game(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.mobiles = []
        self.damagers = []
        self.statics = []
        self.was_updated = True

    def add_internal(self, s):
        if isinstance(s, Damager):
            self.damagers.append(s)
        if isinstance(s, Static):
            self.statics.append(s)
        elif isinstance(s, (Controlled, PathFollower)):
            self.mobiles.append(s)
        Game.add_internal(self, s)
        self.was_updated = True

    def remove_internal(self, s):
        if isinstance(s, Damager):
            self.damagers.remove(s)
        elif isinstance(s, Static):
            self.statics.remove(s)
        elif isinstance(s, (Controlled, PathFollower)):
            self.mobiles.remove(s)
        Game.remove_internal(self, s)
        self.was_updated = True

    def update(self):
        for s in self.sprites():
            s.update()
        self.was_updated = False


from pyggie.gameobjs.mobiles import PathFollower, Controlled
from pyggie.gameobjs.statics import Static
from pyggie.gameobjs.bases import Damager
