# https://www.youtube.com/watch?v=FnRhnZbDprE

import math
import os
import py5

N = 6
DEPTH = 10

WINDOW = 800
BIG_CIRCLE_R = 0.8


class InitPoint:
    R = 0.2

    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.theta = py5.random(math.tau)
        self.delta = py5.random(-0.04, 0.04)

    def point(self):
        x = self.cx + py5.sin(self.theta) * self.R
        y = self.cy + py5.cos(self.theta) * self.R
        return (x, y)

    def draw(self, sketch: py5.Sketch):
        sketch.stroke(0, 100, 0)
        sketch.circle(self.cx, self.cy, self.R)

    def update(self):
        self.theta += self.delta


class RegularNGon(py5.Sketch):
    circles: list[InitPoint] = []

    def settings(self) -> None:
        self.size(WINDOW, WINDOW)

    def setup(self) -> None:
        self.ellipse_mode(self.RADIUS)
        self.setup_circles()

    def draw(self) -> None:
        # Center window at (0,0), edges are -1/+1
        self.translate(WINDOW / 2, WINDOW / 2)
        self.scale(WINDOW / 2)

        self.stroke_weight(0.005)
        self.no_fill()

        self.background(245)
        for c in self.circles:
            c.update()
            c.draw(self)

        points = [c.point() for c in self.circles]
        for i in range(DEPTH):
            points = self.iterate_midpoints(points, i == 0, i == DEPTH - 1)

    def key_typed(self, e):
        if e.get_key() == "s":
            elf.save(os.path.dirname(__file__) + "/regular_ngon.jpg")

    def setup_circles(self) -> None:
        self.circles = []
        for i in range(N):
            theta = math.tau * i / N
            x = math.sin(theta) * BIG_CIRCLE_R  # noqa: F821
            y = math.cos(theta) * BIG_CIRCLE_R
            self.circles.append(InitPoint(x, y))

    def iterate_midpoints(
        self, points: list[tuple[float, float]], outer: bool, inner: bool
    ) -> list[tuple[float, float]]:
        points.append(points[0])

        r = 0.01 if (outer or inner) else 0.003

        col = (220, 220, 220)
        if outer:
            col = (0, 0, 0)
        elif inner:
            col = (100, 0, 0)

        self.fill(*col)
        self.stroke(*col)

        midpoints = []
        for pi, pj in zip(points, points[1:]):
            dir = (pj[0] - pi[0], pj[1] - pi[1])
            midpoint = (pi[0] + dir[0] / 2, pi[1] + dir[1] / 2)
            midpoints.append(midpoint)

            self.circle(pi[0], pi[1], r)
            self.line(pi[0], pi[1], pj[0], pj[1])

        return midpoints


if __name__ == "__main__":
    sketch = RegularNGon()
    sketch.run_sketch()
