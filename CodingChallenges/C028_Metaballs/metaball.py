from random import random, uniform


class Metaball:
    pos: list[float]
    vel: list[float]
    radius: float
    _width: int
    _height: int

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self.pos = [random() * width, random() * height]
        mag = uniform(4, 8)
        self.vel = [mag * random(), mag * random()]
        self.radius = uniform(20, 70)

    def func(self, x: int, y: int) -> float:
        dx = self.pos[0] - x
        dy = self.pos[1] - y
        dis = (dx * dx + dy * dy) ** 0.5
        return self.radius / dis if dis > 0 else self.radius

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.pos[0] <= 0 or self.pos[0] >= self._width:
            self.vel[0] *= -1
        if self.pos[1] <= 0 or self.pos[1] >= self._height:
            self.vel[1] *= -1
