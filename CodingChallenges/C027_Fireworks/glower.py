from math import pi, atan2


class Glower:
    pos: list[float]
    vel: list[float]
    hue: int
    lifetime: int = 0
    gone: bool = False

    def __init__(self, p: list[float], v: list[float], h: int):
        self.pos = p.copy()
        self.vel = v.copy()
        self.hue = h
        self.gone = False
        self.lifetime = 0

    def update(self):
        self.vel[0] += 0
        self.vel[1] += 0.01
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        # Angle between vel and (0, 1)
        vel_mag = (self.vel[0] ** 2 + self.vel[1] ** 2) ** 0.5
        if vel_mag > 0:
            dot = self.vel[1]  # vel[0]*0 + vel[1]*1
            angle = abs(atan2((self.vel[0] ** 2) ** 0.5, dot))
            if angle < pi / 24:
                self.gone = True
        self.lifetime += 1

    def display(self, sketch):
        sketch.no_stroke()
        alpha = sketch.remap(self.lifetime, 0, 150, 100, 0)
        sketch.fill(self.hue, 100, 100, alpha)
        sketch.ellipse(self.pos[0], self.pos[1], 2, 2)
