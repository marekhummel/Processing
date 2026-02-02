from node import Node


class Tree:
    root: Node
    limit: int
    maxgen: int
    gen: int = 0
    vals: list[int]
    actives: list[Node] = []

    def __init__(self, lim: int, gl: int):
        self.root = Node(2)
        self.vals = [self.root.value]
        self.limit = lim
        self.maxgen = gl
        self.actives = []
        self.gen = 0

    def generate_next(self):
        if self.gen == 0:
            self.actives.append(self.root)

        if len(self.actives) == 0:
            return

        for i in range(len(self.actives) - 1, -1, -1):
            n = self.actives[i]
            if n.add_children(self.limit, self.vals):
                self.actives.extend(n.children)
                for c in n.children:
                    self.vals.append(c.value)
            self.actives.pop(i)

        self.gen += 1
        print(len(self.vals))

    def display(self, x: float, y: float, angle: float, sketch):
        for n in self.actives:
            n.hl = True
        self.root.display(x, y, angle, sketch)
