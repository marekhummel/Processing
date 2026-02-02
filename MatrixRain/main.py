import os
from py5 import Sketch
from column import Column


SYMBOL_SIZE = 15


class MatrixRain(Sketch):
    cols: int = 0
    rows: int = 0
    columns: list[Column] = []

    def settings(self):
        self.size(600, 450)
        self.full_screen()
        self.smooth()

    def setup(self):
        self.frame_rate(30)
        self.cols = int(self.width / SYMBOL_SIZE)
        self.rows = int(self.height / SYMBOL_SIZE)

        self.columns = []
        for c in range(self.cols):
            self.columns.append(Column(c, self.rows))

        # Might require `$ sudo apt install fonts-noto-cjk`
        self.text_font(self.create_font("Noto Sans Mono CJK JP", SYMBOL_SIZE, False))

    def draw(self):
        self.background(0)
        for c in self.columns:
            c.display(SYMBOL_SIZE, self)

        for c in self.columns:
            if self.frame_count % 2 == 0:
                c.move()
            if self.frame_count % 5 == 0:
                c.change()

    def mouse_pressed(self):
        self.save(os.path.dirname(__file__) + "/matrix_rain.jpg")


if __name__ == "__main__":
    sketch = MatrixRain()
    sketch.run_sketch()
