class BaseCircle:
    x: float
    y: float
    size: float
    speed: float
    color: int
    is_x: bool
    angle: float = 0.0

    def __init__(self, x: float, y: float, sz: float, spd: float, col: int, is_x: bool):
        self.x = x
        self.y = y
        self.size = sz
        self.speed = spd
        self.color = col
        self.is_x = is_x
        self.angle = 0

    def update(self, sketch):
        # Rotate the point by increasing the angle
        self.angle = (self.angle - self.speed) % sketch.TWO_PI

    def dot_pos(self, sketch) -> tuple[float, float]:
        # Return polar coordinates from angle
        return (sketch.sin(self.angle + sketch.PI), sketch.cos(self.angle + sketch.PI))

    def draw(self, sketch):
        # Transformation, so that the circles center is the origin and its radius is 1
        sketch.push_matrix()
        sketch.translate(self.x, self.y)
        sketch.scale(self.size / 2)
        sketch.stroke(self.color >> 16, self.color >> 8 & 0xFF, self.color & 0xFF)
        sketch.stroke_weight(1 / self.size * 3)

        # Circle
        sketch.no_fill()
        sketch.ellipse(0, 0, 2, 2)

        # Dot
        sketch.fill(255)
        dot_x, dot_y = self.dot_pos(sketch)
        sketch.ellipse(dot_x, dot_y, 0.15, 0.15)
        sketch.pop_matrix()

        # Line
        sketch.stroke_weight(0.5)
        sketch.stroke(0xDD, 0xDD, 0xDD)
        if self.is_x:
            x = self.x + self.dot_pos(sketch)[0] * self.size / 2
            sketch.line(x, -self.size, x, sketch.height)
        else:
            y = self.y + self.dot_pos(sketch)[1] * self.size / 2
            sketch.line(-self.size, y, sketch.width, y)
