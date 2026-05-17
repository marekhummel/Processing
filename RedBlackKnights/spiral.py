from __future__ import annotations

import math

from py5 import Sketch


type Index = tuple[int, int]


class Spiral:
    def __init__(self, upper_bound: int):
        self.upper_bound = upper_bound
        self._max_radius = self._layer_of(upper_bound)

    def _layer_of(self, number: int) -> int:
        if number <= 0:
            return 0
        return math.ceil((math.sqrt(number + 1) - 1) / 2)

    def index_of(self, number: int) -> Index | None:
        if number < 0 or number > self.upper_bound:
            return None
        if number == 0:
            return (0, 0)

        layer = self._layer_of(number)
        side_length = 2 * layer
        first_number = (2 * layer - 1) ** 2
        offset = number - first_number

        if offset < side_length:
            return (layer, -layer + 1 + offset)

        offset -= side_length
        if offset < side_length:
            return (layer - 1 - offset, layer)

        offset -= side_length
        if offset < side_length:
            return (-layer, layer - 1 - offset)

        offset -= side_length
        return (-layer + 1 + offset, -layer)

    def number_at(self, index: Index) -> int | None:
        x, y = index
        if x == 0 and y == 0:
            return 0

        layer = max(abs(x), abs(y))
        first_number = (2 * layer - 1) ** 2

        if x == layer and y >= -layer + 1:
            offset = y + layer - 1
        elif y == layer and x <= layer - 1:
            offset = 2 * layer + (layer - 1 - x)
        elif x == -layer and y <= layer - 1:
            offset = 4 * layer + (layer - 1 - y)
        elif y == -layer and x >= -layer + 1:
            offset = 6 * layer + (x + layer - 1)
        else:
            return None

        number = first_number + offset
        if number > self.upper_bound:
            return None
        return number

    def cell_size(self, sketch: Sketch) -> float:
        usable_width = max(sketch.width, 1)
        usable_height = max(sketch.height, 1)
        cells_per_side = 2 * self._max_radius + 1
        return min(usable_width / cells_per_side, usable_height / cells_per_side)

    def _screen_position(
        self,
        index: Index,
        centre_x: float,
        centre_y: float,
        cell_size: float,
    ) -> tuple[float, float]:
        return (centre_x + index[0] * cell_size, centre_y - index[1] * cell_size)

    def screen_position(self, number: int, sketch: Sketch) -> tuple[float, float] | None:
        index = self.index_of(number)
        if index is None:
            return None

        cell_size = self.cell_size(sketch)
        centre_x = sketch.width / 2
        centre_y = sketch.height / 2
        return self._screen_position(index, centre_x, centre_y, cell_size)

    def draw(self, sketch: Sketch) -> None:
        cell_size = self.cell_size(sketch)
        centre_x = sketch.width / 2
        centre_y = sketch.height / 2

        sketch.stroke(150)
        sketch.stroke_weight(1)
        sketch.no_fill()
        sketch.begin_shape()
        for number in range(self.upper_bound + 1):
            index = self.index_of(number)
            if index is None:
                continue
            x, y = self._screen_position(index, centre_x, centre_y, cell_size)
            sketch.vertex(x, y)
        sketch.end_shape()
