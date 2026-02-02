class Box:
    center: list[float]
    size: float

    def __init__(self, x: float, y: float, s: float):
        self.center = [x, y]
        self.size = s

    def display(self, sketch):
        sketch.push_matrix()
        sketch.translate(self.center[0], self.center[1])
        sketch.rect(0, 0, self.size, self.size)
        sketch.pop_matrix()

    def split(self) -> list["Box"]:
        boxes = []

        ns = self.size / 3
        for x in [-1, 0, 1]:
            nx = self.center[0] + x * ns
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue

                ny = self.center[1] + y * ns
                boxes.append(Box(nx, ny, ns))

        return boxes
