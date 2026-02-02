from math import pow, radians
from lsystem import LSystem
from py5 import Sketch


class SierpinskiCurve(LSystem):
    def __init__(self):
        r = {"a": "+b-a-b+", "b": "-a+b+a-"}
        super().__init__("a", r)

    def set_matrix(self, sketch: Sketch):
        sketch.translate(50, sketch.height - 50)

    def interpretate(self, k: str, sketch: Sketch):
        length = 400 * pow(1 / 2.0, self.n)

        if k in ["a", "b"]:
            sketch.line(0, 0, length, 0)
            sketch.translate(length, 0)
        elif k == "+":
            sketch.rotate(-radians(60))
        elif k == "-":
            sketch.rotate(radians(60))
