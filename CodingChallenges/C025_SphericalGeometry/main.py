import os
from math import sin, cos, pi
from py5 import Sketch

try:
    from peasy import PeasyCam  # type: ignore
except ImportError:
    import py5_tools

    py5_tools.processing.download_library("PeasyCam")
    from peasy import PeasyCam  # type: ignore


class C025_SphericalGeometry(Sketch):
    cam: PeasyCam

    def settings(self):
        self.size(600, 600, self.P3D)

    def setup(self):
        self.cam = PeasyCam(self, 600)

    def draw(self):
        self.background(51)
        self.lights()
        self.fill(255)
        self.usphere(150)

    def usphere(self, r: float):
        step = pi / 10
        lon = 0.0
        while lon <= self.TWO_PI + step:
            self.begin_shape(self.TRIANGLE_STRIP)
            lat = 0.0
            while lat <= pi:
                x = r * sin(lat) * cos(lon)
                y = r * sin(lat) * sin(lon)
                z = r * cos(lat)
                self.vertex(x, y, z)

                x2 = r * sin(lat) * cos(lon + step)
                y2 = r * sin(lat) * sin(lon + step)
                z2 = r * cos(lat)
                self.vertex(x2, y2, z2)

                lat += step / 2
            self.end_shape(self.CLOSE)
            lon += step

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/spherical_geometry.jpg")


if __name__ == "__main__":
    sketch = C025_SphericalGeometry()
    sketch.run_sketch()
