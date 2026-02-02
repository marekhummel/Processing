class Ball:
    pos: list[float]
    vel: list[float]
    acc: list[float]
    r: float = 7.0
    bounce_cooldown: int = 0
    tempr: float = 0.0

    def __init__(self, x: float, y: float):
        self.pos = [x, y]
        self.vel = [0.0, 0.0]
        self.acc = [0.0, 0.0]
        self.tempr = self.r

    def apply_force(self, force: list[float]):
        self.acc[0] += force[0]
        self.acc[1] += force[1]

    def update(self):
        if self.bounce_cooldown > 0:
            self.bounce_cooldown -= 1

        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.acc[0] = 0
        self.acc[1] = 0

    def display(self, sketch):
        if self.tempr != self.r:
            self.tempr += 1

        sketch.no_stroke()
        sketch.fill(255)
        sketch.ellipse(self.pos[0], self.pos[1], self.tempr, self.tempr)
