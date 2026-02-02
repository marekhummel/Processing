import os
import math
from py5 import Sketch, radians, color

WINDOW = 800
RANGE = 3
START_ANGLE: float = radians(-30)  # type: ignore

colors = [
    color(255, 100, 100),
    color(100, 255, 100),
    color(100, 100, 255),
    color(255, 255, 100),
    color(255, 100, 255),
    color(100, 255, 255),
]


class TrigFunctions(Sketch):
    scaling: float
    angle: float = START_ANGLE
    stop_update: bool = False

    def settings(self):
        self.size(WINDOW, WINDOW)

    def setup(self):
        self.scaling = float(WINDOW / (2 * RANGE))
        self.ellipse_mode(self.RADIUS)
        self.text_align(self.CENTER, self.CENTER)
        self.no_stroke()

    def draw(self):
        self.scale(self.scaling)
        self.translate(RANGE, RANGE)

        self.grid()
        self.mainline()
        self.trigs()
        self.labels()

    def mouse_moved(self):
        if not self.stop_update:
            self.angle = math.atan2(self.mouse_y - self.height / 2, self.mouse_x - self.width / 2)

    def mouse_pressed(self):
        if self.mouse_button == self.LEFT:
            self.stop_update = not self.stop_update
            self.mouse_moved()

    def key_typed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/trigs.jpg")

    def grid(self):
        self.background(20)
        self.stroke_weight(1 / self.scaling)
        self.stroke(50)
        for i in range(int(4 * RANGE)):
            xy = -RANGE + i * 0.5
            self.line(-RANGE, xy, RANGE, xy)
            self.line(xy, -RANGE, xy, RANGE)
        self.stroke(150)
        self.line(-RANGE, 0, RANGE, 0)
        self.line(0, -RANGE, 0, RANGE)

        self.no_fill()
        self.stroke(255)
        self.stroke_weight(3 / self.scaling)
        self.circle(0, 0, 1)

    def mainline(self):
        self.push_matrix()
        self.stroke(255)
        self.stroke_weight(2 / self.scaling)
        self.rotate(self.angle)
        self.line(0, 0, 2 * RANGE, 0)
        self.pop_matrix()

    def trigs(self):
        cosa, sina = math.cos(self.angle), math.sin(self.angle)
        seca = 1 / cosa if cosa != 0 else 500 * RANGE
        csca = 1 / sina if sina != 0 else 500 * RANGE

        # cos sin tan cot csc sec
        lines = [
            (cosa, 0, cosa, sina),
            (0, sina, cosa, sina),
            (cosa, sina, seca, 0),
            (cosa, sina, 0, csca),
            (0, 0, 0, csca),
            (0, 0, seca, 0),
        ]

        for c, l in zip(colors, lines):
            self.stroke(c)
            self.line(*l)

        self.no_stroke()
        self.fill(255)
        self.circle(0, 0, 3 / self.scaling)
        self.circle(cosa, sina, 3 / self.scaling)

    def labels(self):
        # Manual scaling due to text size
        self.scale(1 / self.scaling)

        # Values
        cosa, sina = math.cos(self.angle) * self.scaling, math.sin(self.angle) * self.scaling
        seca = (1 / math.cos(self.angle) if cosa != 0 else RANGE) * self.scaling
        csca = (1 / math.sin(self.angle) if sina != 0 else RANGE) * self.scaling
        halfway = RANGE * self.scaling // 2

        def clamp_halfway(val):
            return max(-halfway, min(val, halfway))

        # cos sin tan cot csc sec
        labels = [
            ("sin", cosa - 15, sina // 2),
            ("cos", cosa // 2, sina + 6),
            ("tan", clamp_halfway((cosa + seca) // 2) + 20, sina // 2 + 6),
            ("cot", cosa // 2 + 20, clamp_halfway((sina + csca) // 2 + 6)),
            ("csc", -15, clamp_halfway(csca // 2)),
            ("sec", clamp_halfway(seca // 2), 6),
        ]

        for c, l in zip(colors, labels):
            self.fill(c)
            self.text(*l)


if __name__ == "__main__":
    sketch = TrigFunctions()
    sketch.run_sketch()
