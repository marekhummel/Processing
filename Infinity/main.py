import os
import math
from py5 import Sketch, Py5Vector

N = 120
C = 90  # 82


class Infinity(Sketch):
    pos: list[Py5Vector] = []
    angle: float = 0.0

    def settings(self):
        self.size(500, 500)

    def setup(self):
        self.color_mode(self.HSB, 180, 100, 100)
        for _ in range(N):
            self.pos.append(Py5Vector(self.width / 2, self.height / 2))

    def draw(self):
        self.background(0)
        self.no_stroke()

        x = self.width / 2 + math.cos(self.angle) * 150
        y = self.height / 2 + math.sin(2 * self.angle) * 150
        l = Py5Vector(x, y)
        for i in range(N):
            self.fill(180 / N * i, 90, 90)
            p = self.pos[i]
            v = 0.5 * (l - p)
            p += v
            self.circle(p.x, p.y, 70)
            l = p

        self.angle += math.pi / C

    def key_typed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/infinity.jpg")


if __name__ == "__main__":
    sketch = Infinity()
    sketch.run_sketch()
