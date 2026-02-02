import os
from math import radians, pow
from py5 import Sketch
from lsystem import LSystem


ANGLE = radians(25)


class C016_LSystem(Sketch):
    ls: LSystem
    angle: float = ANGLE

    def settings(self):
        self.size(500, 500)

    def setup(self):
        r = {"f": "ff+[+f-f-f]-[-f+f+f]"}
        self.ls = LSystem("f", r)

        self.frame_rate(2)

    def draw(self):
        self.background(0)

        self.translate(self.width / 2, self.height)
        self.stroke(255, 100)
        length = 150 * pow(0.5, self.ls.n)

        for i in range(len(self.ls.current_state)):
            c = self.ls.current_state[i]
            if c == "f":
                self.line(0, 0, 0, -length)
                self.translate(0, -length)
            elif c == "+":
                self.rotate(self.angle)
            elif c == "-":
                self.rotate(-self.angle)
            elif c == "[":
                self.push_matrix()
            elif c == "]":
                self.pop_matrix()

        self.ls.produce()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/lsystem.jpg")


if __name__ == "__main__":
    sketch = C016_LSystem()
    sketch.run_sketch()
