from random import random, uniform
from math import sqrt, cos, sin, pi
from py5 import Sketch


class Cell:
    pos: list[float]
    r: float
    hue: float
    wobble: bool

    def __init__(self, x: float, y: float, r_: float, w: bool):
        self.pos = [x, y]
        self.r = r_
        self.wobble = w
        self.hue = random() * 255

    def eat(self, other: "Cell") -> bool:
        if other.r >= self.r:
            return False
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        dist = (dx**2 + dy**2) ** 0.5
        if dist > other.r + self.r:
            return False

        self.r = sqrt(self.r * self.r + other.r * other.r)
        return True

    def move(self, mouse_x: int, mouse_y: int, width: int, height: int):
        dir_x = mouse_x - width / 2
        dir_y = mouse_y - height / 2
        mag = (dir_x**2 + dir_y**2) ** 0.5

        mapped_mag = max(0, min((mag / ((width + height) / 2)) * 10, 4))
        if mag > 0:
            dir_x = (dir_x / mag) * mapped_mag
            dir_y = (dir_y / mag) * mapped_mag

        self.pos[0] += dir_x
        self.pos[1] += dir_y
        self.pos[0] = max(-2 * width, min(self.pos[0], 2 * width))
        self.pos[1] = max(-2 * height, min(self.pos[1], 2 * height))

    def display(self, sketch: Sketch):
        sketch.stroke(0)
        sketch.stroke_weight(self.r / 20)
        sketch.fill(self.hue, 255, 255)

        if not self.wobble:
            sketch.ellipse(self.pos[0], self.pos[1], 2 * self.r, 2 * self.r)
        else:
            sketch.begin_shape()
            theta = 0.0
            while theta < sketch.TWO_PI:
                wr = self.r + uniform(-self.r / 16, self.r / 16)
                x = self.pos[0] + wr * cos(theta)
                y = self.pos[1] + wr * sin(theta)
                sketch.vertex(x, y)
                theta += pi / 36
            sketch.end_shape(sketch.CLOSE)
