class Bird:
    y: float = 0.0
    vel: float = 0.0
    acc: float = 0.0
    r: float = 12.0
    dead: bool = False

    def apply_force(self, a: float):
        self.acc += a

    def update(self, height: int):
        self.y += self.vel
        self.vel += self.acc
        self.vel = max(-4, min(self.vel, 6))
        self.acc = 0

        if self.y > height / 2 or self.y < -height / 2:
            self.dead = True

    def display(self, sketch):
        sketch.stroke_weight(1)
        sketch.stroke(0)
        sketch.fill(240, 240, 60)
        sketch.ellipse(0, self.y, 2 * self.r, 2 * self.r)
