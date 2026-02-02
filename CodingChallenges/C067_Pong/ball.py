from random import uniform


class Ball:
    x: float
    y: float
    r: int = 8
    speedx: float
    speedy: float

    def __init__(self, x: int, y: int):
        self.x = float(x)
        self.y = float(y)
        self.r = 8

        self.speedx = uniform(-1, 1)
        self.speedy = uniform(-1, 1)
        scalar = 2.5 / (self.speedx**2 + self.speedy**2) ** 0.5
        self.speedx *= scalar
        self.speedy *= scalar

    def update(self):
        self.x += self.speedx
        self.y += self.speedy

    def draw(self, sketch):
        sketch.no_stroke()
        sketch.fill(255)
        sketch.ellipse(self.x, self.y, self.r << 1, self.r << 1)
