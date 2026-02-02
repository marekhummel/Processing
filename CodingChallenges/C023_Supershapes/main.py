import os
from math import pow, cos, sin, pi, fabs
from py5 import Sketch


# http://paulbourke.net/geometry/supershape/

A = 1.0
B = 1.0
N1 = 0.1
N2 = 1.7
N3 = 1.7
M = 5.0


class C023_Supershapes(Sketch):
    def settings(self):
        self.size(500, 500)

    def setup(self):
        self.no_loop()

    def draw(self):
        self.translate(self.width / 2, self.height / 2)
        self.scale(0.9 * self.width / 2, 0.9 * self.height / 2)
        self.background(51)

        self.stroke(255)
        self.stroke_weight(0.005)
        self.no_fill()
        self.begin_shape()
        theta = 0.0
        while theta < self.TWO_PI:
            apart = pow(fabs(1.0 / A * cos(M / 4.0 * theta)), N2)
            bpart = pow(fabs(1.0 / B * sin(M / 4.0 * theta)), N3)
            r = 1.0 / pow(apart + bpart, 1.0 / N1)

            x = r * cos(theta)
            y = r * sin(theta)
            self.vertex(x, y)

            theta += pi / 200
        self.end_shape(self.CLOSE)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/supershapes.jpg")


if __name__ == "__main__":
    sketch = C023_Supershapes()
    sketch.run_sketch()
