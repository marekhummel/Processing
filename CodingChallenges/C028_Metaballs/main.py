import os
from py5 import Sketch
from metaball import Metaball


SCL = 5


class C028_Metaballs(Sketch):
    blobs: list[Metaball] = []

    def settings(self):
        self.size(640, 480)

    def setup(self):
        self.color_mode(self.HSB)
        self.blobs = []
        for i in range(3):
            self.blobs.append(Metaball(self.width, self.height))

    def draw(self):
        for b in self.blobs:
            b.move()

        self.load_pixels()
        for x in range(self.width):
            for y in range(self.height):
                val = 0.0
                for b in self.blobs:
                    val += b.func(x, y) * b.radius

                index = y * self.width + x
                self.pixels[index] = self.color(val * SCL, 255, 255)
        self.update_pixels()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/metaballs.jpg")


if __name__ == "__main__":
    sketch = C028_Metaballs()
    sketch.run_sketch()
