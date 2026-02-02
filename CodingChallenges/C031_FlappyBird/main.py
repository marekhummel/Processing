import os
from py5 import Sketch
from bird import Bird
from obstacle import Obstacle


GRAVITY = 0.2


class C031_FlappyBird(Sketch):
    b: Bird
    obs: list[Obstacle] = []
    score: int = 0

    def settings(self):
        self.size(400, 400)

    def setup(self):
        self.b = Bird()
        self.obs = []

    def draw(self):
        self.translate(30, self.height / 2)
        self.background(200, 255, 255)

        self.b.apply_force(GRAVITY)
        if self.is_key_pressed:
            self.b.apply_force(-5)
        self.b.update(self.height)
        self.b.display(self)

        if self.frame_count % 75 == 1:
            self.obs.append(Obstacle(self.width, self.height))

        for i in range(len(self.obs) - 1, -1, -1):
            o = self.obs[i]
            if o.x < -o.w:
                self.obs.pop(i)
                continue

            state = o.passed
            self.b.dead = self.b.dead or o.hit(self.b)
            if o.passed and not state:
                self.score += 1

            o.update()
            o.display(self.height, self)

        self.fill(0)
        self.text_size(20)
        self.text(str(self.score), 0, -self.height / 2 + 30)

        if self.b.dead:
            self.no_loop()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/flappy_bird.jpg")


if __name__ == "__main__":
    sketch = C031_FlappyBird()
    sketch.run_sketch()
