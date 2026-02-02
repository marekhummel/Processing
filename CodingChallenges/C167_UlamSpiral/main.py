import os
from math import sqrt
from random import random
from py5 import Sketch


WINDOW_SIZE = 750
MAX_N = 1000  # max 300000
RUNTIME = 3
PLOT_RANDOM = False
UPDATES_PER_DRAW = MAX_N // 50


class C167_UlamSpiral(Sketch):
    back_color: int
    one_color: int
    composite_color: int
    prime_color: int
    sz: int = 0
    n_info: list[tuple[int, int, int, bool]] = []

    def prime_sieve(self, n: int):
        """Sieve of Eratostenes up to n"""
        root = int(sqrt(n))
        primes = [True] * (n + 1)
        primes[0:2] = [False, False]
        for i in range(2, root + 1):
            if primes[i]:
                m = n // i - i + 1
                primes[i * i : n + 1 : i] = [False] * m

        return (i for i, p in enumerate(primes) if p)

    def settings(self):
        self.size(WINDOW_SIZE, WINDOW_SIZE)

    def setup(self):
        self.back_color = self.color(10)
        self.one_color = self.color(0, 127, 255)
        self.composite_color = self.back_color  # self.color(255)
        self.prime_color = self.color(255)  # self.color(255, 0, 0)

        self.background(self.back_color)

        # Get coordinates for each cell
        primes = set(self.prime_sieve(MAX_N))
        i, j = 0, 0
        steplen = 1
        step = 0
        inc = False
        dir = 0
        self.n_info = []

        for n in range(1, MAX_N + 1):
            # Set info
            pred = n in primes if not PLOT_RANDOM else random() < float(len(primes)) / MAX_N
            self.n_info.append((n, i, j, pred))

            # Update coordinates depending on direction
            if dir == 0:
                i += 1
            elif dir == 90:
                j -= 1
            elif dir == 180:
                i -= 1
            elif dir == 270:
                j += 1

            # Increase step in current line of the spiral
            step += 1
            if step == steplen:
                # Line end, update direction and line length if needed
                if inc:  # Only update line length every two updates
                    steplen += 1
                inc = not inc
                step = 0
                dir = (dir + 90) % 360

        # Set framerate to match runtime
        self.sz = WINDOW_SIZE // (int(sqrt(MAX_N)) + 2)
        self.frame_rate(MAX_N // (RUNTIME * UPDATES_PER_DRAW))

    def draw(self):
        # Draw one in center
        self.translate(self.width / 2, self.height / 2)

        for _ in range(UPDATES_PER_DRAW):
            # Abort if last n has been drawn
            if not self.n_info:
                self.no_loop()
                return

            # Fetch current n
            n, i, j, is_prime = self.n_info.pop(0)
            x, y = i * self.sz, j * self.sz
            used_color = (
                self.prime_color
                if is_prime
                else (self.one_color if n == 1 else self.composite_color)
            )

            if self.sz // 2 > 1:
                self.fill(used_color)
                self.no_stroke()
                self.circle(x, y, self.sz // 2)
            else:
                self.no_fill()
                self.stroke(used_color)
                self.point(x, y)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/ulam_spiral.jpg")


if __name__ == "__main__":
    sketch = C167_UlamSpiral()
    sketch.run_sketch()
