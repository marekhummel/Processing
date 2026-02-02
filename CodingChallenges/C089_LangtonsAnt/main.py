import os
from py5 import Sketch


RULE = "LRRRRRLLR"
SPEED = 100


class C089_LangtonsAnt(Sketch):
    ax: int = 0
    ay: int = 0
    ar: int = 0  # 0 1 2 3, up right down left
    grid: list[list[int]] = []

    def settings(self):
        self.size(600, 400)

    def setup(self):
        self.grid = [[0 for y in range(self.height)] for x in range(self.width)]
        self.ax = self.width // 2
        self.ay = self.height // 2

        self.background(245)
        self.color_mode(self.HSB, 255, 255, 255)

    def draw(self):
        self.load_pixels()
        for n in range(SPEED):
            self.grid[self.ax][self.ay] = (self.grid[self.ax][self.ay] + 1) % len(RULE)
            pix = self.ay * self.width + self.ax

            h = int(255 * self.grid[self.ax][self.ay] / len(RULE))
            self.pixels[pix] = self.color(h, 255, 255)

            # Move ant
            letter = RULE[self.grid[self.ax][self.ay]]
            if letter == "L":
                self.ar -= 1
            elif letter == "R":
                self.ar += 1
            elif letter == "U":
                self.ar += 2
            if self.ar < 0:
                self.ar += 4
            if self.ar > 3:
                self.ar -= 4

            if self.ar == 0:
                self.ay -= 1
            elif self.ar == 1:
                self.ax += 1
            elif self.ar == 2:
                self.ay += 1
            elif self.ar == 3:
                self.ax -= 1

        self.update_pixels()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/langtons_ant.jpg")


if __name__ == "__main__":
    sketch = C089_LangtonsAnt()
    sketch.run_sketch()
