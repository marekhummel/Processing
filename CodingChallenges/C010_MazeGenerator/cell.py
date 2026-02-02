class Cell:
    i: int
    j: int
    visited: bool = False
    walls: list[bool]  # TOP RIGHT BOTTOM LEFT

    def __init__(self, i_: int, j_: int):
        self.i = i_
        self.j = j_
        self.visited = False
        self.walls = [True, True, True, True]

    def display(self, size: int, path: bool, tip: bool, sketch):
        x = self.i * size
        y = self.j * size

        sketch.no_stroke()

        if tip:
            sketch.fill(0, 255, 0)
        elif path:
            sketch.fill(0, 127, 0)
        else:
            sketch.fill(0)
        sketch.rect(x, y, size, size)

        sketch.stroke(200)
        sketch.no_fill()
        if self.walls[0]:
            sketch.line(x, y, x + size, y)
        if self.walls[1]:
            sketch.line(x + size, y, x + size, y + size)
        if self.walls[2]:
            sketch.line(x, y + size, x + size, y + size)
        if self.walls[3]:
            sketch.line(x, y, x, y + size)
