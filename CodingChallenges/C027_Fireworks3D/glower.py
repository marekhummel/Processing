from math import acos, pi, sqrt
from py5 import Sketch


class Glower:
    pos: list[list[float]]
    vel: list[float]
    hue: int
    gone: bool = False

    def __init__(self, p: list[float], v: list[float], h: int):
        self.pos = []
        for i in range(3):
            self.pos.append(p[:])
        self.vel = v[:]
        self.hue = h
        self.gone = False

    def update(self):
        for i in range(len(self.pos) - 1, 0, -1):
            self.pos[i] = self.pos[i - 1][:]

        self.vel[1] += 0.05
        self.pos[0][0] += self.vel[0]
        self.pos[0][1] += self.vel[1]
        self.pos[0][2] += self.vel[2]

        # angle between vel and (0, 1, 0)
        mag1 = sqrt(self.vel[0] ** 2 + self.vel[1] ** 2 + self.vel[2] ** 2)
        mag2 = 1.0
        if mag1 > 0:
            dot = self.vel[1]
            angle = acos(dot / (mag1 * mag2))
            if angle < pi / 24:
                self.gone = True

    def display(self, sketch: Sketch):
        sketch.no_stroke()

        # angle between vel and (0, 1, 0)
        mag1 = sqrt(self.vel[0] ** 2 + self.vel[1] ** 2 + self.vel[2] ** 2)
        mag2 = 1.0
        angle = 0.0
        if mag1 > 0:
            dot = self.vel[1]
            angle = acos(dot / (mag1 * mag2))

        for i in range(len(self.pos)):
            s = float(sketch.remap(i, 0, len(self.pos) - 1, 2, 0))
            a = float(sketch.remap(i, 0, len(self.pos) - 1, angle * 100, 0))
            sketch.fill(self.hue, 100, 100, a)

            sketch.push_matrix()
            sketch.translate(self.pos[i][0], self.pos[i][1], self.pos[i][2])
            sketch.sphere(s)
            sketch.pop_matrix()
