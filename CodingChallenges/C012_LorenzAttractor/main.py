import os
from py5 import Sketch

try:
    from peasy import PeasyCam  # type: ignore
except ImportError:
    import py5_tools

    py5_tools.processing.download_library("PeasyCam")
    from peasy import PeasyCam  # type: ignore


class C012_LorenzAttractor(Sketch):
    _pts: list[list[float]] = []
    a: float = 10.0  # sigma
    b: float = 28.0  # rho
    c: float = 8.0 / 3.0  # beta
    dt: float = 0.01
    x: float = 0.1
    y: float = 0.0
    z: float = 0.0
    cam: PeasyCam

    def settings(self):
        self.size(600, 600, self.P3D)

    def setup(self):
        self.cam = PeasyCam(self, 100)
        self.cam.setMinimumDistance(10)
        self.color_mode(self.HSB, 360, 100, 100)
        self._pts = []

    def draw(self):
        # Calculate new point
        # dx / dt = a (y - x)
        # dy / dt = x (b - z) - y
        # dz / dt = xy - c * z
        # dt is basically the time difference, so u can set any fitting value
        # since dx,dy,dz are differences, the values are added to their old values
        dx = self.dt * self.a * (self.y - self.x)
        dy = self.dt * (self.x * (self.b - self.z) - self.y)
        dz = self.dt * (self.x * self.y - self.c * self.z)

        # Save
        self.x += dx
        self.y += dy
        self.z += dz
        self._pts.append([self.x, self.y, self.z])

        # Plot
        self.background(0)
        self.no_fill()

        hue = 0.0
        self.begin_shape()
        for p in self._pts:
            hue = (hue + 0.1) % 360
            self.stroke(hue, 100, 100)
            self.vertex(p[0], p[1], p[2])
        self.end_shape()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/lorenz_attractor.jpg")


if __name__ == "__main__":
    sketch = C012_LorenzAttractor()
    sketch.run_sketch()
