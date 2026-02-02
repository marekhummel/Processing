import os
from py5 import Sketch

from lsystem import LSystem

# ruff: noqa: F401
from fractal_tree import FractalTree
from koch_curve import KochCurve
from sierpinski_triangle import SierpinskiTriangle
from sierpinski_curve import SierpinskiCurve
from dragon_curve import DragonCurve
from fractal_plant import FractalPlant
from hexagonal_gosper import HexagonalGosper
from penrose_tiling import PenroseTiling


class LSystems(Sketch):
    ls: LSystem

    def settings(self):
        self.size(500, 500)

    def setup(self):
        # self.ls = FractalTree()
        # self.ls = KochCurve()
        # self.ls = SierpinskiTriangle()
        self.ls = SierpinskiCurve()
        # self.ls = DragonCurve()
        # self.ls = FractalPlant()
        # self.ls = HexagonalGosper()
        # self.ls = PenroseTiling()

        self.frame_rate(1)

    def draw(self):
        self.background(0)
        print(self.ls.n)

        self.stroke(255, 100)

        self.ls.set_matrix(self)

        for i in range(len(self.ls.current_state)):
            self.ls.interpretate(self.ls.current_state[i], self)

        self.ls.produce()

    def key_typed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + f"/lsystems_{self.ls.__class__.__name__}.jpg")


if __name__ == "__main__":
    sketch = LSystems()
    sketch.run_sketch()
