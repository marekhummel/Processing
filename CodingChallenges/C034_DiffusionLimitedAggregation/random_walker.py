from random import randint, uniform
from math import pi, cos, sin


class RandomWalker:
    pos: list[float]

    def __init__(self, pts: list[list[float]]):
        idx = randint(0, len(pts) - 1)
        self.pos = pts[idx].copy()

    def move(self, width: int, height: int):
        # Random 2D vector
        angle = uniform(0, 2 * pi)
        dx = cos(angle)
        dy = sin(angle)
        self.pos[0] += dx
        self.pos[1] += dy
        self.pos[0] = max(0, min(self.pos[0], width))
        self.pos[1] = max(0, min(self.pos[1], height))

    def stuck(self, seeds: list[list[float]], dis: float) -> bool:
        for s in seeds:
            dist_sq = (self.pos[0] - s[0]) ** 2 + (self.pos[1] - s[1]) ** 2
            if dist_sq <= dis * dis:
                return True
        return False
