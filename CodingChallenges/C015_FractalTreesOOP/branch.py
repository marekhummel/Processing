from math import floor, atan2, cos, sin, sqrt
from py5 import Sketch
from leaf import Leaf


class Branch:
    start: list[float]
    end: list[float]
    children: list["Branch"] | None = None
    leaf: Leaf | None = None

    def __init__(self, s: list[float], e: list[float]):
        self.start = s[:]
        self.end = e[:]

    def add_children(self, c: int, angle: float):
        if self.children is not None:
            for b in self.children:
                b.add_children(c, angle)
            return

        # dir = end - start
        dir_x = self.end[0] - self.start[0]
        dir_y = self.end[1] - self.start[1]

        self.children = []
        for i in range(c):
            m = (i / (c - 1) if c > 1 else 0) * (2 * floor(c / 2.0)) - floor(c / 2.0)

            # Rotate dir by m * angle
            d_x = dir_x * 0.7
            d_y = dir_y * 0.7

            # Rotate
            current_angle = atan2(d_y, d_x)
            new_angle = current_angle + m * angle
            mag = sqrt(d_x * d_x + d_y * d_y)
            d_x = mag * cos(new_angle)
            d_y = mag * sin(new_angle)

            newend = [self.end[0] + d_x, self.end[1] + d_y]
            self.children.append(Branch(self.end, newend))

    def add_leaf(self):
        if self.children is not None:
            for b in self.children:
                b.add_leaf()
            return

        self.leaf = Leaf(self.end[0], self.end[1])

    def display(self, sketch: Sketch):
        sketch.stroke_cap(sketch.ROUND)
        sketch.stroke_weight(2)
        sketch.stroke(255)
        sketch.line(self.start[0], self.start[1], self.end[0], self.end[1])
        if self.leaf is not None:
            self.leaf.display(sketch)

        if self.children is None:
            return
        for b in self.children:
            b.display(sketch)
