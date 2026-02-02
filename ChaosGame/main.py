# https://www.youtube.com/watch?v=kbKtFN71Lfs

import os
from py5 import Sketch

WINDOW = 800
TRACE_RADIUS = 0.5
RANDOM_TRIG = False
JUMP = 0.5


class ChaosGame(Sketch):
    trace: list[tuple[float, float]]
    trig: list[tuple[float, float]]

    def settings(self):
        self.size(WINDOW, WINDOW)

    def setup(self):
        self.ellipse_mode(self.RADIUS)
        self.background(245)
        self.no_stroke()

        self.gen_triangle()
        self.gen_start()

        self.frame_rate(2)

    def draw(self):
        new_trace = []
        for x, y in self.trace:
            for tx, ty in self.trig:
                nx = x + JUMP * (tx - x)
                ny = y + JUMP * (ty - y)
                new_trace.append((nx, ny))
                self.fill(0, 0, 0, 180)
                self.circle(nx, ny, TRACE_RADIUS)
        self.trace = new_trace

        if self.frame_count == 10:
            print("Stop")
            self.no_loop()
            self.save(os.path.dirname(__file__) + "/chaos_game.jpg")

    def gen_triangle(self):
        if not RANDOM_TRIG:
            self.trig = [(400, 100), (100, 700), (700, 700)]
            return

        while True:
            x1, y1 = (self.random(WINDOW), self.random(WINDOW))
            x2, y2 = (self.random(WINDOW), self.random(WINDOW))
            x3, y3 = (self.random(WINDOW), self.random(WINDOW))

            cx, cy = ((x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3)  # centroid
            area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            target_area = 0.25 * (WINDOW * WINDOW)
            s = self.sqrt(target_area / area)

            x1, y1 = (cx + s * (x1 - cx), cy + s * (y1 - cy))
            x2, y2 = (cx + s * (x2 - cx), cy + s * (y2 - cy))
            x3, y3 = (cx + s * (x3 - cx), cy + s * (y3 - cy))
            self.trig = [(x1, y1), (x2, y2), (x3, y3)]

            if all(0 <= v < WINDOW for v in [x1, x2, x3, y1, y2, y3]):
                break

        print("trig found")
        self.fill(0)
        for tx, ty in self.trig:
            self.circle(tx, ty, 7)

    def gen_start(self):
        x1, y1 = self.trig[0]
        x2, y2 = self.trig[1]
        x3, y3 = self.trig[2]
        denominator = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
        while True:
            candidate = (self.random(WINDOW), self.random(WINDOW))
            x, y = candidate

            a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denominator
            b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denominator
            if a >= 0 and b >= 0 and (1 - a - b) >= 0:
                self.trace = [candidate]
                self.fill(255, 0, 0)
                self.circle(candidate[0], candidate[1], TRACE_RADIUS * 3)
                print("start found")
                break


if __name__ == "__main__":
    sketch = ChaosGame()
    sketch.run_sketch()
