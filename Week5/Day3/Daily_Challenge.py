import math
class Circle:
    ''''''
    def __init__(self, r=None, d=None):
        if r:
            self.r = r
        elif d:
            self.r = d/2
        else:
            raise Exception('this class needs r or d to initialize')
    @property
    def diameter(self):
        return self.r*2
    @property
    def area(self):
        return math.pi * self.r**2
    def __repr__(self):
        return f'circle object: radius of {self.r}'
    def __add__(self, other):
        if isinstance(other,Circle):
            return Circle(r=self.r+other.r)
        else:
            raise Exception('only add 2 circles')
    def __gt__(self, other):
        if isinstance(other,Circle):
            return self.r > other.r
        else:
            raise Exception('only compare 2 circles')
    def __lt__(self, other):
        if isinstance(other,Circle):
            return self.r < other.r
        else:
            raise Exception('only compare 2 circles')
    def __eq__(self, other):
        if isinstance(other,Circle):
            return self.r == other.r
        else:
            raise Exception('only compare 2 circles')
c = Circle(r=3)
c2 = Circle(r=5)