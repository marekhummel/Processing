import os
from py5 import Sketch
from firework import Firework

try:
    from peasy import PeasyCam  # type: ignore
except ImportError:
    import py5_tools

    py5_tools.processing.download_library("PeasyCam")
    from peasy import PeasyCam  # type: ignore


class C027_Fireworks3D(Sketch):
    cam: PeasyCam
    fireworks: list[Firework] = []

    def settings(self):
        self.size(600, 400, self.P3D)

    def setup(self):
        self.cam = PeasyCam(self, 500)
        self.color_mode(self.HSB, 360, 100, 100, 100)
        self.fireworks = []

    def draw(self):
        self.background(10)
        if self.frame_count % 40 == 0:
            self.fireworks.append(Firework(self.width, self.height))

        for i in range(len(self.fireworks) - 1, -1, -1):
            self.fireworks[i].update()
            self.fireworks[i].display(self)

            if self.fireworks[i].gone:
                self.fireworks.pop(i)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/fireworks_3d.jpg")


if __name__ == "__main__":
    sketch = C027_Fireworks3D()
    sketch.run_sketch()
