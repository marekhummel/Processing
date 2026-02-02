import os
from math import floor, sqrt
from random import random
from time import sleep
from py5 import Sketch


OFFSET = 50


class C035_TravellingSalesmanProblem(Sketch):
    cities: list[list[float]] = []
    total: int = 0
    perm: list[int] = []
    best: list[int] = []
    bestdis: float = 10000000.0

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.cities = []
        for i in range(6):
            self.cities.append(
                [
                    random() * (self.width - 2 * OFFSET) + OFFSET,
                    random() * (self.height - 2 * OFFSET) + OFFSET,
                ]
            )

        self.perm = list(range(len(self.cities)))
        self.best = self.perm[:]
        self.total = self.fact(len(self.perm))

    def draw(self):
        self.background(51)

        # Best Path
        self.stroke(255, 0, 0, 80)
        self.stroke_weight(12)
        self.no_fill()
        self.begin_shape()
        for i in self.best:
            self.vertex(self.cities[i][0], self.cities[i][1])
        self.end_shape()

        # Path
        self.stroke(255)
        self.stroke_weight(3)
        self.no_fill()
        self.begin_shape()
        for i in self.perm:
            self.vertex(self.cities[i][0], self.cities[i][1])
        self.end_shape()

        # Cities
        self.stroke(255)
        self.stroke_weight(2)
        self.fill(0)
        for i in range(len(self.cities)):
            self.ellipse(self.cities[i][0], self.cities[i][1], 20, 20)

        # Update
        dis = 0.0
        for i in range(len(self.perm) - 1):
            dx = self.cities[self.perm[i]][0] - self.cities[self.perm[i + 1]][0]
            dy = self.cities[self.perm[i]][1] - self.cities[self.perm[i + 1]][1]
            dis += sqrt(dx * dx + dy * dy)

        if dis < self.bestdis:
            self.bestdis = dis
            self.best = self.perm[:]

        self.stroke(255)
        self.fill(255)
        self.text_size(15)
        self.text(self.p(self.perm) + "    " + str(int(dis)), 10, 20)
        self.text(self.p(self.best) + "    " + str(int(self.bestdis)), 10, 40)

        if self.frame_count == 1:
            sleep(1)
        elif self.frame_count == self.total:
            self.no_loop()
        else:
            self.next_perm()

    def next_perm(self):
        # https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
        x = 0
        y = 0
        for x in range(len(self.perm) - 2, -1, -1):
            if self.perm[x] < self.perm[x + 1]:
                break
        for y in range(len(self.perm) - 1, x, -1):
            if self.perm[x] < self.perm[y]:
                break

        temp = self.perm[y]
        self.perm[y] = self.perm[x]
        self.perm[x] = temp

        for i in range(x + 1, floor((len(self.perm) - x - 1) / 2) + x + 1):
            temp = self.perm[len(self.perm) - (i - x)]
            self.perm[len(self.perm) - (i - x)] = self.perm[i]
            self.perm[i] = temp

    def fact(self, num: int) -> int:
        return 1 if num == 1 else self.fact(num - 1) * num

    def p(self, a: list[int]) -> str:
        s = ""
        for i in a:
            s += str(i) + " | "
        return s[:-3]

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/travelling_salesman.jpg")


if __name__ == "__main__":
    sketch = C035_TravellingSalesmanProblem()
    sketch.run_sketch()
