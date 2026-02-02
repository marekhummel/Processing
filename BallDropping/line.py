from math import sqrt, pow


class Line:
    start: list[float]
    end: list[float]

    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.start = [x1, y1]
        self.end = [x2, y2]

    def dir(self) -> list[float]:
        return [self.end[0] - self.start[0], self.end[1] - self.start[1]]

    def touches_ball(self, b) -> bool:
        dir1 = sqrt(pow(b.pos[0] - self.start[0], 2) + pow(b.pos[1] - self.start[1], 2))
        dir2 = sqrt(pow(b.pos[0] - self.end[0], 2) + pow(b.pos[1] - self.end[1], 2))
        dir_vec = self.dir()
        dir_mag = sqrt(dir_vec[0] ** 2 + dir_vec[1] ** 2)
        return (dir1 + dir2) < sqrt(pow(dir_mag, 2) + pow(b.r / 2, 2))

    def display(self, sketch):
        sketch.stroke(255)
        sketch.no_fill()
        sketch.line(self.start[0], self.start[1], self.end[0], self.end[1])
