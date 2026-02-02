import os
from math import pow, floor, log
from py5 import Sketch


XMIN = -40
XMAX = 60
YMIN = -5
YMAX = 10


def f(x):
    return 1 / x


class FunctionPlotter(Sketch):
    xscl: float = 0.0
    yscl: float = 0.0

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.xscl = self.width / (XMAX - XMIN)
        self.yscl = self.height / (YMAX - YMIN)

    def draw(self):
        self.background(245)
        self.translate(
            float(self.remap(0, XMIN, XMAX, 0, self.width)),
            float(self.remap(0, YMIN, YMAX, self.height, 0)),
        )
        self.scale(self.xscl, self.yscl)

        self.grid()

        # Plot
        self.no_fill()
        self.stroke(255, 0, 0)
        self.stroke_weight(1 / min(self.xscl, self.yscl))
        self.begin_shape()
        x = XMIN
        while x <= XMAX:
            self.vertex(x, -f(x))
            x += 2 / self.xscl
        self.end_shape()
        self.no_loop()
        self.save(os.path.dirname(__file__) + "/function_plotter.jpg")

    def grid(self):
        xdist = pow(10, floor(log(XMAX - XMIN) / log(10)) - 1)
        ydist = pow(10, floor(log(YMAX - YMIN) / log(10)) - 1)

        self.stroke(0, 50)
        i = 0
        while True:
            self.stroke_weight((3 if i == 0 else 1) / self.xscl)
            self.line(i * xdist, -YMIN, i * xdist, -YMAX)
            self.line(-i * xdist, -YMIN, -i * xdist, -YMAX)
            if i * xdist > XMAX and -i * xdist < XMIN:
                break
            i += 1

        i = 0
        while True:
            self.stroke_weight((3 if i == 0 else 1) / self.yscl)
            self.line(XMIN, -i * ydist, XMAX, -i * ydist)
            self.line(XMIN, i * ydist, XMAX, i * ydist)
            if i * ydist > YMAX and -i * ydist < YMIN:
                break
            i += 1

        self.push_matrix()
        self.reset_matrix()
        self.no_stroke()
        self.fill(0)
        self.text_size(10)
        self.text_align(self.LEFT, self.TOP)
        self.text(f"{xdist:.2f}|{ydist:.2f}", 10, 10)
        self.pop_matrix()


if __name__ == "__main__":
    sketch = FunctionPlotter()
    sketch.run_sketch()
