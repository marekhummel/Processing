from random import random, randint
from symbol import Symbol


class Column:
    symbols: list[Symbol]
    index: int
    tip: int
    len: int
    totalrows: int
    showtip: bool

    def __init__(self, i: int, rows: int):
        self.index = i
        self.totalrows = rows
        self.showtip = randint(0, 3) == 0

        self.symbols = []
        for r in range(rows + 1):
            self.symbols.append(Symbol(i, r))

        self.reset(True)

    def reset(self, init: bool):
        self.tip = randint(-self.totalrows, 0) if init else 1
        self.len = randint(10, self.totalrows - 8)

    def move(self):
        self.tip += 1
        if self.tip - self.len > self.totalrows:
            self.reset(False)

    def change(self):
        for s in self.symbols:
            if random() < 0.5:
                s.change()

    def display(self, size: float, sketch):
        for s in self.symbols:
            if s.j <= self.tip and s.j > self.tip - self.len:
                alpha = sketch.remap(self.tip - s.j, 0, self.len, 1, 0)
                s.display(size, alpha, self.showtip and s.j == self.tip, sketch)
