import os
from random import random
from py5 import Sketch
from cell import Cell


WIDTH = 20
HEIGHT = 10
BOMBRATE = 0.13
SQSIZE = 40
MARGIN = 10
TEXT_COLS = [
    (29, 73, 145),
    (5, 127, 58),
    (206, 18, 8),
    (96, 3, 93),
    (128, 0, 0),
    (66, 215, 244),
    (25, 0, 24),
    (132, 132, 132),
]


class C071_Minesweeper(Sketch):
    cells: list[list[Cell]] = []
    bombcount: int = 0
    gamestate: int = 0  # 0 = running, -1 = lost; 1 = won

    def settings(self):
        self.size(WIDTH * SQSIZE + 2 * MARGIN, HEIGHT * SQSIZE + 2 * MARGIN)

    def setup(self):
        self.text_align(self.CENTER, self.CENTER)
        self.text_font(self.create_font("Ubuntu Regular", 0.8 * SQSIZE))

        self.cells = []
        for xi in range(WIDTH):
            col = []
            for yi in range(HEIGHT):
                c = Cell()
                if random() < BOMBRATE:
                    c.value = -1
                    self.bombcount += 1
                col.append(c)
            self.cells.append(col)

        for xi in range(WIDTH):
            for yi in range(HEIGHT):
                self.count_bomb_neighbors(xi, yi)

    def draw(self):
        self.background(51)
        self.text_size(0.8 * SQSIZE)
        for xi in range(WIDTH):
            for yi in range(HEIGHT):
                self.draw_cell(xi, yi)

        self.check_game_state()
        if self.gamestate != 0:
            self.text_size(0.8 * SQSIZE)
            for xi in range(WIDTH):
                for yi in range(HEIGHT):
                    self.cells[xi][yi].visible = True
                    self.draw_cell(xi, yi)

            self.fill(255, 255, 255, 180)
            self.rect(0, 0, self.width, self.height)
            self.text_size(95)
            if self.gamestate == 1:
                self.fill(0, 221, 0)
                self.text("WON!", 0.5 * self.width, 0.45 * self.height)
            else:
                self.fill(176, 0, 0)
                self.text("LOST!", 0.5 * self.width, 0.45 * self.height)
            self.no_loop()

    def mouse_pressed(self):
        if self.gamestate != 0:
            return

        xi = int((self.mouse_x - MARGIN) / SQSIZE)
        yi = int((self.mouse_y - MARGIN) / SQSIZE)
        if xi < 0 or xi >= WIDTH or yi < 0 or yi >= HEIGHT:
            return

        if self.mouse_button == self.LEFT:
            self.reveal(xi, yi)
        elif self.mouse_button == self.RIGHT:
            self.cells[xi][yi].flagged = not self.cells[xi][yi].flagged

    def check_game_state(self):
        hiddencount = 0
        correct_flags = 0
        for xi in range(WIDTH):
            for yi in range(HEIGHT):
                if self.cells[xi][yi].visible and self.cells[xi][yi].value == -1:
                    self.gamestate = -1
                    return

                if not self.cells[xi][yi].visible:
                    hiddencount += 1

                if self.cells[xi][yi].flagged and self.cells[xi][yi].value == -1:
                    correct_flags += 1

        if hiddencount == self.bombcount and correct_flags == self.bombcount:
            self.gamestate = 1

    def reveal(self, xi: int, yi: int):
        c = self.cells[xi][yi]
        if c.flagged or c.visible:
            return

        c.visible = True
        if c.value != 0:
            return

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nxi = xi + dx
                nyi = yi + dy
                if nxi >= 0 and nxi < WIDTH and nyi >= 0 and nyi < HEIGHT:
                    self.reveal(nxi, nyi)

    def draw_cell(self, xi: int, yi: int):
        x = xi * SQSIZE + MARGIN
        y = yi * SQSIZE + MARGIN
        c = self.cells[xi][yi]

        if c.visible:
            self.fill(221)
        else:
            self.fill(136)

        self.rect(x, y, SQSIZE, SQSIZE)

        if c.flagged:
            self.fill(255, 0, 0)
            self.text("F", x + SQSIZE / 2, y + SQSIZE / 2)
        elif c.visible:
            if c.value == -1:
                self.fill(0)
                self.text("B", x + SQSIZE / 2, y + SQSIZE / 2)
            elif c.value > 0:
                self.fill(*TEXT_COLS[c.value - 1])
                self.text(str(c.value), x + SQSIZE / 2, y + SQSIZE / 2)

    def count_bomb_neighbors(self, xi: int, yi: int):
        if self.cells[xi][yi].value == -1:
            return

        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nxi = xi + dx
                nyi = yi + dy
                if nxi >= 0 and nxi < WIDTH and nyi >= 0 and nyi < HEIGHT:
                    if self.cells[nxi][nyi].value == -1:
                        count += 1

        self.cells[xi][yi].value = count

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/minesweeper.jpg")


if __name__ == "__main__":
    sketch = C071_Minesweeper()
    sketch.run_sketch()
