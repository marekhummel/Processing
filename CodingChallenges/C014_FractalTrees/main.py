import os
from math import pi
from py5 import Sketch


ANGLE = pi / 6
MAX_D = 1


class C014_FractalTrees(Sketch):
    angle: float = ANGLE
    maxd: int = MAX_D
    ticks: int = 0
    depth: int = 0

    def settings(self):
        self.size(600, 600)

    def setup(self):
        pass

    def draw(self):
        self.ticks += 1

        if self.ticks % 30 == 0:
            self.maxd += 1
        self.angle = float(self.remap(self.mouse_x, 0, self.width, 0, pi / 2))

        self.background(0)
        self.translate(self.width / 2, self.height)
        self.stroke_cap(self.ROUND)
        self.depth = 0
        self.branch(self.height * 0.3)

    def branch(self, len_: float):
        if self.depth == self.maxd or len_ < 4:
            self.leaf(len_)
            return

        self.depth += 1
        self.stroke(255)
        self.stroke_weight(len_ / 30)
        self.no_fill()
        self.line(0, 0, 0, -len_)

        self.translate(0, -len_)
        self.push_matrix()
        self.rotate(-self.angle)
        self.branch(len_ * 0.7)
        self.pop_matrix()
        self.push_matrix()
        self.rotate(self.angle)
        self.branch(len_ * 0.7)
        self.pop_matrix()
        self.depth -= 1

    def leaf(self, r: float):
        self.stroke(255)
        self.stroke_weight(1)
        self.fill(0, 255, 0, 127)
        self.ellipse(0, 0, r, r)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/fractal_trees.jpg")


if __name__ == "__main__":
    sketch = C014_FractalTrees()
    sketch.run_sketch()
