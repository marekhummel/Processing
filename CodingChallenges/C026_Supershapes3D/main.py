import os
from math import cos, sin, pi, pow, fabs
from py5 import Sketch

try:
    from peasy import PeasyCam  # type: ignore
except ImportError:
    import py5_tools

    py5_tools.processing.download_library("PeasyCam")
    from peasy import PeasyCam  # type: ignore

A = 1.0
B = 1.0
STEPS = 72


class C026_Supershapes3D(Sketch):
    cam: PeasyCam
    _shape: list[list[list[float]]] = []
    hoff: int = 0

    def settings(self):
        self.size(600, 600, self.P3D)

    def setup(self):
        self.color_mode(self.HSB, 360, 100, 100)
        self.cam = PeasyCam(self, 500)
        self._shape = []
        for _ in range(STEPS + 1):
            col = []
            for _ in range(STEPS + 1):
                col.append([0.0, 0.0, 0.0])
            self._shape.append(col)

    def draw(self):
        if self.frame_count % 2 == 0:
            self.hoff += 1
        self.background(0)
        self.lights()
        self.no_stroke()
        self.fill(255)
        self.supershape(150)

    def supershape(self, r: float):
        for pi_ in range(STEPS + 1):
            phi = float(self.remap(pi_, 0, STEPS, -self.HALF_PI, self.HALF_PI))
            for ti in range(STEPS + 1):
                theta = float(self.remap(ti, 0, STEPS, -pi, pi))

                r1 = self.cr(theta, 5, 0.1, 1.7, 1.7)
                r2 = self.cr(phi, 1, 0.3, 0.5, 0.5)

                x = r * r1 * cos(theta) * r2 * cos(phi)
                y = r * r1 * sin(theta) * r2 * cos(phi)
                z = r * r2 * sin(phi)
                self._shape[ti][pi_] = [x, y, z]

        for pi_ in range(STEPS):
            self.begin_shape(self.TRIANGLE_STRIP)
            self.fill(float(self.remap(pi_ + self.hoff, 0, STEPS, 0, 360 * 6)) % 360, 100, 100)
            for ti in range(STEPS + 1):
                v1 = self._shape[ti][pi_]
                v2 = self._shape[ti][pi_ + 1]
                self.vertex(v1[0], v1[1], v1[2])
                self.vertex(v2[0], v2[1], v2[2])
            self.end_shape()

    def cr(self, angle: float, m: float, n1: float, n2: float, n3: float) -> float:
        apart = pow(fabs(1.0 / A * cos(m / 4.0 * angle)), n2)
        bpart = pow(fabs(1.0 / B * sin(m / 4.0 * angle)), n3)
        r = 1.0 / pow(apart + bpart, 1.0 / n1)
        return r

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/supershapes_3d.jpg")


if __name__ == "__main__":
    sketch = C026_Supershapes3D()
    sketch.run_sketch()
