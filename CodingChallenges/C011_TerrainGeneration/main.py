import os
from math import pi
from py5 import Sketch


W = 1600
H = 1200
SCL = 20.0


class C011_TerrainGeneration(Sketch):
    _rows: int = 0
    _cols: int = 0
    z: list[list[float]] = []
    _off: float = 0.0

    def settings(self):
        self.size(600, 300, self.P3D)

    def setup(self):
        self._rows = int(H / SCL)
        self._cols = int(W / SCL)

        self.z = []
        for i in range(self._cols):
            col = []
            for j in range(self._rows):
                col.append(0.0)
            self.z.append(col)

    def draw(self):
        self._off += 0.04
        for j in range(self._rows):
            for i in range(self._cols):
                self.z[i][j] = float(
                    self.remap(self.noise(0.1 * i, 0.1 * j + self._off), 0, 1, -100, 100)
                )

        self.background(0)

        self.translate(self.width / 2, self.height / 2)
        self.rotate_x(pi / 2)
        self.translate(0, 0, -self.height / 2 - 50)

        self.stroke(255)
        self.fill(10)

        for j in range(1, self._rows):
            y = -j * SCL

            self.begin_shape(self.TRIANGLE_STRIP)
            for i in range(self._cols):
                x = i * SCL - W / 2

                self.vertex(x, y, self.z[i][j])
                self.vertex(x, y + SCL, self.z[i][j - 1])
            self.end_shape()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/terrain_generation.jpg")


if __name__ == "__main__":
    sketch = C011_TerrainGeneration()
    sketch.run_sketch()
