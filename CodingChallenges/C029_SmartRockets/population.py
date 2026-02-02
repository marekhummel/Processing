from math import floor
from random import random
from py5 import Sketch
from individual import Individual
from dna import DNA
from obstacle import Obstacle


LIFESPAN = 200


class Population:
    size: int
    creatures: list[Individual]
    obstacles: list[Obstacle]
    lifespan: int = LIFESPAN

    def __init__(self, s: int, height: int):
        self.size = s
        self.creatures = []
        for i in range(s):
            self.creatures.append(Individual(DNA(self.lifespan), height))
        self.obstacles = []
        self._height = height

    def generate(self):
        pool = []
        for c in self.creatures:
            for i in range(int(c.fitness * 100)):
                pool.append(c)

        newcreatures = []
        for i in range(self.size):
            a = pool[floor(random() * len(pool))]
            b = pool[floor(random() * len(pool))]
            newcreatures.append(a.crossover(b, self._height))

        self.creatures = newcreatures

    def run(self, target: list[float], sketch: Sketch):
        for i in self.creatures:
            i.update(target, self.obstacles, sketch.width, sketch.height)
            i.display(sketch)
        for o in self.obstacles:
            o.display(sketch)
