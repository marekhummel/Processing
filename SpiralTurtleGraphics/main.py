import os
from py5 import Sketch


class SpiralTurtleGraphics(Sketch):
    len: float = 400.0

    def settings(self):
        self.size(500, 500)

    def setup(self):
        self.translate(120, 450)
        self.push_matrix()

        self.background(0)
        self.stroke(255, 100)

    def draw(self):
        self.pop_matrix()
        self.line(0, 0, 0, -self.len)
        self.translate(0, -self.len)
        self.rotate(2 * self.PI / 3 * 1.005)
        self.push_matrix()

        self.len -= 1

        if self.len <= 0:
            self.no_loop()

    def key_typed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/spiral_turtle_graphics.jpg")


if __name__ == "__main__":
    sketch = SpiralTurtleGraphics()
    sketch.run_sketch()
