import os
from math import pow, pi
from py5 import Sketch
from circle import Circle


BACKGROUND = (54, 54, 54)
K = -4
S = 3
FREQ = 50


class C061_FractalSpirograph(Sketch):
    circles: list[Circle] = []
    tracepts: list[list[float]] = []
    circle_color: int = 0
    trace_color: int = 0

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.ellipse_mode(self.RADIUS)
        self.circle_color = self.color(255, 127)
        self.trace_color = self.color(255, 100, 100)

        scale = 1 / (180 / pi * FREQ)
        self.circles = []
        self.circles.append(Circle(100, None, pow(K, 0) * scale))
        for i in range(1, 11):
            last = self.circles[-1]
            self.circles.append(Circle(last.r / S, last, pow(K, i) * scale))

        self.tracepts = []

    def draw(self):
        # Update
        for _ in range(FREQ):
            for c in self.circles:
                c.update()
            newpt = self.circles[-1].trace(self)
            if newpt not in self.tracepts:
                self.tracepts.append(newpt)

        # Draw
        self.translate(self.width / 2, self.height / 2)
        self.rotate(-self.HALF_PI)
        self.background(*BACKGROUND)
        for c in self.circles:
            c.display(self, self.circle_color)

        self.stroke(self.trace_color)
        self.stroke_weight(1)
        self.no_fill()
        self.begin_shape()
        for pt in self.tracepts:
            self.vertex(pt[0], pt[1])
        self.end_shape()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/fractal_spirograph.jpg")


if __name__ == "__main__":
    sketch = C061_FractalSpirograph()
    sketch.run_sketch()
