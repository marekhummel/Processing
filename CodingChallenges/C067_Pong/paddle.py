class Paddle:
    x: int
    y: int
    width: int = 10
    height: int = 70

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 70

    def draw(self, sketch):
        sketch.no_stroke()
        sketch.fill(255)
        sketch.rect(self.x, self.y, self.width, self.height)
