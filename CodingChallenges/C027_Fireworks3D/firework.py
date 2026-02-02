from random import random, uniform
from math import floor
from py5 import Sketch
from glower import Glower


class Firework:
    pos: list[float]
    speed: float
    hue: int
    exploded: bool = False
    gone: bool = False
    dust: list[Glower] = []

    def __init__(self, width: int, height: int):
        self.pos = [random() * width, height, random() * 20]
        self.speed = uniform(5, 6)
        self.hue = floor(random() * 360)
        self.exploded = False
        self._width = width
        self._height = height

    def update(self):
        if self.exploded:
            allgone = True
            for g in self.dust:
                g.update()
                allgone = allgone and g.gone
            if allgone:
                self.gone = True
            return

        self.pos[1] -= self.speed
        self.speed -= 0.05
        if self.speed <= 0.5:
            self.explode()

    def explode(self):
        self.exploded = True
        self.dust = []
        for i in range(floor(uniform(10, 20))):
            vx = random()
            vy = random()
            vz = random()
            self.dust.append(Glower(self.pos[:], [vx, vy, vz], self.hue))

    def display(self, sketch: Sketch):
        if not self.exploded:
            sketch.no_stroke()
            sketch.fill(self.hue, 100, 100, 80)

            sketch.push_matrix()
            sketch.translate(self.pos[0], self.pos[1], self.pos[2])
            sketch.sphere(5)
            sketch.pop_matrix()
        else:
            for g in self.dust:
                g.display(sketch)
