import os
from math import pow, pi, cos, sin, fabs
from py5 import Sketch


class C019_Superellipse(Sketch):
    a: float = 1.0
    b: float = 1.0
    n: float = 1 / 2.0

    def settings(self):
        self.size(500, 500)

    def setup(self):
        self.no_loop()

    def draw(self):
        self.translate(self.width / 2, self.height / 2)
        self.scale(0.9 * self.width / 2, 0.9 * self.height / 2)
        self.background(0)

        self.stroke(255)
        self.stroke_weight(0.01)
        self.no_fill()
        self.begin_shape()
        theta = 0
        while theta < self.TWO_PI:
            x = pow(fabs(cos(theta)), 2.0 / self.n) * self.a * self.sgn(cos(theta))
            y = pow(fabs(sin(theta)), 2.0 / self.n) * self.b * self.sgn(sin(theta))
            self.vertex(x, y)
            theta += pi / 36
        self.end_shape()

    def sgn(self, a: float) -> int:
        if a > 0:
            return 1
        if a < 0:
            return -1
        return 0

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/superellipse.jpg")


if __name__ == "__main__":
    sketch = C019_Superellipse()
    sketch.run_sketch()
