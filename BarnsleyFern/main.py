# https://en.wikipedia.org/wiki/En/articles/Barnsley_fern

import os
from py5 import Sketch

WINDOW_HEIGHT = 800
X_RANGE = (-2.2, 2.7)
Y_RANGE = (0, 10)
TRACE_RADIUS = 0.005
UPDATES_PER_FRAME = 500


class BarnsleyFern(Sketch):
    x: float = 0.0
    y: float = 0.0

    def settings(self):
        self.size(
            int(WINDOW_HEIGHT / (Y_RANGE[1] - Y_RANGE[0]) * (X_RANGE[1] - X_RANGE[0])),
            WINDOW_HEIGHT,
        )

    def setup(self):
        self.ellipse_mode(self.RADIUS)
        self.background(245)
        self.no_stroke()
        self.fill(0, 100, 0, 100)
        self.frame_rate(60)

    def draw(self):
        self.translate(0, self.height)  # Move origin to bottom-left
        self.scale(1, -1)  # Flip Y-axis
        self.scale(
            self.height / (Y_RANGE[1] - Y_RANGE[0])
        )  # Given how the width is computed, we have scaleX == scaleY
        self.translate(-X_RANGE[0], 0)  # Shift fern to fit correctly

        for _ in range(UPDATES_PER_FRAME):
            self.iterate()

    def iterate(self):
        r = self.random(1)
        if r < 0.01:
            xn = 0.0
            yn = 0.16 * self.y
        elif r < 0.86:
            xn = 0.85 * self.x + 0.04 * self.y
            yn = -0.04 * self.x + 0.85 * self.y + 1.6
        elif r < 0.93:
            xn = 0.2 * self.x - 0.26 * self.y
            yn = 0.23 * self.x + 0.22 * self.y + 1.6
        else:
            xn = -0.15 * self.x + 0.28 * self.y
            yn = 0.26 * self.x + 0.24 * self.y + 0.44

        self.x, self.y = xn, yn
        self.circle(self.x, self.y, 0.01)

    def mouse_pressed(self):
        self.save(os.path.dirname(__file__) + "/barnsley_fern.jpg")


if __name__ == "__main__":
    sketch = BarnsleyFern()
    sketch.run_sketch()
