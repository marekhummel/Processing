from random import random, uniform
from py5 import Sketch
from crown_area import CrownArea


class AttractionPoint:
    pos: list[float]
    reached: bool = False

    def __init__(
        self,
        x: float | None = None,
        y: float | None = None,
        z: float | None = None,
        width: int = 400,
        height: int = 600,
    ):
        if x is not None and y is not None and z is not None:
            self.pos = [x, y, z]
        else:
            scx = 0.0
            scy = 0.0
            scz = 0.0
            while True:
                scx = uniform(-1, 1)
                scy = random()
                scz = uniform(-1, 1)
                if CrownArea.in_area(scx, scy, scz):
                    break

            x = scx * (width / 2)
            y = scy * (-height)
            z = scz * (width / 2)
            self.pos = [x, y, z]

    def display(self, sketch: Sketch):
        if self.reached:
            return

        sketch.no_stroke()
        sketch.fill(255, 0, 0, 100)

        sketch.push_matrix()
        sketch.translate(self.pos[0], self.pos[1], self.pos[2])
        sketch.sphere(1)
        sketch.pop_matrix()
