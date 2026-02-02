from random import uniform
from math import sqrt


class RainDrop:
    ACC: float = 0.1
    HUE: float = 270.0

    x: float
    y: float
    volume: float
    len: float
    thickness: float
    brightness: float
    vel: float

    def __init__(self, width: int, height: int):
        self.x = uniform(-width / 2, width / 2)
        self.y = uniform(-height / 2 - 100, -height / 2)

        self.vel = uniform(1, 10)

        self.volume = uniform(3, 15)
        self.brightness = uniform(30, 65)
        self.len = 0
        self.thickness = 0

    def update(self):
        self.y += self.vel
        self.vel += self.ACC

        self.len = self.remap(self.vel, 0, 15, sqrt(self.volume), self.volume)
        self.thickness = self.volume / self.len

    def remap(
        self, value: float, start1: float, stop1: float, start2: float, stop2: float
    ) -> float:
        return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

    def display(self, sketch):
        sketch.stroke_weight(self.thickness)
        sketch.stroke(self.HUE, 100, self.brightness)
        sketch.line(self.x, self.y, self.x, self.y - self.len)
