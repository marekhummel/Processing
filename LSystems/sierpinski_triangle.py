from math import pow, radians
from lsystem import LSystem
from py5 import Sketch


class SierpinskiTriangle(LSystem):
    def __init__(self):
        r = {"f": "f-g+f+g-f", "g": "gg"}
        super().__init__("f-g-g", r)

    def set_matrix(self, sketch: Sketch):
        sketch.translate(50, 50)

    def interpretate(self, k: str, sketch: Sketch):
        length = 400 * pow(1 / 2.0, self.n)

        if k in ["f", "g"]:
            sketch.line(0, 0, length, 0)
            sketch.translate(length, 0)
        elif k == "+":
            sketch.rotate(-radians(120))
        elif k == "-":
            sketch.rotate(radians(120))
