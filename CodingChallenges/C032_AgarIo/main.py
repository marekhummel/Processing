import os
from random import uniform
from py5 import Sketch
from cell import Cell


RES = 30


class C032_AgarIo(Sketch):
    me: Cell
    food: list[Cell] = []

    def settings(self):
        self.size(600, 600)

    def setup(self):
        self.color_mode(self.HSB)

        self.me = Cell(0, 0, 32, True)

        self.food = []
        for i in range(200):
            self.food.append(
                Cell(
                    uniform(-2 * self.width, 2 * self.width),
                    uniform(-2 * self.height, 2 * self.height),
                    8,
                    False,
                )
            )

    def draw(self):
        self.me.move(self.mouse_x, self.mouse_y, self.width, self.height)
        self.translate(self.width / 2, self.height / 2)
        self.translate(-self.me.pos[0], -self.me.pos[1])

        self.background(245)
        self.stroke(0)
        self.stroke_weight(4)
        self.no_fill()
        self.rect(-2 * self.width, -2 * self.height, 4 * self.width, 4 * self.height)

        self.stroke(0, 100)
        self.stroke_weight(1)
        ex = 5
        startx = self.me.pos[0] - self.width / 2 - self.me.pos[0] % RES - ex * RES
        starty = self.me.pos[1] - self.height / 2 - self.me.pos[1] % RES - ex * RES
        for i in range(int(self.width / RES + 2 * ex)):
            self.line(
                startx, starty + i * RES, startx + self.width + 2 * ex * RES, starty + i * RES
            )
            self.line(
                startx + i * RES, starty, startx + i * RES, starty + self.height + 2 * ex * RES
            )

        for i in range(len(self.food) - 1, -1, -1):
            f = self.food[i]
            if self.me.eat(f):
                self.food.pop(i)
                self.food.append(
                    Cell(
                        uniform(-2 * self.width, 2 * self.width),
                        uniform(-2 * self.height, 2 * self.height),
                        8,
                        False,
                    )
                )
                continue
            f.display(self)
        self.me.display(self)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/agar_io.jpg")


if __name__ == "__main__":
    sketch = C032_AgarIo()
    sketch.run_sketch()
