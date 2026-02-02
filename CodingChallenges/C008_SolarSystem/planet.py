import random
import math


class Planet:
    loc: list[float]
    r: float
    angle: float
    orbitspeed: float
    children: list["Planet"] | None

    def __init__(self, d: float, r_: float, os: float):
        # Random 3D vector
        theta = random.uniform(0, 2 * math.pi)
        phi = random.uniform(0, math.pi)

        self.loc = [
            d * math.sin(phi) * math.cos(theta),
            d * math.sin(phi) * math.sin(theta),
            d * math.cos(phi),
        ]

        self.r = r_
        self.orbitspeed = os
        self.angle = random.uniform(0, 2 * math.pi)

        # Get some children
        if r_ > 10:
            num_children = int(random.uniform(0, r_ / 7))
            self.children = []
            for i in range(num_children):
                self.children.append(
                    Planet(
                        random.uniform(2, 4) * r_,
                        random.uniform(0.2, 0.4) * r_,
                        random.uniform(math.pi / 270, math.pi / 90),
                    )
                )
        else:
            self.children = None

    def update(self):
        self.angle += self.orbitspeed

        if self.children is not None:
            for c in self.children:
                c.update()

    def display(self, sketch):
        sketch.push_matrix()

        # Cross product with (0, 0, 1)
        rot_x = -self.loc[1]
        rot_y = self.loc[0]
        rot_z = 0

        sketch.rotate(self.angle, rot_x, rot_y, rot_z)
        sketch.translate(self.loc[0], self.loc[1], self.loc[2])

        sketch.no_stroke()
        sketch.fill(255)
        sketch.sphere(self.r)

        if self.children is not None:
            for c in self.children:
                c.display(sketch)

        sketch.pop_matrix()
