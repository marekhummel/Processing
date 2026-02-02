from math import sqrt
from py5 import Sketch
from attraction_point import AttractionPoint
from branch import Branch
from crown_area import CrownArea


class Tree:
    kill_dis_sq: float
    attract_dis_sq: float
    branch_len: float
    aps: list[AttractionPoint]
    branches: list[Branch]
    fully_grown: bool = False

    def __init__(self, kd: float, ad: float, bl: float):
        self.kill_dis_sq = kd * kd
        self.attract_dis_sq = ad * ad
        self.branch_len = bl
        self.fully_grown = False

        self.aps = []
        self.branches = []

        self.branches.append(Branch([0.0, 0.0], [0.0, -1.0]))

    def gen_aps(self, amount: int, width: int, height: int):
        for i in range(amount):
            self.aps.append(AttractionPoint(width=width, height=height))

        # Pull the trunk upwards
        y = 0.0
        while -y < CrownArea.MIN_HEIGHT * height:
            self.aps.append(AttractionPoint(0, y, width, height))
            y -= sqrt(self.attract_dis_sq) / 4

    def grow(self):
        # Attract branches
        for a in self.aps:
            if a.reached:
                continue

            # Find closest branch
            lowest_dis_sq = 0.0
            closest_branch = None

            for b in self.branches:
                dx = a.pos[0] - b.pos[0]
                dy = a.pos[1] - b.pos[1]
                dis_sq = dx * dx + dy * dy

                # AP reached
                if dis_sq <= self.kill_dis_sq:
                    a.reached = True
                    break

                # Ignore
                if dis_sq > self.attract_dis_sq:
                    continue

                # Check if closest
                if closest_branch is None or dis_sq < lowest_dis_sq:
                    closest_branch = b
                    lowest_dis_sq = dis_sq

            # Save attraction
            if closest_branch is None:
                continue
            dx = a.pos[0] - closest_branch.pos[0]
            dy = a.pos[1] - closest_branch.pos[1]
            mag = sqrt(dx * dx + dy * dy)
            if mag > 0:
                closest_branch.attrac_dir[0] += dx / mag
                closest_branch.attrac_dir[1] += dy / mag

        # Create new branches
        newbs = []
        for b in self.branches:
            mag_sq = b.attrac_dir[0] * b.attrac_dir[0] + b.attrac_dir[1] * b.attrac_dir[1]
            if mag_sq == 0:
                continue  # Ignore if unattracted

            # Normalize attrac_dir
            mag = sqrt(mag_sq)
            norm_dir = [b.attrac_dir[0] / mag, b.attrac_dir[1] / mag]

            new_b = Branch(b.pos, norm_dir, b, self.branch_len)
            newbs.append(new_b)
            b.attrac_dir = [0.0, 0.0]  # Reset attraction
            b.children.append(new_b)

        for b in newbs:
            self.branches.append(b)

        if len(newbs) == 0:
            self.fully_grown = True

    def display(self, sketch: Sketch):
        if not self.fully_grown:
            for ap in self.aps:
                ap.display(sketch)

        for b in self.branches:
            b.display(sketch)
