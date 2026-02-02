import os
from math import cos, sin
from py5 import Sketch


RES = 200
WOBBLE = 1 / 5.0


class C036_Blobby(Sketch):
    r: float = 0.0
    t: float = 0.0

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.r = 1 / 3.0 * min(self.width, self.height)

    def draw(self):
        self.translate(self.width / 2, self.height / 2)

        self.background(51)
        self.no_stroke()
        self.fill(255)

        self.begin_shape()
        for s in range(RES):
            angle = s * self.TWO_PI / RES
            cr = self.r + float(
                self.remap(
                    self.noise(cos(angle) + 1, sin(angle) + 1, self.t),
                    0,
                    1,
                    -self.r * WOBBLE,
                    self.r * WOBBLE,
                )
            )
            x = cr * cos(angle)
            y = cr * sin(angle)
            self.vertex(x, y)
        self.end_shape()

        self.t += 0.01

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/blobby.jpg")


if __name__ == "__main__":
    sketch = C036_Blobby()
    sketch.run_sketch()
