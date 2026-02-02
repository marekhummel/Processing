from math import pow, radians
from lsystem import LSystem
from py5 import Sketch


class FractalTree(LSystem):
    def __init__(self):
        r = {"f": "ff+[+f-f-f]-[-f+f+f]"}
        super().__init__("f", r)

    def set_matrix(self, sketch: Sketch):
        sketch.translate(sketch.width / 2, sketch.height)
        sketch.rotate(-sketch.HALF_PI)

    def interpretate(self, k: str, sketch: Sketch):
        length = 150 * pow(0.5, self.n)

        if k == "f":
            sketch.line(0, 0, length, 0)
            sketch.translate(length, 0)
        elif k == "+":
            sketch.rotate(radians(25))
        elif k == "-":
            sketch.rotate(-radians(25))
        elif k == "[":
            sketch.push_matrix()
        elif k == "]":
            sketch.pop_matrix()
