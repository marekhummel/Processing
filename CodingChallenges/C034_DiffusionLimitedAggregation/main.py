import os
from py5 import Sketch
from random_walker import RandomWalker


MAX_WALKERS = 100
ITER = 200
RAD = 4.0


class C034_DiffusionLimitedAggregation(Sketch):
    walkers: list[RandomWalker] = []
    seeds: list[list[float]] = []
    startingpoints: list[list[float]] = []

    def settings(self):
        self.size(400, 400)

    def setup(self):
        self.color_mode(self.HSB)
        self.no_stroke()

        self.set_starting_points()
        self.walkers = []
        for i in range(MAX_WALKERS):
            self.walkers.append(RandomWalker(self.startingpoints))
        self.set_seeds()

    def set_starting_points(self):
        self.startingpoints = []

        # 1
        x = 0.0
        while x < self.width:
            self.startingpoints.append([x, 0.0])
            self.startingpoints.append([x, float(self.height)])
            x += 0.5

        y = 0.0
        while y < self.height:
            self.startingpoints.append([0.0, y])
            self.startingpoints.append([float(self.width), y])
            y += 0.5

    def set_seeds(self):
        self.seeds = []

        # 1
        self.seeds.append([float(self.width / 2), float(self.height / 2)])

    def draw(self):
        self.background(51)

        for i in range(ITER):
            for wi in range(len(self.walkers) - 1, -1, -1):
                rw = self.walkers[wi]
                rw.move(self.width, self.height)
                if rw.stuck(self.seeds, RAD * 2):
                    self.seeds.append(rw.pos.copy())
                    self.walkers.pop(wi)

        while len(self.walkers) != MAX_WALKERS:
            self.walkers.append(RandomWalker(self.startingpoints))

        self.fill(255)

        c = 0.0
        for s in self.seeds:
            c += 0.3
            self.fill(c % 255, 255, 255)
            self.ellipse(s[0], s[1], 2 * RAD, 2 * RAD)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/diffusion_limited_aggregation.jpg")


if __name__ == "__main__":
    sketch = C034_DiffusionLimitedAggregation()
    sketch.run_sketch()
