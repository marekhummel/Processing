from random import randint


class Symbol:
    i: int
    j: int
    value: str

    def __init__(self, i_: int, j_: int):
        self.i = i_
        self.j = j_
        charval = 0x30A0 + randint(0, 95)
        self.value = chr(charval)

    def change(self):
        charval = 0x30A0 + randint(0, 95)
        self.value = chr(charval)

    def display(self, size: float, alpha: float, hl: bool, sketch):
        if hl:
            sketch.fill(230, 255, 230, alpha * 255)
        else:
            sketch.fill(0, 255, 70, alpha * 255)
        sketch.text_size(size)
        sketch.text(self.value, self.i * size, self.j * size)
        sketch.text_size(size + 2)
        sketch.fill(200, 100)
        sketch.text(self.value, self.i * size - 1, self.j * size - 1)
