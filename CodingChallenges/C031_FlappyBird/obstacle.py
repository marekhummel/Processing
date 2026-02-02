from random import uniform


class Obstacle:
    x: float
    top: float
    bottom: float
    w: float = 40.0
    passed: bool = False

    def __init__(self, x_: float, height: int):
        self.x = x_

        gapsize = uniform(100, 300)
        self.top = uniform(-height / 2 + 20, height / 2 - 20 - gapsize)
        self.bottom = self.top + gapsize

    def hit(self, b) -> bool:
        if self.x + self.w / 2 < 0:
            self.passed = True

        if self.x - self.w / 2 > 0 or self.passed:
            return False
        return b.y - b.r <= self.top or b.y + b.r >= self.bottom

    def update(self):
        self.x -= 3

    def display(self, height: int, sketch):
        sketch.stroke_weight(5)
        sketch.stroke(0, 50)
        sketch.fill(0, 170, 0)

        sketch.rect(self.x - self.w / 2, -height / 2, self.w, height / 2 + self.top)
        sketch.rect(self.x - self.w / 2, height / 2, self.w, -(height / 2 - self.bottom))
