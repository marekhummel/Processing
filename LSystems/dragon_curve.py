import math
from lsystem import LSystem

from py5 import Sketch


class DragonCurve(LSystem):
    def __init__(self):
        r = {"x": "x+yf+", "y": "-fx-y"}
        super().__init__("fx", r)

    def set_matrix(self, sketch: Sketch):
        sketch.translate(sketch.width / 2, sketch.height / 2)

    def interpretate(self, k: str, sketch: Sketch):
        length = 200 * math.pow(7 / 10.0, self.n)

        if k == "f":
            sketch.line(0, 0, length, 0)
            sketch.translate(length, 0)
        elif k == "+":
            sketch.rotate(-math.pi / 2)
        elif k == "-":
            sketch.rotate(math.pi / 2)
