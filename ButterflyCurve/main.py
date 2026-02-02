import os
from py5 import Sketch
import math

SCALE: int = 50


class ButterflyCurve(Sketch):
    t: float = 0.0
    lx: float = 0.0
    ly: float = 0.0

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.background(245)
        self.lx = 0
        self.ly = -math.exp(1) + 2

        steps = 400
        self.translate(self.width / 2, self.height / 2)
        self.no_stroke()
        self.fill(150)
        for i in range(steps):
            self.ellipse(float(self.lerp(-self.width, self.width, i / steps)), 0, 1, 1)
            self.ellipse(0, float(self.lerp(-self.height, self.height, i / steps)), 1, 1)

        theta = 0
        while theta < math.tau:
            for r in range(1, 10):
                self.ellipse(r * SCALE * math.cos(theta), r * SCALE * math.sin(theta), 1, 1)
            theta += math.pi / steps * 2

        self.frame_rate(180)

    def draw(self):
        self.translate(self.width / 2, self.height / 2)

        r = (
            math.exp(math.cos(self.t))
            - 2 * math.cos(4 * self.t)
            - math.pow(math.sin(self.t / 12), 5)
        )
        x = math.sin(self.t) * r
        y = math.cos(self.t) * r
        self.stroke(255, 0, 0, 100)
        self.line(x * SCALE, y * SCALE, self.lx * SCALE, self.ly * SCALE)

        self.lx = x
        self.ly = y
        self.t += 0.04

    def key_typed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/butterfly_curve.jpg")


if __name__ == "__main__":
    sketch = ButterflyCurve()
    sketch.run_sketch()
