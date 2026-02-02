class Bullet:
    x: float
    y: float
    w: float
    h: float

    def __init__(self, x_: float, height: int):
        self.x = x_
        self.y = height - 30
        self.w = 10
        self.h = 20

    def update(self):
        self.y -= 20

    def display(self, sketch):
        sketch.no_stroke()
        sketch.fill(0)
        sketch.rect_mode(sketch.CENTER)
        sketch.rect(self.x, self.y, self.w, self.h, 5, 5, 0, 0)
