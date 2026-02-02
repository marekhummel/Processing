import os
from math import floor, cos, sin
from py5 import Sketch
from particle import Particle


SCL = 20


class C024_PerlinNoiseFlowField(Sketch):
    particles: list[Particle] = []
    zoff: float = 0.0

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.background(255)
        self.particles = []
        for i in range(500):
            self.particles.append(Particle(self.width, self.height))

    def draw(self):
        for i in range(self.width // SCL):
            for j in range(self.height // SCL):
                angle = self.noise(i * 0.1, j * 0.1, self.zoff) * self.TWO_PI * 2
                v = [cos(angle), sin(angle)]

                for p in self.particles:
                    if floor(p.pos[0] / SCL) == i and floor(p.pos[1] / SCL) == j:
                        p.add_dir(v, 0.3)

        for p in self.particles:
            p.update()
            p.display(self)

        self.zoff += 0.005

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/perlin_noise_flow_field.jpg")


if __name__ == "__main__":
    sketch = C024_PerlinNoiseFlowField()
    sketch.run_sketch()
