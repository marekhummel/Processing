from random import random as rand


class Star:
    x: float
    y: float
    z: float
    sx: float
    sy: float
    px: float
    py: float
    speed: float = 5.0

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = rand() * width - width / 2
        self.y = rand() * height - height / 2
        self.z = rand() * (width / 2)

        self.sx = self.remap(self.x / self.z, 0, 1, 0, width / 2)
        self.sy = self.remap(self.y / self.z, 0, 1, 0, height / 2)
        self.px = self.sx
        self.py = self.sy

    def remap(
        self, value: float, start1: float, stop1: float, start2: float, stop2: float
    ) -> float:
        return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

    def update(self):
        self.z = self.z - self.speed

        self.px = self.sx
        self.py = self.sy
        self.sx = self.remap(self.x / self.z, 0, 1, 0, self.width / 2)
        self.sy = self.remap(self.y / self.z, 0, 1, 0, self.height / 2)

        if (
            self.sx < -self.width / 2
            or self.sx > self.width / 2
            or self.sy < -self.height / 2
            or self.sy > self.height / 2
        ):
            self.z = rand() * (self.width / 2)
            self.sx = self.remap(self.x / self.z, 0, 1, 0, self.width / 2)
            self.sy = self.remap(self.y / self.z, 0, 1, 0, self.height / 2)
            self.px = self.sx
            self.py = self.sy

    def show(self, sketch):
        sketch.no_stroke()
        sketch.fill(255)

        r = sketch.remap(self.z, self.width / 2, 1, 0, 3)
        sketch.ellipse(self.sx, self.sy, r, r)

        sketch.stroke(255)
        sketch.line(self.px, self.py, self.sx, self.sy)
