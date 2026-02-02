from math import pow, pi
from lsystem import LSystem
from py5 import Sketch


class HexagonalGosper(LSystem):
    def __init__(self):
        r = {"x": "x+yf++yf-fx--fxfx-yf+", "y": "-fx+yfyf++yf+fx--fx-y"}
        super().__init__("xf", r)

    def set_matrix(self, sketch: Sketch):
        sketch.translate(2 * sketch.width / 3, sketch.height - 50)

    def interpretate(self, k: str, sketch: Sketch):
        length = 100 * pow(1 / 2.0, self.n)

        if k == "f":
            sketch.line(0, 0, length, 0)
            sketch.translate(length, 0)
        elif k == "+":
            sketch.rotate(-pi / 3)
        elif k == "-":
            sketch.rotate(pi / 3)
