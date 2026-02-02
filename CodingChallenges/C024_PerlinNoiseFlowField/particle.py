from random import random, uniform
from py5 import Sketch


class Particle:
    pos: list[float]
    dir: list[float]
    prev: list[float]
    speed: float
    dec: float

    def __init__(self, width: int, height: int):
        self.pos = [random() * width, random() * height]
        self.dir = [0.0, 0.0]
        self.speed = uniform(5, 7)
        self.dec = uniform(0.001, 0.02)
        self.prev = self.pos[:]
        self._width = width
        self._height = height

    def update(self):
        if self.speed <= 0:
            return

        self.prev = self.pos[:]
        self.pos[0] += self.dir[0] * self.speed
        self.pos[1] += self.dir[1] * self.speed
        self.speed -= self.dec
        self.check_edges()

    def add_dir(self, f: list[float], imp: float):
        self.dir[0] += f[0] * imp
        self.dir[1] += f[1] * imp
        mag = (self.dir[0] ** 2 + self.dir[1] ** 2) ** 0.5
        if mag > 0:
            self.dir[0] /= mag
            self.dir[1] /= mag

    def check_edges(self):
        if self.pos[0] <= 0:
            self.pos[0] = self._width
        if self.pos[0] >= self._width:
            self.pos[0] = 0
        if self.pos[1] <= 0:
            self.pos[1] = self._height
        if self.pos[1] >= self._height:
            self.pos[1] = 0

        if (
            self.pos[0] <= 0
            or self.pos[0] >= self._width
            or self.pos[1] <= 0
            or self.pos[1] >= self._height
        ):
            self.prev = self.pos[:]

    def display(self, sketch: Sketch):
        sketch.stroke(0, 10)
        sketch.line(self.pos[0], self.pos[1], self.prev[0], self.prev[1])
