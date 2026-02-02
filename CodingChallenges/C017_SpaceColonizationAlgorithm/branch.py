from math import pow
from py5 import Sketch


class Branch:
    pos: list[float]
    dir: list[float]
    parent: "Branch | None"
    attrac_dir: list[float]
    children: list["Branch"]

    def __init__(
        self, p: list[float], d: list[float], par: "Branch | None" = None, m: float = 1.0
    ):
        if par is None:
            self.pos = p[:]
            self.dir = d[:]
            self.parent = None
        else:
            self.pos = [par.pos[0] + d[0] * m, par.pos[1] + d[1] * m]
            self.dir = d[:]
            self.parent = par

        self.children = []
        self.attrac_dir = [0.0, 0.0]

    def get_r(self) -> float:
        exp = 2.7
        if len(self.children) == 0:
            return 0.5

        sum_val = 0.0
        for c in self.children:
            sum_val += pow(c.get_r(), exp)
        return pow(sum_val, 1 / exp)

    def display(self, sketch: Sketch):
        if self.parent is None:
            return

        sketch.stroke(127, 10, 10)
        sketch.stroke_weight(self.get_r() * 2)
        sketch.line(self.parent.pos[0], self.parent.pos[1], self.pos[0], self.pos[1])
