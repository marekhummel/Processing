import os
from py5 import Sketch
from tree import Tree

try:
    from peasy import PeasyCam  # type: ignore
except ImportError:
    import py5_tools

    py5_tools.processing.download_library("PeasyCam")
    from peasy import PeasyCam  # type: ignore

N = 100  # Amount of APs
D = 5  # Branch len
DK = 2 * D  # Kill dis
DI = 10000  # Attraction dis


class C018_SpaceColonizationAlgorithm3D(Sketch):
    t: Tree
    growing: bool = False
    cam: PeasyCam

    def settings(self):
        self.size(400, 600, self.P3D)

    def setup(self):
        self.t = Tree(DK, DI, D)
        self.t.gen_aps(N, self.width, self.height)
        self.cam = PeasyCam(self, 0, -100, 0, 300)

    def draw(self):
        self.background(255)
        self.t.display(self)
        if self.growing:
            self.t.grow()

        if self.t.fully_grown:
            self.t.display(self)
            self.no_loop()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/space_colonization_3d.jpg")
        else:
            self.growing = not self.growing


if __name__ == "__main__":
    sketch = C018_SpaceColonizationAlgorithm3D()
    sketch.run_sketch()
