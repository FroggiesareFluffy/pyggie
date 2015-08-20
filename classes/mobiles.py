import pygame

from gamesprite import GameSprite

LOOP,FLIP,STOP = "LFS"

class PathFollower(GameSprite):
    """ Mobile class that follows a path"""
    def __init__(self,game,path,speed,image,startpos=0,loop=LOOP):
        GameSprite.__init__(self,game)
        self.path = path
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.ppos = startpos
        self.loop = loop

    def update(self):
        self.update_path()

    def update_path(self):
        if self.ppos >= len(self.path):
            if self.loop == LOOP:
                self.ppos %= len(self.path)
            elif self.loop == FLIP:
                self.ppos = len(self.path) - (self.ppos - len(self.path)) - 1
            else:
                self.ppos = len(self.path)
        self.pos = self.path[self.ppos]
        self.rect.center = self.pos
        self.ppos += self.speed
        
class PathFinder(PathFollower):
    """Mobile class that finds a path to its target"""
    def __init__(self,game,speed,pos,image,target):
        Seeker.__init__(self,game,speed,speed,pos,image,target)
        PathFollower.__init__(self,game,Path(),speed,image)
    def update(self):
        if not hasattr(self,"path") or self.game.was_updated:
            self.create_path()
            self.ppos = 0
        self.update_path()
            
    def create_path(self):
        import Queue
        frontier = Queue.PriorityQueue()
        frontier.put((0,self.pos))
        came_from = {}
        cost_so_far = {}
        came_from[self.pos] = None
        cost_so_far[self.pos] = 0
        if isinstance(self.target,GameSprite):
            endpos = self.target.pos
        else:
            endpos = self.target
        while not frontier.empty():
            current = frontier.get()[0]
            if current == endpos:
                break
            x,y = current
            for nextpos in ((x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),
                            (x-1,y+1),(x,y+1),(x+1,y+1)):
                newcost = cost_so_far[current] + 1
                if nextpos not in cost_so_far or newcost < cost_so_far[nextpos]:
                    cost_so_far[nextpos] = nescost
                    priority = new_cost + self.heuristic(self,x,y)
                    frontier.put((priority,nextpos))
                    came_from[nextpos] = current
        path = []
        while current != self.pos:
            path.insert(0,current)
            current = came_from(current)
        path.insert(0,self.pos)
        self.path = Path(path)

    def heuristic(self,x,y):
        if isinstance(self.target,GameSprite):
            x2,y2 = self.target.pos
        else:
            x2,y2 = self.target
        dx = abs(x - x2)
        dy = abs(y - y2)
        return max(dx,dy)

class Directed(GameSprite):
    """ Base class for objects that move in a direction"""
    def __init__(self,game,pos,image,xspeed,yspeed):
        GameSprite.__init__(self,game)
        self.pos = list(pos)
        self.image = image
        self.rect = self.image.get_rect()
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.pos[0] += self.xspeed
        self.pos[1] += self.yspeed
        self.rect.center = self.pos

class Controlled(Directed):
    """Base class for player or computer controlled mobiles"""
    def __init__(self,game,pos,image,speed):
        Directional.__init__(self,game,pos,image,0,0)
        self.speed = speed

    def start_left(self):
        self.xspeed -= self.speed
    def start_right(self):
        self.xspeed += self.speed
    def start_up(self):
        self.yspeed -= self.speed
    def start_down(self):
        self.yspeed += self.speed

    def stop_left(self):
        self.xspeed += self.speed
    def stop_right(self):
        self.xspeed -= self.speed
    def stop_up(self):
        self.yspeed += self.speed
    def stop_down(self):
        self.yspeed -= self.speed

