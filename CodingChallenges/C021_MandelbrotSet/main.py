import os
from math import floor, sqrt
from py5 import Sketch


ITER = 256
OXMIN = -2.5
OXMAX = 1.0
OYMIN = -1.0
OYMAX = 1.0


class C021_MandelbrotSet(Sketch):
    xmin: float = 0.0
    xmax: float = 0.0
    ymin: float = 0.0
    ymax: float = 0.0
    zoompt: list[float] = [0.0, 0.0]
    zoom: float = 1.0
    pts: list[list[int]] = []
    gradient: list[int] = []

    def settings(self):
        self.size(700, 400)

    def setup(self):
        self.pts = []
        for x in range(self.width + 1):
            col = []
            for y in range(self.height + 1):
                col.append(0)
            self.pts.append(col)

        self.zoompt = [-0.75, 0.1]
        self.set_gradient()

        self.xmin = OXMIN
        self.xmax = OXMAX
        self.ymin = OYMIN
        self.ymax = OYMAX
        self.calc()

    def draw(self):
        zx = float(self.remap(self.mouse_x, 0, self.width, self.xmin, self.xmax))
        zy = float(self.remap(self.mouse_y, 0, self.height, self.ymax, self.ymin))
        self.zoompt = [zx, zy]

        self.load_pixels()
        for x in range(self.width):
            for y in range(self.height):
                self.pixels[y * self.width + x] = self.color(self.pts[x][y])
        self.update_pixels()

    def mouse_pressed(self, e):
        if e.get_button() == self.LEFT:
            self.zoom_in()

    def set_gradient(self):
        self.gradient = [
            self.color(0, 0, 0),
            self.color(25, 7, 26),
            self.color(9, 1, 47),
            self.color(4, 4, 73),
            self.color(0, 7, 100),
            self.color(12, 44, 138),
            self.color(24, 82, 177),
            self.color(57, 125, 209),
            self.color(134, 181, 229),
            self.color(211, 236, 248),
            self.color(241, 233, 191),
            self.color(248, 201, 95),
            self.color(255, 170, 0),
            self.color(204, 128, 0),
            self.color(153, 87, 0),
            self.color(106, 52, 3),
        ]

    def calc(self):
        step_x = (self.xmax - self.xmin) / self.width
        step_y = (self.ymax - self.ymin) / self.height
        x = self.xmin
        while x < self.xmax:
            y = self.ymin
            while y < self.ymax:
                i = 0
                re = x
                im = y
                while i < ITER:
                    nre = re * re - im * im + x
                    nim = 2 * re * im + y
                    re = nre
                    im = nim
                    if re * re + im * im > 4:
                        break
                    i += 1

                scx = floor(self.remap(x, self.xmin, self.xmax, 0, self.width))
                scy = floor(self.remap(y, self.ymin, self.ymax, self.height, 0))
                self.pts[scx][scy] = floor(sqrt(float(i) / ITER) * 255)

                y += step_y
            x += step_x

    def zoom_in(self):
        self.zoom *= 1.5

        self.xmin = self.zoompt[0] - (OXMAX - OXMIN) / (2 * self.zoom)
        self.xmax = self.zoompt[0] + (OXMAX - OXMIN) / (2 * self.zoom)
        self.ymin = self.zoompt[1] - (OYMAX - OYMIN) / (2 * self.zoom)
        self.ymax = self.zoompt[1] + (OYMAX - OYMIN) / (2 * self.zoom)

        print(self.xmin, self.xmax, self.ymin, self.ymax)

        self.calc()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/mandelbrot_set.jpg")


if __name__ == "__main__":
    sketch = C021_MandelbrotSet()
    sketch.run_sketch()
