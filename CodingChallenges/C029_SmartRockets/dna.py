from random import random


class DNA:
    genes: list[list[float]]
    ols: int
    lifespan: int

    def __init__(self, ls: int, g: list[list[float]] | None = None):
        self.ols = ls
        self.lifespan = ls
        self.genes = []
        if g is None:
            for i in range(ls):
                mag = 2.0
                self.genes.append([mag * random(), mag * random()])
        else:
            for i in range(ls):
                self.genes.append(g[i][:])

    def crossover(self, other: "DNA") -> "DNA":
        g = []
        for i in range(self.ols):
            if random() < 0.5:
                g.append(self.genes[i][:])
            else:
                g.append(other.genes[i][:])
            if random() < 0.01:
                mag = 2.0
                g[i] = [mag * random(), mag * random()]
        return DNA(self.ols, g)
