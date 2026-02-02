from random import uniform, randint
from math import pi, cos, sin
from glower import Glower


class Firework:
    pos: list[float]
    speed: float
    hue: int
    exploded: bool = False
    gone: bool = False
    dust: list[Glower] = []

    def __init__(self, width: int, height: int):
        self.pos = [uniform(0, width), float(height)]
        self.speed = uniform(5, 6)
        self.hue = randint(0, 359)
        self.exploded = False
        self.gone = False
        self.dust = []

    def update(self):
        if self.exploded:
            all_gone = True
            for g in self.dust:
                g.update()
                all_gone = all_gone and g.gone
            if all_gone:
                self.gone = True
            return

        self.pos[1] -= self.speed
        self.speed -= 0.05
        if self.speed <= 0.5:
            self.explode()

    def explode(self):
        self.exploded = True
        num_dust = randint(40, 69)
        self.dust = []
        for i in range(num_dust):
            # Random 2D vector
            angle = uniform(0, 2 * pi)
            mag = uniform(0, 1)
            v = [mag * cos(angle), mag * sin(angle)]
            self.dust.append(Glower(self.pos, v, self.hue))

    def display(self, sketch):
        if not self.exploded:
            sketch.no_stroke()
            sketch.fill(self.hue, 100, 100, 80)
            sketch.ellipse(self.pos[0], self.pos[1], 5, 5)
        else:
            for g in self.dust:
                g.display(sketch)
