import os
from math import sqrt, ceil, floor, pi, cos, sin
from random import uniform
from py5 import Sketch


# http://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph07-poissondisk.pdf

R = 15.0
K = 30
CS = R / sqrt(2)


class C033_PoissonDiskSampling(Sketch):
    rows: int = 0
    cols: int = 0
    grid: list[list[float] | None] = []
    active: list[list[float]] = []

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.cols = ceil(self.width / CS)
        self.rows = ceil(self.height / CS)

        self.grid = [None] * (self.cols * self.rows)
        self.active = []

        x0 = [float(self.width / 2), float(self.height / 2)]
        self.grid[self.gridindex(x0)] = x0
        self.active.append(x0)

        self.background(0)
        self.no_fill()
        self.stroke_weight(0.5 * R)
        self.stroke(255)

    def draw(self):
        idx = floor(uniform(0, len(self.active)))
        apt = self.active[idx]

        found_new = False
        for i in range(K):
            # Random 2D vector with magnitude between r and 2*r
            angle = uniform(0, 2 * pi)
            mag = uniform(R, 2 * R)
            npt = [apt[0] + mag * cos(angle), apt[1] + mag * sin(angle)]

            if npt[0] > CS * self.cols or npt[0] < 0 or npt[1] < 0 or npt[1] > CS * self.rows:
                continue

            grid_idx = self.gridindex(npt)
            if self.grid[grid_idx] is not None:
                continue

            neighbors = self.get_neighbors(grid_idx)
            too_close = False
            for n in neighbors:
                dist = sqrt((npt[0] - n[0]) ** 2 + (npt[1] - n[1]) ** 2)
                if dist < R:
                    too_close = True
                    break

            if not too_close:
                self.point(npt[0], npt[1])
                self.grid[grid_idx] = npt
                self.active.append(npt)
                found_new = True
                break

        if not found_new:
            self.active.pop(idx)

        if len(self.active) == 0:
            self.no_loop()
            print("FINISHED")

    def gridindex(self, p: list[float]) -> int:
        return floor(p[0] / CS) + floor(p[1] / CS) * self.cols

    def get_neighbors(self, idx: int) -> list[list[float]]:
        ret = []

        top = idx >= self.cols
        bottom = idx < (self.rows * self.cols - self.cols)
        left = (idx % self.cols) != 0
        right = (idx % self.cols) != (self.cols - 1)

        if top and left and self.grid[idx - 1 - self.cols] is not None:
            ret.append(self.grid[idx - 1 - self.cols])
        if top and right and self.grid[idx + 1 - self.cols] is not None:
            ret.append(self.grid[idx + 1 - self.cols])
        if bottom and left and self.grid[idx - 1 + self.cols] is not None:
            ret.append(self.grid[idx - 1 + self.cols])
        if bottom and right and self.grid[idx + 1 + self.cols] is not None:
            ret.append(self.grid[idx + 1 + self.cols])
        if top and self.grid[idx - self.cols] is not None:
            ret.append(self.grid[idx - self.cols])
        if left and self.grid[idx - 1] is not None:
            ret.append(self.grid[idx - 1])
        if bottom and self.grid[idx + self.cols] is not None:
            ret.append(self.grid[idx + self.cols])
        if right and self.grid[idx + 1] is not None:
            ret.append(self.grid[idx + 1])

        return ret  # type: ignore

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/poisson_disk_sampling.jpg")


if __name__ == "__main__":
    sketch = C033_PoissonDiskSampling()
    sketch.run_sketch()
