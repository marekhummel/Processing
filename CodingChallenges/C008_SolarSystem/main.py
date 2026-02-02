import os
from py5 import Sketch
from planet import Planet

try:
    from peasy import PeasyCam  # type: ignore
except ImportError:
    import py5_tools

    py5_tools.processing.download_library("PeasyCam")
    from peasy import PeasyCam  # type: ignore


class C008_SolarSystem(Sketch):
    sun: Planet

    def settings(self):
        self.size(500, 500, self.P3D)

    def setup(self):
        PeasyCam(self, 500)
        self.sun = Planet(0, 60, 0)

    def draw(self):
        # Update
        self.sun.update()

        # Draw
        self.background(0)
        self.lights()

        self.sun.display(self)
        self.point_light(255, 255, 255, 0, 0, 0)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/solar_system.jpg")


if __name__ == "__main__":
    sketch = C008_SolarSystem()
    sketch.run_sketch()
