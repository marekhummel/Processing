import os
from math import sqrt, pow
from py5 import Sketch
from invader import Invader
from bullet import Bullet


class C005_SpaceInvaders(Sketch):
    _spaceship: list[float] = [0.0, 0.0]
    _invaders: list[Invader] = []
    _rows: int = 4
    _cols: int = 5
    _inv_size: float = 40.0
    _xoffset: float = 0.0
    _bullets: list[Bullet] = []
    _lastbullet: int = 0
    _keys: list[bool] = [False, False, False]
    _tickcount: int = 0

    def settings(self):
        self.size(500, 500)

    def setup(self):
        # Set spaceship
        self._spaceship = [self.width / 2, self.height - 15]

        # Create bullets
        self._bullets = []

        # Create invaders
        self._invaders = []
        margin = 2 * self._inv_size
        for j in range(self._rows):
            y = 50 + j * 0.5 * margin
            for i in range(self._cols):
                x = 50 + (0.5 * margin if j % 2 == 1 else 0) + i * margin
                self._invaders.append(Invader(x, y, self._inv_size))

        # Set x offset (move range per tick)
        self._xoffset = 20

        # Init keys
        self._keys = [False, False, False]

    def draw(self):
        self._tickcount += 1

        # Update invaders every 60th tick
        if self._tickcount % 60 == 0:
            next_left_x = self._invaders[0].x - self._inv_size / 2 + self._xoffset
            next_right_x = (
                self._invaders[2 * self._cols - 1].x + self._inv_size / 2 + self._xoffset
            )
            if next_left_x < 0 or next_right_x > self.width:
                for inv in self._invaders:
                    inv.move(0, 20)
                self._xoffset = -self._xoffset
            else:
                for inv in self._invaders:
                    inv.move(self._xoffset, 0)

        # Update bullet every second tick
        if self._tickcount % 2 == 0:
            for bul in self._bullets:
                bul.update()

        # Check collisions
        rm = [False] * len(self._bullets)

        for ib in range(len(self._bullets)):
            for i in self._invaders:
                if i.dead:
                    continue

                b = self._bullets[ib]
                d1 = self.dis(b.x - b.w / 2, b.y - b.h / 2, i.x, i.y)
                d2 = self.dis(b.x + b.w / 2, b.y - b.h / 2, i.x, i.y)

                if d1 < self._inv_size / 2 or d2 < self._inv_size / 2:
                    i.dead = True
                    rm[ib] = True

        for i in range(len(rm) - 1, -1, -1):
            if rm[i]:
                self._bullets.pop(i)

        # Update keyboard actions
        self.update_actions()

        # Display
        self.background(245)

        self.rect_mode(self.CENTER)
        self.no_stroke()
        self.fill(170, 0, 0)
        self.rect(self._spaceship[0], self._spaceship[1], 70, 30)

        for inv in self._invaders:
            inv.display(self)
        for bul in self._bullets:
            bul.display(self)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/space_invaders.jpg")
        if e.get_key_code() == self.LEFT:
            self._keys[0] = True
        if e.get_key_code() == self.RIGHT:
            self._keys[1] = True
        if e.get_key() == " ":
            self._keys[2] = True

    def key_released(self, e):
        if e.get_key_code() == self.LEFT:
            self._keys[0] = False
        if e.get_key_code() == self.RIGHT:
            self._keys[1] = False
        if e.get_key() == " ":
            self._keys[2] = False

    def update_actions(self):
        if self._keys[0]:
            self._spaceship[0] -= 7

        if self._keys[1]:
            self._spaceship[0] += 7

        if self._keys[2]:
            if self._tickcount - self._lastbullet < 20:
                return

            self._bullets.append(Bullet(self._spaceship[0], self.height))
            self._lastbullet = self._tickcount

    def dis(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


if __name__ == "__main__":
    sketch = C005_SpaceInvaders()
    sketch.run_sketch()
