
from pygame import Rect

class Vector:
    """
    instance of 2D vector
    i - horizontal
    j - vertical
    """
    def __init__(self, _i, _j):
        self.i = _i
        self.j = _j

    def add_components(self, other):
        self.i += other.i
        self.j += other.j

    def fmt(self):
        return [self.i, self.j]


class Movable:

    def __init__(self, pos: Vector, size: Vector,
                 vel: Vector = None,
                 acc: Vector = None):
        self.pos = pos
        self.size = size
        self.pygame_rect = Rect(*self.pos.fmt(), *self.size.fmt())
        self.vel = vel or Vector(0, 0)
        self.acc = acc or Vector(0, 0)


    def update(self):
        self.pos.add_components(self.vel)
        self.vel.add_components(self.acc)
        self.pygame_rect = Rect(*self.pos.fmt(), *self.size.fmt())

    def draw(self):
        pass

    def fmt(self):
        return [*self.pos.fmt(), *self.size.fmt()]


WINDOW_W = 400
WINDOW_H = 400
