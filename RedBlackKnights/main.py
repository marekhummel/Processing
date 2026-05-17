# https://www.youtube.com/watch?v=UiX4CFIiegM

import os
from py5 import Sketch

from knighting import Knighting
from pieces import Piece, PieceType, Colour
from spiral import Spiral


N = 3200000
SIZE = 1200
DRAW_SPIRAL = False
STEPS_PER_FRAME = N // 20
SQUARE_SIZE_FACTOR = 1.0


# PIECES = [Piece(PieceType.Knight, Colour.Blue)]
# PIECES = [Piece(PieceType.Knight, Colour.Black), Piece(PieceType.Knight, Colour.Red)]
# PIECES = [Piece(PieceType.Knight, c) for c in [Colour.Black, Colour.Red, Colour.Cyan]]
# PIECES = [Piece(PieceType.Knight, c) for c in [Colour.Black, Colour.Red, Colour.Cyan, Colour.Pink]]
# PIECES = [Piece(PieceType.Alfil, Colour.Black), Piece(PieceType.Dromedary, Colour.Yellow)]
# PIECES = [Piece(PieceType.Knight, Colour.Black), Piece(PieceType.Antelope, Colour.Cyan)]
# PIECES = [Piece(PieceType.Knight, Colour.Black), Piece(PieceType.Dabbaba, Colour.Red), Piece(PieceType.Wazir, Colour.Cyan), Piece(PieceType.Wazir, Colour.Purple)]  # fmt: skip
# PIECES = [Piece(PieceType.Knight, Colour.Black), Piece(PieceType.Zebra, Colour.Red)]
# PIECES = [Piece(PieceType.Wazir, Colour.Black), Piece(PieceType.Ferz, Colour.Red), Piece(PieceType.Wazir, Colour.Cyan), Piece(PieceType.Ferz, Colour.Purple)]  # fmt: skip
PIECES = [Piece(PieceType.Camel, Colour.Black), Piece(PieceType.Knight, Colour.Yellow)]


class RedBlackKnights(Sketch):
    spiral: Spiral
    knighting: Knighting

    def settings(self):
        self.size(SIZE, SIZE)

    def setup(self):
        self.spiral = Spiral(N)
        self.knighting = Knighting(self.spiral, PIECES)

        self.background(245)
        if DRAW_SPIRAL:
            self.spiral.draw(self)

    def draw(self):
        advanced = False
        for _ in range(STEPS_PER_FRAME):
            if not self.knighting.step():
                break
            advanced = True
        self.knighting.draw(self, SQUARE_SIZE_FACTOR)
        if not advanced:
            self.no_loop()

    def key_typed(self, e):
        if e.get_key() == "s":
            pieces = [p.ptype.abbrev().lower() for p in PIECES]
            self.save(os.path.dirname(__file__) + f"/images/chess_{''.join(pieces)}_{N}.jpg")


if __name__ == "__main__":
    sketch = RedBlackKnights()
    sketch.run_sketch()
