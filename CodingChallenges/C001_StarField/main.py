import os
from py5 import Sketch
from star import Star


class C001_StarField(Sketch):
    _stars: list[Star] = []

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self._stars = []
        for i in range(800):
            self._stars.append(Star(self.width, self.height))

    def draw(self):
        self.background(0)
        self.translate(self.width / 2, self.height / 2)

        for s in self._stars:
            s.update()
            s.show(self)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/star_field.jpg")


if __name__ == "__main__":
    sketch = C001_StarField()
    sketch.run_sketch()
