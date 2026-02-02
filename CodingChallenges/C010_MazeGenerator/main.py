import os
from random import randint
from py5 import Sketch
from cell import Cell


ROWS = 20
COLS = 20
CELLSIZE = 15


class C010_MazeGenerator(Sketch):
    _cells: list[list[Cell]]
    _current: Cell
    _path: list[Cell]
    _visited: int = 0

    def settings(self):
        self.size(COLS * CELLSIZE + 1, ROWS * CELLSIZE + 1)

    def setup(self):
        self.frame_rate(30)

        # Cells
        self._cells = []
        for i in range(COLS):
            col = []
            for j in range(ROWS):
                col.append(Cell(i, j))
            self._cells.append(col)

        self._path = []
        self._current = self._cells[0][0]
        self._path.append(self._current)

    def draw(self):
        # Update
        if self._visited != COLS * ROWS or len(self._path) != 0:
            neighbors = self.get_unvisited_neighbors(self._current.i, self._current.j)

            if len(neighbors) != 0:
                chosen = neighbors[randint(0, len(neighbors) - 1)]

                self._path.append(self._current)

                if self._current.i - chosen.i == 1:
                    self._current.walls[3] = False
                    chosen.walls[1] = False
                if self._current.i - chosen.i == -1:
                    self._current.walls[1] = False
                    chosen.walls[3] = False
                if self._current.j - chosen.j == 1:
                    self._current.walls[0] = False
                    chosen.walls[2] = False
                if self._current.j - chosen.j == -1:
                    self._current.walls[2] = False
                    chosen.walls[0] = False

                chosen.visited = True
                self._visited += 1
                self._current = chosen
            elif len(self._path) != 0:
                lasti = len(self._path) - 1
                self._current = self._path[lasti]
                self._path.pop(lasti)

        # Draw
        self.background(245)
        for i in range(COLS):
            for j in range(ROWS):
                self._cells[i][j].display(CELLSIZE, False, False, self)

        for c in self._path:
            c.display(CELLSIZE, True, False, self)
        self._current.display(CELLSIZE, True, True, self)

    def get_unvisited_neighbors(self, i: int, j: int) -> list[Cell]:
        ret = []

        if i + 1 != COLS and not self._cells[i + 1][j].visited:
            ret.append(self._cells[i + 1][j])
        if i - 1 != -1 and not self._cells[i - 1][j].visited:
            ret.append(self._cells[i - 1][j])
        if j + 1 != ROWS and not self._cells[i][j + 1].visited:
            ret.append(self._cells[i][j + 1])
        if j - 1 != -1 and not self._cells[i][j - 1].visited:
            ret.append(self._cells[i][j - 1])

        return ret

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/maze_generator.jpg")


if __name__ == "__main__":
    sketch = C010_MazeGenerator()
    sketch.run_sketch()
