import os
from py5 import Sketch
from population import Population
from obstacle import Obstacle


class C029_SmartRockets(Sketch):
    p: Population
    target: list[float] = [0.0, 20.0]
    lifetime: int = 0

    def settings(self):
        self.size(600, 400)

    def setup(self):
        self.p = Population(25, self.height)
        self.p.obstacles.append(Obstacle(-100, 150, 160, 20))
        self.p.obstacles.append(Obstacle(100, 150, 160, 20))
        self.target = [0, 20]

    def draw(self):
        if self.lifetime == self.p.lifespan:
            self.p.generate()
            self.lifetime = 0
        self.lifetime += 1

        self.translate(self.width / 2, 0)
        self.background(20)
        self.p.run(self.target, self)

        self.fill(0, 0, 255)
        self.stroke_weight(1)
        self.ellipse(self.target[0], self.target[1], 10, 10)

        self.fill(255)
        self.text_size(14)
        self.text(str(self.lifetime), -self.width / 2 + 20, 20)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/smart_rockets.jpg")


if __name__ == "__main__":
    sketch = C029_SmartRockets()
    sketch.run_sketch()
