import os
from math import sqrt, cos, sin, radians
from py5 import Sketch


class C030_Phyllotaxis(Sketch):
    c: float = 7.0
    angle: float = 0.0

    def settings(self):
        self.size(500, 500)

    def setup(self):
        self.c = 7.0
        self.angle = radians(137.7)  # .3 .5 .7

        self.color_mode(self.HSB, 1500, 100, 100)
        self.background(0)
        self.frame_rate(120)

    def draw(self):
        self.translate(self.width / 2, self.height / 2)

        r = 0.5 * self.c * sqrt(self.frame_count)
        theta = self.frame_count * self.angle
        px = r * cos(theta)
        py = r * sin(theta)

        self.fill(self.frame_count % 2500, 100, 100)
        self.ellipse(px, py, self.c, self.c)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/phyllotaxis.jpg")


if __name__ == "__main__":
    sketch = C030_Phyllotaxis()
    sketch.run_sketch()
