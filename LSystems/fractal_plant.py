import math
from lsystem import LSystem
from py5 import Sketch


class FractalPlant(LSystem):
    def __init__(self):
        r = {"x": "f-[[x]+]+f[+fx]-x", "f": "ff"}
        super().__init__("x", r)

    def set_matrix(self, sketch: Sketch):
        sketch.translate(sketch.width / 2, sketch.height)
        sketch.rotate(-math.pi / 2)

    def interpretate(self, k: str, sketch: Sketch):
        length = 150 * pow(0.5, self.n)

        if k == "f":
            sketch.line(0, 0, length, 0)
            sketch.translate(length, 0)
        elif k == "+":
            sketch.rotate(math.radians(25))
        elif k == "-":
            sketch.rotate(-math.radians(25))
        elif k == "[":
            sketch.push_matrix()
        elif k == "]":
            sketch.pop_matrix()
