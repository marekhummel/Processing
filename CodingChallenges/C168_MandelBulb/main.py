from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from math import sqrt, atan2, sin, cos, pow
from py5 import Sketch


try:
    from peasy import PeasyCam  # type: ignore
except ImportError:
    import py5_tools

    py5_tools.processing.download_library("PeasyCam")
    from peasy import PeasyCam  # type: ignore


DIM = 128
N = 8
MAX_ITER = 20


class Computation:
    @staticmethod
    def compute_bulbs(i: int, j: int) -> list[tuple[float, float, float]]:
        bulbs = []
        edge = False
        for k in range(DIM):
            x = float(Computation.remap(i, 0, DIM - 1, -1, 1))
            y = float(Computation.remap(j, 0, DIM - 1, -1, 1))
            z = float(Computation.remap(k, 0, DIM - 1, -1, 1))
            v = (x, y, z)

            if Computation.calc_iterations(v):
                if not edge:
                    edge = True
                    bulbs.append(v)
            else:
                edge = False

        return bulbs

    @staticmethod
    def calc_iterations(v: tuple[float, float, float]) -> bool:
        x, y, z = v
        zeta = (0.0, 0.0, 0.0)
        for _ in range(MAX_ITER):
            r, theta, phi = Computation.cart_to_polar(zeta)
            if r > 2:
                break

            nx = pow(r, N) * sin(theta * N) * cos(phi * N)
            ny = pow(r, N) * sin(theta * N) * sin(phi * N)
            nz = pow(r, N) * cos(theta * N)
            zeta = (nx + x, ny + y, nz + z)
        else:
            return True

        return False

    @staticmethod
    def cart_to_polar(vec: tuple[float, float, float]) -> tuple[float, float, float]:
        x, y, z = vec
        x2 = x * x
        y2 = y * y
        r = sqrt(x2 + y2 + z * z)
        theta = atan2(sqrt(x2 + y2), z)
        phi = atan2(y, x)

        return (r, theta, phi)

    @staticmethod
    def remap(value: float, start1: float, stop1: float, start2: float, stop2: float) -> float:
        """Re-maps a number from one range to another."""
        return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))


class C168_MandelBulb(Sketch):
    bulb: list[tuple[float, float, float]] = []
    cam = None

    def settings(self):
        self.size(600, 600, self.P3D)

    def setup(self):
        PeasyCam(self, 600)

        print("Calculating MandelBulb points...")
        start = self.millis()
        self.bulb = []

        futures = []
        with ThreadPoolExecutor() as ppe:
            for i in range(DIM):
                for j in range(DIM):
                    futures.append(ppe.submit(Computation.compute_bulbs, i, j))

        for f in as_completed(futures):
            self.bulb.extend(f.result())

        print("Calculation took", self.millis() - start, "milliseconds")

    def draw(self):
        self.background(0)
        self.stroke(255)
        self.stroke_weight(1)

        for p in self.bulb:
            x, y, z = p
            self.point(x * 200, y * 200, z * 200)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/mandelbulb.jpg")


if __name__ == "__main__":
    sketch = C168_MandelBulb()
    sketch.run_sketch()
