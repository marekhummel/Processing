import os
from math import floor, sqrt
from py5 import Sketch


ITER = 100


class C022_JuliaSet(Sketch):
    cre: float = 0.0
    cim: float = 0.0
    pts: list[list[int]] = []
    gradient: list[int] = []

    def settings(self):
        self.size(600, 400)

    def setup(self):
        self.pts = []
        for x in range(self.width + 1):
            col = []
            for y in range(self.height + 1):
                col.append(0)
            self.pts.append(col)

        self.set_gradient()

    def draw(self):
        self.cre = float(self.remap(self.mouse_x, 0, self.width, -2, 2))
        self.cim = float(self.remap(self.mouse_y, 0, self.height, 1, -1))

        self.load_pixels()
        x = -2.0
        while x < 2:
            y = -1.0
            while y < 1:
                i = 0
                re = x
                im = y
                while i < ITER:
                    nre = re * re - im * im + self.cre
                    nim = 2 * re * im + self.cim
                    re = nre
                    im = nim
                    if re * re + im * im > 4:
                        break
                    i += 1

                scx = floor(self.remap(x, -2, 2, 0, self.width - 1))
                scy = floor(self.remap(y, -1, 1, self.height - 1, 0))
                self.pixels[scy * self.width + scx] = self.color(sqrt(float(i) / ITER) * 255)

                y += 2.0 / self.height
            x += 4.0 / self.width

        self.update_pixels()

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

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/julia_set.jpg")


if __name__ == "__main__":
    sketch = C022_JuliaSet()
    sketch.run_sketch()
