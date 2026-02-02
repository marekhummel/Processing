import math
import py5

CRADIUS = 15
WINDOW = (800, 800)


class DrawCircle(py5.Sketch):
    gridsize: tuple[int, int]
    cellsize: int

    def settings(self):
        self.gridsize = (CRADIUS * 2 + 5, CRADIUS * 2 + 5)
        self.cellsize = WINDOW[0] // self.gridsize[0]
        self.size(
            self.gridsize[0] * self.cellsize,
            self.gridsize[1] * self.cellsize,
        )  # adapt window size to fit cells

    def setup(self):
        self.draw_grid()
        self.draw_circle()
        myFont = self.create_font("Ubuntu Mono Regular", self.cellsize)
        self.text_font(myFont)
        self.text(str(CRADIUS), 0, self.cellsize - 1)
        self.no_loop()
        self.save("circle.jpg")

    def draw_grid(self):
        self.background(245)

        for i in range(1, self.gridsize[0]):
            self.stroke(200 if i % 5 == 0 else 230)
            x = i * self.cellsize
            self.line(x, 0, x, self.height)

        for j in range(1, self.gridsize[1]):
            self.stroke(200 if j % 5 == 0 else 230)
            y = j * self.cellsize
            self.line(0, y, self.width, y)

    def draw_circle(self):
        # center
        center = (self.gridsize[0] // 2, self.gridsize[1] // 2)
        self.fill(255, 0, 0)
        self.stroke(100, 0, 0)
        self.fill_rect(*center)

        start = (center[0] + CRADIUS, center[1])
        last_cell = start

        self.fill(55)
        self.stroke(25)
        self.fill_rect(*last_cell)

        while True:
            neighbors = moore(*last_cell, self.width, self.height)
            poss_neighbors = [n for n in neighbors if is_in_front_ccw(center, last_cell, n)]
            if start in poss_neighbors:
                break

            distances = [(n, distance(center, n)) for n in poss_neighbors]
            best = sorted(distances, key=lambda d: abs(CRADIUS - d[1]))[0][0]
            self.fill_rect(*best)

            last_cell = best

    def fill_rect(self, i: int, j: int):
        sw = self.cellsize * 0.1
        self.stroke_weight(sw)
        self.rect(
            i * self.cellsize + sw // 2,
            j * self.cellsize + sw // 2,
            self.cellsize - sw + 1,
            self.cellsize - sw + 1,
        )


def moore(i: int, j: int, width: int, height: int) -> list[tuple[int, int]]:
    neighbors = []
    if i != 0:
        neighbors.append((i - 1, j))  # left
    if i != width - 1:
        neighbors.append((i + 1, j))  # right
    if j != 0:
        neighbors.append((i, j - 1))  # top
    if j != height - 1:
        neighbors.append((i, j + 1))  # bottom

    if i != 0 and j != 0:
        neighbors.append((i - 1, j - 1))  # top left
    if i != 0 and j != height - 1:
        neighbors.append((i - 1, j + 1))  # bottom left
    if i != width - 1 and j != 0:
        neighbors.append((i + 1, j - 1))  # top right
    if i != width - 1 and j != height - 1:
        neighbors.append((i + 1, j + 1))  # bottom right

    return neighbors


def is_in_front_ccw(center: tuple[int, int], p1: tuple[int, int], p2: tuple[int, int]) -> bool:
    v1 = (p1[0] - center[0], p1[1] - center[1])
    v2 = (p2[0] - center[0], p2[1] - center[1])
    # z-entry of cross product, if negative it means v2 is left of v1 (ccw)
    c3 = v1[0] * v2[1] - v1[1] * v2[0]
    return c3 < 0


def distance(center: tuple[int, int], pt: tuple[int, int]) -> float:
    v = (pt[0] - center[0], pt[1] - center[1])
    return math.sqrt(v[0] * v[0] + v[1] * v[1])


if __name__ == "__main__":
    sketch = DrawCircle()
    sketch.run_sketch()
