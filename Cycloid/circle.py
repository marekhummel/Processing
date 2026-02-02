from math import cos, sin


CIRCLE = (255, 127)
TRACE = (255, 100, 100)


class Circle:
    r: float
    theta: float = 0.0
    parent: "Circle | None"
    epi: bool
    d: float
    x: float = 0.0
    y: float = 0.0
    speed: float

    def __init__(self, r_: float, p: "Circle | None", e: bool, s: float, d_: float | None = None):
        self.r = r_
        self.parent = p
        self.epi = e
        self.speed = s
        self.d = d_ if d_ is not None else r_
        self.theta = 0.0

    def update(self):
        if self.parent is not None:
            self.x = self.parent.x
            self.x += self.parent.r * cos(self.theta)
            self.x += (1 if self.epi else -1) * self.r * cos(self.theta)
            self.y = self.parent.y
            self.y += self.parent.r * sin(self.theta)
            self.y += (1 if self.epi else -1) * self.r * sin(self.theta)

        self.theta -= self.speed

    def display(self, sketch):
        if self.r < 1:
            return
        sketch.stroke_weight(3 if self.parent is None else 1)
        sketch.stroke(*CIRCLE)
        sketch.no_fill()
        sketch.ellipse(self.x, self.y, self.r, self.r)

    def draw_trace(self, t: tuple[float, float], sketch):
        if self.r > 2:
            sketch.stroke(*CIRCLE)
            sketch.line(self.x, self.y, t[0], t[1])
            sketch.no_stroke()
            sketch.fill(*CIRCLE)
            sketch.ellipse(self.x, self.y, self.r / 4, self.r / 4)
            sketch.fill(*TRACE)
            sketch.ellipse(t[0], t[1], 5, 5)

    def trace(self) -> tuple[float, float]:
        assert self.parent
        spin = self.theta * (self.parent.r / self.r + 1)
        tx = self.x - self.d * cos(spin)
        ty = self.y - self.d * sin(spin)

        return (tx, ty)
