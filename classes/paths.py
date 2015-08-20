class Path(object):
    def __init__(self,points,**kwargs):
        if self.__class__ != Path:
            self.calculate_points(points,**kwargs)
        else:
            self.points = points

    def __iter__(self):
        for p in self.points:
            yield p

    def __len__(self):
        return len(self.points)

    def __getitem__(self,index):
        return self.points[index]

class SquarePath(Path):
    def calculate_points(self,corners,loop=True):
        self.points = []
        for c in range(len(corners)-1+loop):
            point = corners[c]
            nextpoint = corners[(c+1)%len(corners)]
            if nextpoint[0] == point[0]:
                for y in range(point[1],nextpoint[1]):
                    self.points.append((point[0],y))
            elif nextpoint[1] == point[1]:
                for x in range(point[0],nextpoint[0]):
                    self.points.append((x,point[1]))
        self.points = tuple(points)

class AngularPath(Path):
    """Makes Linear paths using Bresenham's Line algorithm"""
    def calculate_points(self,corners,loop=True):
        self.points = []
        for c in range(len(corners)-1+loop):
            x1,y1 = corners[c]
            x2,y2 = corners[(c+1)%len(corners)]
            delta_x = abs(x2-x1)
            delta_y = abs(y2-y1)
            xInc = 1 if x1 < x2 else -1
            yInc = 1 if y1 < y2 else -1
            error = delta_x - delta_y
            while True:
                self.points.append((x1,y1))
                if x1 == x2 and y1 == y2:
                    break
                error2 = 2 * error
                if error2 > -delta_y:
                    error -= delta_y
                    x1 += xInc
                if error2 < delta_x:
                    error += delta_x
                    y1 += yInc

class BezierPath(Path):
    """Makes Bezier paths using de Casteljau's algorithm"""
    def calculate_points(self,controls):
        self.points = []
        i = 0
        offset = 0.01
        last_point = controls[0]
        if len(controls) == 1:
            return
        while i < 1:
            i += offset
            point = self.calculate_point(controls,i)
            dx = abs(point[0]-last_point[0])
            dy = abs(point[1]-last_point[1])
            if dx + dy == 1 or dx == dy == 1:
                self.points.append((point))
                last_point = point
            elif dx + dy == 0:
                i -= offset
                offset *= 2
            else:
                i -= offset
                offset /= 2
            if last_point == controls[-1]:
                break

    def calculate_point(self,controls,i):
        points = []
        for index in range(len(controls)-1):
            x1,y1 = controls[index]
            x2,y2 = controls[index+1]
            x = x1 + (x2 - x1) * i
            y = y1 + (y2 - y1) * i
            points.append((x,y))
        if len(points) == 1:
            return int(points[0][0]),int(points[0][1])
        else:
            return self.calculate_point(points,i)
