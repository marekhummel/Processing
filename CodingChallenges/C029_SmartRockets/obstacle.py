from py5 import Sketch


class Obstacle:
    x: float
    y: float
    w: float
    h: float

    def __init__(self, x_: float, y_: float, w_: float, h_: float):
        self.x = x_
        self.y = y_
        self.w = w_
        self.h = h_

    def hit(self, p: list[float]) -> bool:
        return (
            p[0] < self.x + self.w / 2
            and p[0] > self.x - self.w / 2
            and p[1] < self.y + self.h / 2
            and p[1] > self.y - self.h / 2
        )

    def display(self, sketch: Sketch):
        sketch.fill(255, 100)
        sketch.stroke_weight(3)
        sketch.stroke(255)
        sketch.rect(self.x, self.y, self.w, self.h)
