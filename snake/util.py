from pygame import Rect

CELL_W = 20
CELL_H = 20
WINDOW_W = CELL_W * 20
WINDOW_H = CELL_H * 20


class Vector:
    """
    instance of 2D vector
    i - horizontal
    j - vertical
    """

    def __init__(self, _i, _j):
        self.i = _i
        self.j = _j

    def __eq__(self, other) -> bool:
        return (
                self.i == other.i
                and
                self.j == other.j
        )

    def __repr__(self):
        return f'{{ {self.i}, {self.j} }}'

    def add_components(self, other):
        self.i += other.i
        self.j += other.j

    def add_components_new(self, other):
        return Vector(
            self.i + other.i,
            self.j + other.j,
        )

    def sub_components_new(self, other):
        return Vector(
            self.i - other.i,
            self.j - other.j,
        )

    def fmt(self, scalar=1):
        return [self.i * scalar, self.j * scalar]


class Movable:

    def __init__(self, pos: Vector, size: Vector,
                 vel: Vector = None,
                 acc: Vector = None):
        self.pos = pos
        self.size = size
        print('moveable init')
        print(self.pos, self.size)
        self.pygame_rect = Rect(*self.pos.fmt(), *self.size.fmt())
        self.vel = vel or Vector(0, 0)
        self.acc = acc or Vector(0, 0)

    def __repr__(self):
        return f'{{ pos:{self.pos} size:{self.size} vel:{self.vel} }}'

    def update(self):
        self.pos.add_components(self.vel)
        self.vel.add_components(self.acc)
        self.pygame_rect = Rect(*self.pos.fmt(), *self.size.fmt())

    def draw(self):
        pass

    def fmt(self):
        return [*self.pos.fmt(), *self.size.fmt()]
