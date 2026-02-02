import os
from math import pi
from py5 import Sketch
from tree import Tree


class CollatzConjecture(Sketch):
    t: Tree

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.t = Tree(10000, 20)
        self.frame_rate(10)
        self.stroke(0)
        self.text_align(self.CENTER, self.CENTER)
        self.text_size(10)

    def draw(self):
        self.background(51)
        self.translate(3 * self.width / 4, self.height - 20)
        self.t.display(0, 0, pi, self)
        self.t.generate_next()

    def key_typed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/collatz_conjecture.jpg")


if __name__ == "__main__":
    sketch = CollatzConjecture()
    sketch.run_sketch()
