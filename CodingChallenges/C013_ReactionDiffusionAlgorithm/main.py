import os
from math import floor
from random import random
from py5 import Sketch
from tuple import Tuple


DA = 1.0
DB = 0.5
FEED = 0.055
KILL = 0.062
DT = 1.0
UPF = 5  # updates per frame


class C013_ReactionDiffusionAlgorithm(Sketch):
    _cells: list[list[Tuple]] = []
    _laplace: list[list[Tuple]] = []

    def settings(self):
        self.size(300, 300)

    def setup(self):
        self._cells = []
        self._laplace = []
        for x in range(self.width):
            cells_col = []
            laplace_col = []
            for y in range(self.height):
                cells_col.append(Tuple(1.0, 0.0))
                laplace_col.append(Tuple(1.0, 0.0))
            self._cells.append(cells_col)
            self._laplace.append(laplace_col)

        for i in range(10):
            cx = floor(random() * (self.width - 10))
            cy = floor(random() * (self.height - 10))
            for xoff in range(10):
                for yoff in range(10):
                    self._cells[cx + xoff][cy + yoff] = Tuple(1.0, 1.0)

        self.update_laplace()

    def draw(self):
        # Update
        for i in range(UPF):
            new_cells = []
            for x in range(self.width):
                col = []
                for y in range(self.height):
                    col.append(self.calc_new_values(x, y))
                new_cells.append(col)
            self._cells = new_cells
            self.update_laplace()

        # Draw
        self.load_pixels()
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                index = x + y * self.width
                self.pixels[index] = self.color((self._cells[x][y].a - self._cells[x][y].b) * 255)
        self.update_pixels()
        print(self.get_frame_rate())

    def calc_new_values(self, x: int, y: int) -> Tuple:
        old = self._cells[x][y]
        lp = self._laplace[x][y]
        a = old.a + (DA * lp.a - old.a * old.b * old.b + FEED * (1 - old.a)) * DT
        b = old.b + (DB * lp.b + old.a * old.b * old.b - (KILL + FEED) * old.b) * DT
        return Tuple(max(0, min(a, 1)), max(0, min(b, 1)))

    def update_laplace(self):
        # "The Laplacian is performed with a 3x3 convolution with center weight -1, adjacent neighbors .2, and diagonals .05"
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                a = self._cells[x][y].a * -1
                a += self._cells[x + 1][y].a * 0.2
                a += self._cells[x - 1][y].a * 0.2
                a += self._cells[x][y + 1].a * 0.2
                a += self._cells[x][y - 1].a * 0.2
                a += self._cells[x + 1][y + 1].a * 0.05
                a += self._cells[x + 1][y - 1].a * 0.05
                a += self._cells[x - 1][y + 1].a * 0.05
                a += self._cells[x - 1][y - 1].a * 0.05

                b = self._cells[x][y].b * -1
                b += self._cells[x + 1][y].b * 0.2
                b += self._cells[x - 1][y].b * 0.2
                b += self._cells[x][y + 1].b * 0.2
                b += self._cells[x][y - 1].b * 0.2
                b += self._cells[x + 1][y + 1].b * 0.05
                b += self._cells[x + 1][y - 1].b * 0.05
                b += self._cells[x - 1][y + 1].b * 0.05
                b += self._cells[x - 1][y - 1].b * 0.05

                self._laplace[x][y] = Tuple(a, b)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/reaction_diffusion.jpg")


if __name__ == "__main__":
    sketch = C013_ReactionDiffusionAlgorithm()
    sketch.run_sketch()
