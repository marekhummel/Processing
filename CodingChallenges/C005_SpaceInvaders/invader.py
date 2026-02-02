class Invader:
    x: float
    y: float
    r: float
    dead: bool = False

    def __init__(self, x_: float, y_: float, _r: float):
        self.x = x_
        self.y = y_
        self.r = _r
        self.dead = False

    def move(self, xoff: float, yoff: float):
        self.x += xoff
        self.y += yoff

    def display(self, sketch):
        if self.dead:
            return

        sketch.stroke(0, 220, 0)
        sketch.fill(0, 200, 0)
        sketch.ellipse(self.x, self.y, self.r, self.r)
