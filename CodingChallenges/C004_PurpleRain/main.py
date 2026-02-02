import os
from py5 import Sketch
from rain_drop import RainDrop


class C004_PurpleRain(Sketch):
    _drops: list[RainDrop] = []

    def settings(self):
        self.size(600, 400)

    def setup(self):
        self._drops = []
        for i in range(500):
            self._drops.append(RainDrop(self.width, self.height))

        self.color_mode(self.HSB, 360, 100, 100)

    def draw(self):
        self.background(270, 15, 80)
        self.translate(self.width / 2, self.height / 2)

        for i in range(len(self._drops)):
            self._drops[i].display(self)
            self._drops[i].update()

            if self._drops[i].y > self.height / 2:
                self._drops[i] = RainDrop(self.width, self.height)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/purple_rain.jpg")


if __name__ == "__main__":
    sketch = C004_PurpleRain()
    sketch.run_sketch()
