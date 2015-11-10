from gamesprite import GameSprite


class Damager(GameSprite):
    """Base class for something that damages others"""

    def __init__(self, game, damagepoints):
        GameSprite.__init__(self, game)
        self.damagepoints = damagepoints


class Damageable(GameSprite):
    """Base class for damageable entities"""

    def __init__(self, game, health):
        GameSprite.__init__(self, game)
        self.health = health
        self.hurt = False
        self.dead = False  # Used if you want to do something when it dies

    def update(self):
        self.update_health()

    def update_health(self):
        self.hurt = False
        for p in self.game.damagers:
            if p.rect.cilliderect(self.rect):
                self.hurt = True
                self.health -= p.damagepoints
                if self.health <= 0:
                    self.dead = True


class Launcher(GameSprite):
    def __init__(self, game, pos, projectile, *pargs, **pkwargs):
        GameSprite.__init__(self, game)
        self.pos = pos
        self.projectile = projectile
        self.pargs = pargs
        self.pkwargs = pkwargs

    def update(self):
        self.update_launch()

    def update_launch(self):
        args = self.pargs.copy()
        p = self.projectile(self.game, *args, **self.kwargs)
        p.pos = self.pos
