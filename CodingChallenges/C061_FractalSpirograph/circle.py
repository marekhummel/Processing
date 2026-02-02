from math import cos, sin
from py5 import Sketch


class Circle:
    r: float
    theta: float
    parent: "Circle | None" = None
    d: float
    x: float = 0.0
    y: float = 0.0
    speed: float

    def __init__(self, r_: float, p: "Circle | None", s: float, d_: float = 0.0):
        self.r = r_
        self.parent = p
        self.speed = s
        self.d = d_
        self.theta = 0

    def update(self):
        if self.parent is not None:
            self.x = self.parent.x + (self.parent.r + self.r) * cos(self.theta)
            self.y = self.parent.y + (self.parent.r + self.r) * sin(self.theta)
        self.theta -= self.speed

    def display(self, sketch: Sketch, circle_color: int):
        if self.r < 1:
            return
        sketch.stroke_weight(3 if self.parent is None else 1)
        sketch.stroke(circle_color)
        sketch.no_fill()
        sketch.ellipse(self.x, self.y, self.r, self.r)

    def trace(self, sketch: Sketch) -> list[float]:
        assert self.parent
        spin = self.theta * (self.parent.r / self.r + 1)
        tx = self.x - self.d * cos(spin)
        ty = self.y - self.d * sin(spin)

        if self.r > 2:
            sketch.line(self.x, self.y, tx, ty)
            sketch.no_stroke()
            sketch.fill(0, 127)
            sketch.ellipse(self.x, self.y, self.r / 4, self.r / 4)
            sketch.fill(255, 0, 0, 127)
            sketch.ellipse(tx, ty, 5, 5)

        return [tx, ty]
