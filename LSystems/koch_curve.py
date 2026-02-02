from math import pow, pi
from lsystem import LSystem
from py5 import Sketch


class KochCurve(LSystem):
    def __init__(self):
        r = {"f": "f+f--f+f"}
        super().__init__("f", r)

    def set_matrix(self, sketch: Sketch):
        sketch.translate(50, sketch.height - 50)

    def interpretate(self, k: str, sketch: Sketch):
        length = 400 * pow(1 / 3.0, self.n)

        if k == "f":
            sketch.line(0, 0, length, 0)
            sketch.translate(length, 0)
        elif k == "+":
            sketch.rotate(-pi / 3)
        elif k == "-":
            sketch.rotate(pi / 3)
