import os
from py5 import Sketch
from base_circle import BaseCircle
from lissajous_figure import LissajousCurve


SQSIZE = 100
SIZE_SCALAR = 0.85
SPEED_SCALAR = 0.015
COLORS = [0xFFFF00, 0x00FF00, 0x3124FF, 0xFF69B4, 0xFF0000]


class C116_LissajousTable(Sketch):
    base_circles_x: list[BaseCircle] = []
    base_circles_y: list[BaseCircle] = []
    lissajous: list[LissajousCurve] = []

    def settings(self):
        self.size(600, 400)
        self.smooth()

    def setup(self):
        # Init circles
        self.base_circles_x = []
        self.base_circles_y = []
        self.lissajous = []

        for i in range(1, self.width // SQSIZE):
            self.base_circles_x.append(
                BaseCircle(
                    i * SQSIZE, 0, SQSIZE * SIZE_SCALAR, i * SPEED_SCALAR, COLORS[i - 1], True
                )
            )
        for j in range(1, self.height // SQSIZE):
            self.base_circles_y.append(
                BaseCircle(
                    0, j * SQSIZE, SQSIZE * SIZE_SCALAR, j * SPEED_SCALAR, COLORS[j - 1], False
                )
            )

        # Init curves
        for i in range(1, self.width // SQSIZE):
            for j in range(1, self.height // SQSIZE):
                self.lissajous.append(
                    LissajousCurve(
                        i * SQSIZE,
                        j * SQSIZE,
                        SQSIZE * SIZE_SCALAR,
                        (self.base_circles_x[i - 1], self.base_circles_y[j - 1]),
                        self,
                    )
                )

    def draw(self):
        self.background(10)
        self.translate(SQSIZE >> 1, SQSIZE >> 1)

        # Draw the circles as orientation (basically the header of the table)
        for circle in self.base_circles_x + self.base_circles_y:
            circle.update(self)
            circle.draw(self)

        # Draw figures - calc_done describes whether new coordinates need to be calculated, or if the curve is now repeating itself
        calc_done = (
            self.base_circles_x[0].speed * self.frame_count > self.TWO_PI
            and self.base_circles_x[1].speed * self.frame_count > self.TWO_PI
        )
        for lissa in self.lissajous:
            lissa.update(calc_done, self)
            lissa.draw(self)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/lissajous_table.jpg")


if __name__ == "__main__":
    sketch = C116_LissajousTable()
    sketch.run_sketch()
