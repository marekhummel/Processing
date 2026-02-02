from random import random, uniform
from py5 import Sketch
from crown_area import CrownArea


class AttractionPoint:
    pos: list[float]
    reached: bool = False

    def __init__(
        self, x: float | None = None, y: float | None = None, width: int = 400, height: int = 600
    ):
        if x is not None and y is not None:
            self.pos = [x, y]
        else:
            scx = 0.0
            scy = 0.0
            while True:
                scx = uniform(-1, 1)
                scy = random()
                if CrownArea.in_area(scx, scy, 0.1 * uniform(-1, 1)):
                    break

            x = scx * (width / 2)
            y = scy * (-height)
            self.pos = [x, y]

    def display(self, sketch: Sketch):
        if self.reached:
            return

        sketch.no_stroke()
        sketch.fill(20)
        sketch.ellipse(self.pos[0], self.pos[1], 2, 2)
