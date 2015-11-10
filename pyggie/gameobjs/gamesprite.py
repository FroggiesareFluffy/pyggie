import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self,game)

    def __setattr__(self, name, value):
        if name in ("pos","rect"):
            self.game.was_updated = True
        pygame.sprite.Sprite.__setattr__(self, name, value)

