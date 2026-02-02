from math import pow, radians
from lsystem import LSystem
from py5 import Sketch


class PenroseTiling(LSystem):
    # Axiom:
    # [N]++[N]++[N]++[N]++[N]
    # Rules:
    # M=OA++pA----NA[-OA----MA]++;
    # N=+OA--PA[---MA--NA]+;
    # O=-MA++NA[+++OA++PA]-;
    # P=;
    # A=
    # Angle:36

    def __init__(self):
        r = {
            "m": "oa++pa----na[-oa----ma]++",
            "n": "+oa--pa[---ma--na]+",
            "o": "-ma++na[+++oa++pa]-",
            "p": "--oa++++ma[+pa++++na]--na",
            "a": "",
        }
        super().__init__("[n]++[n]++[n]++[n]++[n]", r)

    def set_matrix(self, sketch: Sketch):
        sketch.translate(sketch.width / 2, sketch.height / 2)

    def interpretate(self, k: str, sketch: Sketch):
        length = 200 * pow(1 / 2.0, self.n)

        if k in ["m", "n", "o", "p", "a"]:
            sketch.line(0, 0, length, 0)
            sketch.translate(length, 0)
        elif k == "+":
            sketch.rotate(-radians(36))
        elif k == "-":
            sketch.rotate(radians(36))
        elif k == "[":
            sketch.push_matrix()
        elif k == "]":
            sketch.pop_matrix()
