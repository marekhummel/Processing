import os
from math import pi
from py5 import Sketch
from circle import Circle, TRACE


BACKGROUND = (54,)
FREQ = 50


class Cycloid(Sketch):
    circles: list[Circle] = []
    tracepts: list[tuple[float, float]] = []

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.ellipse_mode(self.RADIUS)

        self.circles = []
        self.circles.append(Circle(150, None, False, 0))
        self.circles.append(Circle(50, None, True, 2 * pi / 3600))
        self.circles.append(Circle(10, None, False, 2 * pi / 1200))
        for i in range(1, len(self.circles)):
            self.circles[i].parent = self.circles[i - 1]

        self.tracepts = []

    def draw(self):
        # Update
        for i in range(FREQ):
            for c in self.circles:
                c.update()
            newpt = self.circles[-1].trace()
            if newpt not in self.tracepts:
                self.tracepts.append(newpt)

        # Draw
        self.translate(self.width / 2, self.height / 2)
        self.rotate(-self.HALF_PI)
        self.background(*BACKGROUND)
        for c in self.circles:
            c.display(self)
        self.circles[-1].draw_trace(self.tracepts[-1], self)

        self.stroke(*TRACE)
        self.stroke_weight(1)
        self.no_fill()
        self.begin_shape()
        for pt in self.tracepts:
            self.vertex(pt[0], pt[1])
        self.end_shape()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/cycloid.jpg")


if __name__ == "__main__":
    sketch = Cycloid()
    sketch.run_sketch()
