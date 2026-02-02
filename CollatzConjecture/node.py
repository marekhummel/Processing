from math import pi, cos, sin


class Node:
    value: int
    children: list["Node"]
    r: float = 5.0
    df: float = 3.0
    a: float = pi / 13
    hl: bool = False

    def __init__(self, v: int):
        self.value = v
        self.children = []

    def add_children(self, limit: int, vals: list[int]) -> bool:
        if self.value * 2 < limit and (self.value * 2) not in vals:
            self.children.append(Node(self.value * 2))

        if (self.value * 2 - 1) % 3 == 0 and self.value > 2:
            nv = (self.value * 2 - 1) // 3
            if nv not in vals:
                self.children.append(Node(nv))

        return len(self.children) != 0

    def display(self, x: float, y: float, angle: float, sketch):
        if self.children is not None:
            for c in self.children:
                oa = angle
                if (c.value & 1) == 0:
                    angle -= self.a
                else:
                    angle += self.a

                nx = x + self.df * self.r * cos(angle)
                ny = y - self.df * self.r * sin(angle)

                sketch.stroke_weight(5)
                sketch.stroke(255, 100)
                sketch.line(x, y, nx, ny)

                c.display(nx, ny, angle, sketch)
                angle = oa

        if self.hl:
            sketch.fill(255, 0, 0)
        else:
            sketch.fill(255)
        sketch.no_stroke()
        sketch.stroke_weight(1)
        sketch.ellipse(x, y, self.r, self.r)
        self.hl = False

        sketch.fill(0)
        # sketch.text(str(self.value), x, y)
