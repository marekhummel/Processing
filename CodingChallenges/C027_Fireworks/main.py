import os
from py5 import Sketch
from firework import Firework


class C027_Fireworks(Sketch):
    fireworks: list[Firework] = []

    def settings(self):
        self.size(600, 400)

    def setup(self):
        self.color_mode(self.HSB, 360, 100, 100, 100)
        self.fireworks = []
        self.background(10)

    def draw(self):
        self.fill(10, 20)
        self.rect(0, 0, self.width, self.height)

        if self.frame_count % 20 == 0:
            self.fireworks.append(Firework(self.width, self.height))

        for i in range(len(self.fireworks) - 1, -1, -1):
            self.fireworks[i].update()
            self.fireworks[i].display(self)

            if self.fireworks[i].gone:
                self.fireworks.pop(i)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/fireworks.jpg")


if __name__ == "__main__":
    sketch = C027_Fireworks()
    sketch.run_sketch()
