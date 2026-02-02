from py5 import Sketch

WINDOW = 800
CELL_COUNT = 61


class LightningBFS(Sketch):
    cell_size: int = WINDOW // CELL_COUNT
    grid_size: int = CELL_COUNT * cell_size
    border: int = cell_size
    grid: list[list[int]] = [[0 for _ in range(CELL_COUNT)] for _ in range(CELL_COUNT)]
    light_counter: int = 0
    current_front: list = []
    lightning: list[tuple[int, int]] = []
    maze: tuple[list[list[bool]], list[list[bool]]]

    def settings(self) -> None:
        # self.random_seed(65536)
        self.size(self.grid_size + 2 * self.border, self.grid_size + int(1.5 * self.border))

    def setup(self) -> None:
        self.frame_rate(CELL_COUNT // 2)
        self.maze = self.compute_maze()

    def draw(self) -> None:
        self.translate(self.border, self.border)
        self.draw_maze_bg()

        if not self.lightning:
            self.light_counter += 1
            if self.light_counter == 1:
                self.start_lightning()
            else:
                self.update_front()
                self.check_finished()
            self.draw_front()
        else:
            self.frame_rate(self.get_frame_rate() * 2)
            self.update_lightning()
            self.draw_lightning()
        self.draw_maze()

    def compute_maze(self) -> tuple[list[list[bool]], list[list[bool]]]:
        # ** Vertical walls between cells in each row / horizontal walls between rows (initially all walls are set)
        verts = [[True for _ in range(CELL_COUNT - 1)] for _ in range(CELL_COUNT)]
        horis = [[True for _ in range(CELL_COUNT)] for _ in range(CELL_COUNT - 1)]

        # ** Compute path by connecting cell clusters until there's only one cluster
        maze = {x * CELL_COUNT + y: {(x, y)} for y in range(CELL_COUNT) for x in range(CELL_COUNT)}
        while len(maze) > 1:
            # Pick random cell and random neighbor
            x, y = int(self.random(CELL_COUNT)), int(self.random(CELL_COUNT))
            neighbors = get_neighbors(x, y)
            nx, ny = neighbors[int(self.random(len(neighbors)))]

            # Find clusters of both cells (only continue if different clusters)
            cluster = next(idx for idx, cells in maze.items() if (x, y) in cells)
            if (nx, ny) in maze[cluster]:
                continue
            ncluster = next(idx for idx, cells in maze.items() if (nx, ny) in cells)

            # Remove wall of the path connecting both cells
            if y == ny:
                verts[y][min(x, nx)] = False
            elif x == nx:
                horis[min(y, ny)][x] = False

            # Update dict to keep track of clusters
            maze[cluster] |= maze[ncluster]
            del maze[ncluster]

        # ** Return walls
        return verts, horis

    def draw_maze_bg(self) -> None:
        self.background(30)
        self.stroke_weight(1)
        self.fill(60)
        self.rect(0, 0, self.grid_size, self.grid_size)

    def draw_maze(self) -> None:
        # ** Walls
        self.stroke_weight(1)
        self.stroke(200)
        verts, horis = self.maze

        # Vertical
        self.push_matrix()
        for row in verts:
            self.push_matrix()
            for wall in row:
                self.translate(self.cell_size, 0)
                if wall:
                    self.line(0, 0, 0, self.cell_size)
            self.pop_matrix()
            self.translate(0, self.cell_size)
        self.pop_matrix()

        # Horizontal
        self.push_matrix()
        for row in horis:
            self.translate(0, self.cell_size)
            self.push_matrix()
            for wall in row:
                if wall:
                    self.line(0, 0, self.cell_size, 0)
                self.translate(self.cell_size, 0)
            self.pop_matrix()
        self.pop_matrix()

        # ** Border
        self.stroke(170)
        self.stroke_weight(4)
        self.no_fill()
        self.rect(-2, -2, self.grid_size + 4, self.grid_size + 4)
        self.no_stroke()
        self.fill(0, 100, 0)
        self.rect(-self.border, self.grid_size, self.grid_size + 2 * self.border, self.border // 2)
        # Cell values
        self.text_align(self.CENTER, self.CENTER)
        self.text_size(self.cell_size // 2.5)
        self.fill(245, 245, 245, 150)
        for y in range(CELL_COUNT):
            for x in range(CELL_COUNT):
                if self.grid[x][y] != 0:
                    self.text(
                        self.grid[x][y],
                        x * self.cell_size + self.cell_size // 2,
                        y * self.cell_size + self.cell_size // 2,
                    )

    def start_lightning(self) -> None:
        # global current_front
        self.grid[CELL_COUNT // 2][0] = self.light_counter
        self.current_front = [(CELL_COUNT // 2, 0)]

    def update_front(self) -> None:
        # global current_front
        verts, horis = self.maze
        new_front = []
        for x, y in self.current_front:
            neighbors = get_neighbors(x, y)
            for nx, ny in neighbors:
                if x != nx:
                    if not verts[y][min(x, nx)] and self.grid[nx][y] == 0:
                        self.grid[nx][y] = self.light_counter
                        new_front.append((nx, y))
                elif y != ny:
                    if not horis[min(y, ny)][x] and self.grid[x][ny] == 0:
                        self.grid[x][ny] = self.light_counter
                        new_front.append((x, ny))

        self.current_front = new_front

    def draw_front(self) -> None:
        if len(self.current_front) == 0:
            return

        min_y = min(y for _, y in self.current_front) - 1
        max_y = max(y for _, y in self.current_front)
        self.no_stroke()
        for x, y in self.current_front:
            trans: float = self.remap(y, min_y, max_y, 60, 250)  # type: ignore

            self.fill(255, 220, 0, trans)
            self.draw_cell(x, y)

    def check_finished(self) -> None:
        for x, y in self.current_front:
            if y == CELL_COUNT - 1:
                self.lightning = [(x, y)]
                return

    def update_lightning(self) -> None:
        x, y = self.lightning[-1]
        counter = self.grid[x][y]
        if counter == 1:
            return

        next_cell = next(
            (nx, ny) for nx, ny in get_neighbors(x, y) if self.grid[nx][ny] == counter - 1
        )
        self.lightning.append(next_cell)

    def draw_lightning(self) -> None:
        self.fill(255, 220, 0)
        for x, y in self.lightning:
            self.draw_cell(x, y)

    def draw_cell(self, x: int, y: int) -> None:
        self.rect(
            x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, 7, 7, 7, 7
        )


def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
    neighbors = []
    if x != 0:
        neighbors.append((x - 1, y))
    if x != CELL_COUNT - 1:
        neighbors.append((x + 1, y))
    if y != 0:
        neighbors.append((x, y - 1))
    if y != CELL_COUNT - 1:
        neighbors.append((x, y + 1))

    return neighbors


if __name__ == "__main__":
    sketch = LightningBFS()
    sketch.run_sketch()
