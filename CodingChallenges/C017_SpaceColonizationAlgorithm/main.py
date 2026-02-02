import os
from py5 import Sketch
from tree import Tree
from crown_area import CrownArea


N = 2000  # Amount of APs
D = 10  # Branch len
DK = 1 * D  # Kill dis
DI = 200  # Attraction dis


class C017_SpaceColonizationAlgorithm(Sketch):
    t: Tree
    growing: bool = False

    def settings(self):
        self.size(400, 600)

    def setup(self):
        self.t = Tree(DK, DI, D)
        self.t.gen_aps(N, self.width, self.height)

    def draw(self):
        self.background(255)
        self.translate(self.width / 2, self.height)
        self.t.display(self)
        if self.growing:
            self.t.grow()

        # Status
        self.stroke(0)
        if self.t.fully_grown:
            self.fill(255, 180, 0)
        elif self.growing:
            self.fill(0, 255, 0)
        else:
            self.fill(255, 0, 0)
        self.rect(-self.width / 2 - 1, -15, 15, 15)

        # Show crown
        self.stroke(255, 0, 0)
        scy = CrownArea.MIN_HEIGHT
        while scy <= 1:
            x = (CrownArea.max_dis(scy) + 1) / 2 * self.width - self.width / 2
            y = scy * (-self.height)
            px = (CrownArea.max_dis(scy - 0.02) + 1) / 2 * self.width - self.width / 2
            py = (scy - 0.02) * (-self.height)
            self.line(x, y, px, py)
            self.line(-x, y, -px, py)
            scy += 0.02

        if self.t.fully_grown:
            self.no_loop()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/space_colonization.jpg")
        else:
            self.growing = not self.growing


if __name__ == "__main__":
    sketch = C017_SpaceColonizationAlgorithm()
    sketch.run_sketch()
