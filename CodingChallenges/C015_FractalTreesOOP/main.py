import os
from math import pi
from py5 import Sketch
from branch import Branch


C = 5
A = pi / 6
MAX_D = 4


class C015_FractalTreesOOP(Sketch):
    _trunk: Branch
    ticks: int = 0
    depth: int = 0
    maxd: int = MAX_D
    c: int = C
    a: float = A

    def settings(self):
        self.size(400, 400)

    def setup(self):
        self._trunk = Branch([self.width / 2, self.height], [self.width / 2, self.height - 100])

    def draw(self):
        self.ticks += 1

        self.background(0)

        if self.ticks % 30 == 0:
            self.depth += 1
            if self.depth < self.maxd:
                self._trunk.add_children(self.c, self.a)
            elif self.depth == self.maxd:
                self._trunk.add_leaf()

        self._trunk.display(self)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/fractal_trees_oop.jpg")


if __name__ == "__main__":
    sketch = C015_FractalTreesOOP()
    sketch.run_sketch()
