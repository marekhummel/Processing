from math import pow, atan2
from py5 import Sketch
from dna import DNA
from obstacle import Obstacle


class Individual:
    dna: DNA
    fitness: float = 0.0
    succeeded: bool = False
    dead: bool = False
    pos: list[float]
    vel: list[float]

    def __init__(self, d: DNA, height: int):
        self.pos = [0.0, height - 20.0]
        self.vel = [0.0, 0.0]
        self.dna = d

    def crossover(self, o: "Individual", height: int) -> "Individual":
        newdna = self.dna.crossover(o.dna)
        return Individual(newdna, height)

    def update(self, target: list[float], obs: list[Obstacle], width: int, height: int):
        if self.succeeded or self.dead:
            return

        self.dna.lifespan -= 1

        # Set magnitude to 10
        mag = (self.vel[0] ** 2 + self.vel[1] ** 2) ** 0.5
        if mag > 0:
            self.vel[0] = (self.vel[0] / mag) * 10
            self.vel[1] = (self.vel[1] / mag) * 10

        # Add gene
        self.vel[0] += self.dna.genes[self.dna.lifespan][0]
        self.vel[1] += self.dna.genes[self.dna.lifespan][1]

        # Limit to 3
        mag = (self.vel[0] ** 2 + self.vel[1] ** 2) ** 0.5
        if mag > 3:
            self.vel[0] = (self.vel[0] / mag) * 3
            self.vel[1] = (self.vel[1] / mag) * 3

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        dx = target[0] - self.pos[0]
        dy = target[1] - self.pos[1]
        dist = (dx**2 + dy**2) ** 0.5
        self.fitness = pow(0.99, dist)

        if (
            self.pos[0] < -width / 2
            or self.pos[0] > width / 2
            or self.pos[1] < 0
            or self.pos[1] > height
        ):
            self.dead = True
            self.fitness *= 0.1
            return

        for o in obs:
            if o.hit(self.pos):
                self.dead = True
                self.fitness *= 0.1
                return

        if dist < 10:
            self.succeeded = True
            self.fitness *= 10
            return

    def display(self, sketch: Sketch):
        sketch.push_matrix()
        sketch.translate(self.pos[0], self.pos[1])
        heading = atan2(self.vel[1], self.vel[0])
        sketch.rotate(heading - sketch.HALF_PI)
        sketch.stroke_weight(1)
        sketch.stroke(255, 100)
        sketch.fill(200, 100)
        sketch.rect_mode(sketch.CENTER)
        sketch.rect(0, 0, 10, 20)
        sketch.pop_matrix()
