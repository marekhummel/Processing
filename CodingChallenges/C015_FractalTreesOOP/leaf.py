from py5 import Sketch


class Leaf:
    x: float
    y: float

    def __init__(self, x_: float, y_: float):
        self.x = x_
        self.y = y_

    def display(self, sketch: Sketch):
        sketch.stroke_weight(1)
        sketch.fill(0, 255, 0, 200)
        sketch.ellipse(self.x, self.y, 10, 10)
