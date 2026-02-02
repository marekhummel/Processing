import os
from random import randint
from py5 import Sketch


SQUARE_SIZE = 10


class C003_SnakeGame(Sketch):
    _snake: list[list[int]] = []
    _snakelength: int = 0
    _fruit: list[int] = [0, 0]
    _dir: int = 0  # UP RIGHT DOWN LEFT
    _dirchanged: bool = False
    _gamerunning: bool = True
    _maxindex: list[int] = [0, 0]

    def settings(self):
        self.size(600, 400)

    def setup(self):
        self.frame_rate(8)

        self._maxindex = [int(self.width / SQUARE_SIZE) - 1, int(self.height / SQUARE_SIZE) - 1]

        max_size = int((self._maxindex[0] + 1) * (self._maxindex[1] + 1))
        self._snake = [[-1, -1] for _ in range(max_size)]

        self._snake[0] = [int(self._maxindex[0] / 2), int(self._maxindex[1] / 2)]
        self._snake[1] = [int(self._maxindex[0] / 2) - 1, int(self._maxindex[1] / 2)]
        self._snake[2] = [int(self._maxindex[0] / 2) - 2, int(self._maxindex[1] / 2)]
        self._snakelength = 3
        self._dir = 0

        self._fruit = [randint(0, self._maxindex[0]), randint(0, self._maxindex[1])]

        self._gamerunning = True

    def draw(self):
        self.background(0)

        # Update snake
        if self._gamerunning:
            next_sq = self.get_next_square()

            if self.out_of_bounds(next_sq) or self.hit_itself(next_sq):
                self._gamerunning = False
            else:
                if next_sq[0] == self._fruit[0] and next_sq[1] == self._fruit[1]:
                    self._snakelength += 3
                    self._fruit = [randint(0, self._maxindex[0]), randint(0, self._maxindex[1])]

                for i in range(self._snakelength - 1, 0, -1):
                    self._snake[i] = self._snake[i - 1].copy()
                self._snake[0] = next_sq
                self._dirchanged = False

        # Draw fruit
        self.fill(127, 0, 0)
        self.rect(
            self._fruit[0] * SQUARE_SIZE, self._fruit[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE
        )

        # Draw snake
        self.stroke(255)
        self.fill(0, 0, 255)
        for i in range(self._snakelength):
            self.rect(
                self._snake[i][0] * SQUARE_SIZE,
                self._snake[i][1] * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE,
            )
        self.fill(255)
        self.rect(
            self._snake[0][0] * SQUARE_SIZE,
            self._snake[0][1] * SQUARE_SIZE,
            SQUARE_SIZE,
            SQUARE_SIZE,
        )

    def get_next_square(self) -> list[int]:
        last = self._snake[0]
        next_sq = [-1, -1]

        if self._dir == 0:
            next_sq = [last[0], last[1] - 1]
        elif self._dir == 1:
            next_sq = [last[0] + 1, last[1]]
        elif self._dir == 2:
            next_sq = [last[0], last[1] + 1]
        elif self._dir == 3:
            next_sq = [last[0] - 1, last[1]]

        return next_sq

    def out_of_bounds(self, p: list[int]) -> bool:
        return p[0] < 0 or p[0] > self._maxindex[0] or p[1] < 0 or p[1] > self._maxindex[1]

    def hit_itself(self, p: list[int]) -> bool:
        for i in range(self._snakelength):
            if self._snake[i][0] == p[0] and self._snake[i][1] == p[1]:
                return True
        return False

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/snake_game.jpg")
            return

        if self._dirchanged:
            return

        key_code = e.get_key_code()
        if key_code == self.UP and self._dir != 2:
            self._dir = 0
            self._dirchanged = True
        elif key_code == self.RIGHT and self._dir != 3:
            self._dir = 1
            self._dirchanged = True
        elif key_code == self.DOWN and self._dir != 0:
            self._dir = 2
            self._dirchanged = True
        elif key_code == self.LEFT and self._dir != 1:
            self._dir = 3
            self._dirchanged = True


if __name__ == "__main__":
    sketch = C003_SnakeGame()
    sketch.run_sketch()
