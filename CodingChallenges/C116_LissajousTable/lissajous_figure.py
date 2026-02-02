class LissajousCurve:
    x: float
    y: float
    size: float
    base: tuple
    color: int
    points: list[tuple[float, float]]

    def __init__(self, x: float, y: float, sz: float, base: tuple, sketch):
        self.x = x
        self.y = y
        self.size = sz
        self.base = base
        self.color = sketch.lerp_color(base[0].color, base[1].color, 0.5)

        self.points = [(self.base[0].dot_pos(sketch)[0], self.base[1].dot_pos(sketch)[1])]

    def update(self, finished: bool, sketch):
        # If calc is done, only rotate the point array, else add new point
        if finished:
            self.points = self.points[1:] + self.points[0:1]
        else:
            new = (self.base[0].dot_pos(sketch)[0], self.base[1].dot_pos(sketch)[1])
            self.points.append(new)

    def draw(self, sketch):
        # Transformation, so that the curves center (center of mass if u wish) is the origin and the size of the surrounding box is 2
        sketch.push_matrix()
        sketch.translate(self.x, self.y)
        sketch.scale(self.size / 2)
        sketch.stroke(self.color >> 16, self.color >> 8 & 0xFF, self.color & 0xFF)
        sketch.stroke_weight(1 / self.size * 2)

        # Figure
        sketch.no_fill()
        sketch.begin_shape()
        for pt in self.points:
            sketch.vertex(pt[0], pt[1])
        sketch.end_shape()

        # Dot
        sketch.fill(255)
        sketch.ellipse(self.points[-1][0], self.points[-1][1], 0.15, 0.15)
        sketch.pop_matrix()
