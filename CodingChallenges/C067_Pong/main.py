import os
from py5 import Sketch
from ball import Ball
from paddle import Paddle


class C067_Pong(Sketch):
    b: Ball
    pl: Paddle
    pr: Paddle
    scoreL: int = 0
    scoreR: int = 0

    def settings(self):
        self.size(400, 400)

    def setup(self):
        self.rect_mode(self.CENTER)
        self.b = Ball(self.width >> 1, self.height >> 1)
        self.pl = Paddle(int(0.05 * self.width), self.height >> 1)
        self.pr = Paddle(int(0.95 * self.width), self.height >> 1)

    def draw(self):
        # Update
        self.b.update()
        self.update_paddles()
        self.deflect_ball()
        self.score()

        # Draw
        self.background(51)
        self.b.draw(self)
        self.pl.draw(self)
        self.pr.draw(self)

        self.text_align(self.LEFT, self.TOP)
        self.text(str(self.scoreL), 0, 0)
        self.text_align(self.RIGHT, self.TOP)
        self.text(str(self.scoreR), self.width, 0)

    def update_paddles(self):
        if self.is_key_pressed:
            if self.key_code == self.UP:
                self.pl.y -= 1
            elif self.key_code == self.DOWN:
                self.pl.y += 1

    def deflect_ball(self):
        # Walls
        if self.b.y + self.b.r >= self.height or self.b.y - self.b.r <= 0:
            self.b.speedy *= -1

        # Paddles
        if self.b.x - self.b.r <= self.pl.x + (self.pl.width >> 1):
            if self.b.y <= self.pl.y + (self.pl.height >> 1) and self.b.y >= self.pl.y - (
                self.pl.height >> 1
            ):
                self.b.speedx *= -1
        elif self.b.x + self.b.r >= self.pr.x - (self.pr.width >> 1):
            if self.b.y <= self.pr.y + (self.pr.height >> 1) and self.b.y >= self.pr.y - (
                self.pr.height >> 1
            ):
                self.b.speedx *= -1

    def score(self):
        if self.b.x + self.b.r >= self.width:
            self.scoreL += 1
        if self.b.x - self.b.r <= 0:
            self.scoreR += 1

        if self.b.x + self.b.r >= self.width or self.b.x - self.b.r <= 0:
            self.b = Ball(self.width >> 1, self.height >> 1)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/pong.jpg")


if __name__ == "__main__":
    sketch = C067_Pong()
    sketch.run_sketch()
