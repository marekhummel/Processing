from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from py5 import Sketch

from pieces import Piece
from spiral import Spiral, Index


@dataclass(frozen=True)
class PiecePlacement:
    piece: Piece
    number: int
    index: Index


class Knighting:
    def __init__(self, spiral: Spiral, pieces: list[Piece]):
        self.spiral = spiral
        self.pieces = pieces
        self._piece_index = 0
        self._placements: list[PiecePlacement] = []
        self._pending_draw_placements: list[PiecePlacement] = []
        self._scan_numbers = [0] * len(self.pieces)
        self._occupied_indices: dict[tuple[int, int], Piece] = {}
        self._occupied_indices_by_piece: dict[Piece, set[Index]] = {piece: set() for piece in pieces}
        self._seed_origin()

    def step(self) -> bool:
        checked_pieces = 0
        while checked_pieces < len(self.pieces):
            piece_index = self._piece_index
            while self._scan_numbers[piece_index] < self.spiral.upper_bound:
                next_number = self._scan_numbers[piece_index] + 1
                index = self.spiral.index_of(next_number)
                self._scan_numbers[piece_index] = next_number

                if index is None:
                    continue

                if self._is_piece_move_blocked(piece_index, index):
                    continue

                self._place(next_number, index, piece_index)
                self._advance_piece()
                return True

            self._advance_piece()
            checked_pieces += 1

        return False

    def draw(self, sketch: Sketch, square_size_factor: float) -> None:
        cell_size = self.spiral.cell_size(sketch)
        square_size = cell_size * square_size_factor
        use_single_pixel = square_size < 1

        centre_x = sketch.width / 2
        centre_y = sketch.height / 2

        if use_single_pixel:
            sketch.load_np_pixels()
            piece_xys: dict[Piece, list[tuple[int, int]]] = {p: [] for p in self.pieces}
            for placement in self._pending_draw_placements:
                x = round(centre_x + placement.index[0] * cell_size)
                y = round(centre_y - placement.index[1] * cell_size)
                if x < 0 or x >= sketch.width or y < 0 or y >= sketch.height:
                    continue
                piece_xys[placement.piece].append((x, y))

            for piece, xys in piece_xys.items():
                if xys:
                    xs = [xy[0] for xy in xys]
                    ys = [xy[1] for xy in xys]
                    r, g, b = piece.colour.value
                    sketch.np_pixels[np.asarray(ys), np.asarray(xs)] = np.array(
                        [255, r, g, b], dtype=np.uint8
                    )
            sketch.update_np_pixels()

        else:
            half_size = square_size / 2

            sketch.no_stroke()
            for placement in self._pending_draw_placements:
                x = centre_x + placement.index[0] * cell_size
                y = centre_y - placement.index[1] * cell_size
                sketch.fill(*placement.piece.colour.value)
                sketch.rect(x - half_size, y - half_size, square_size, square_size)

        self._pending_draw_placements.clear()

    def _seed_origin(self) -> None:
        origin = self.spiral.index_of(0)
        if origin is None:
            raise ValueError("spiral must contain the origin")
        self._place(0, origin, self._piece_index)
        self._advance_piece()

    def _advance_piece(self) -> None:
        self._piece_index = (self._piece_index + 1) % len(self.pieces)

    def _place(self, number: int, index: Index, piece_index: int) -> None:
        piece = self.pieces[piece_index]
        placement = PiecePlacement(piece, number, index)
        self._placements.append(placement)
        self._pending_draw_placements.append(placement)
        self._occupied_indices[index] = piece
        self._occupied_indices_by_piece[piece].add(index)

    def _is_piece_move_blocked(self, piece_index: int, index: Index) -> bool:
        if index in self._occupied_indices:
            return True

        current_piece = self.pieces[piece_index]
        for other_piece in self.pieces:
            if len(self.pieces) > 1 and other_piece is current_piece:
                continue

            occupied_indices = self._occupied_indices_by_piece[other_piece]
            for dx, dy in other_piece.variants:
                if (index[0] + dx, index[1] + dy) in occupied_indices:
                    return True

        return False
