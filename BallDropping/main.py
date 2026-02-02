import os
from py5 import Sketch
from ball import Ball
from line import Line


class BallDropping(Sketch):
    _balls: list[Ball] = []
    _lines: list[Line] = []
    _gravity: list[float] = [0.0, 0.03]
    _spawn: list[float] = [10.0, 200.0]
    _tickcount: int = 0
    _start: list[float] | None = None

    def settings(self):
        self.size(600, 400)

    def setup(self):
        self.frame_rate(180)

    def draw(self):
        self._tickcount += 1

        if self._tickcount % 120 == 0:
            self._balls.append(Ball(self._spawn[0], self._spawn[1]))

        self.background(0)

        self.stroke(255)
        self.no_fill()
        self.ellipse(self._spawn[0], self._spawn[1], 8, 8)

        for l in self._lines:
            for b in self._balls:
                if b.bounce_cooldown == 0 and l.touches_ball(b):
                    # Split vel in two vectors (parallel to line and orthogonal to line)
                    par = l.dir()
                    dot_vel_par = b.vel[0] * par[0] + b.vel[1] * par[1]
                    dot_par_par = par[0] * par[0] + par[1] * par[1]
                    scl = dot_vel_par / dot_par_par

                    par_scaled = [par[0] * scl, par[1] * scl]
                    orth = [b.vel[0] - par_scaled[0], b.vel[1] - par_scaled[1]]

                    # Set new vel (by inverting the orthogonal one)
                    b.vel = [par_scaled[0] + orth[0] * -0.9, par_scaled[1] + orth[1] * -0.9]
                    b.bounce_cooldown = 10

            l.display(self)

        for b in self._balls:
            b.apply_force(self._gravity)
            b.update()
            b.display(self)

        if self._start is not None:
            self.no_stroke()
            self.fill(255)
            self.rect(self._start[0] - 2, self._start[1] - 2, 4, 4)

    def mouse_clicked(self):
        if self.mouse_button == self.RIGHT:
            self._spawn = [float(self.mouse_x), float(self.mouse_y)]
        elif self._start is not None:
            self._lines.append(
                Line(self._start[0], self._start[1], float(self.mouse_x), float(self.mouse_y))
            )
            self._start = None
        else:
            self._start = [float(self.mouse_x), float(self.mouse_y)]

    def key_typed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/ball_dropping.jpg")


if __name__ == "__main__":
    sketch = BallDropping()
    sketch.run_sketch()
