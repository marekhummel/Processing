from __future__ import annotations
from enum import Enum


class Colour(Enum):
    Blue = (30, 90, 220)
    Black = (20, 20, 20)
    Red = (220, 40, 40)
    Cyan = (0, 200, 200)
    Pink = (255, 100, 200)
    Yellow = (255, 200, 0)
    Purple = (255, 0, 255)


# https://en.wikipedia.org/wiki/Fairy_chess_piece
class PieceType(Enum):
    Wazir = (1, 0)
    Dabbaba = (2, 0)
    Dromedary = (3, 0)
    Ferz = (1, 1)
    Knight = (2, 1)
    Camel = (3, 1)
    Alfil = (2, 2)
    Zebra = (3, 2)
    Antelope = (4, 3)

    def abbrev(self) -> str:
        match self:
            case PieceType.Wazir:
                return "W"
            case PieceType.Dabbaba:
                return "D"
            case PieceType.Dromedary:
                return "H"
            case PieceType.Ferz:
                return "F"
            case PieceType.Knight:
                return "N"
            case PieceType.Camel:
                return "C"
            case PieceType.Alfil:
                return "A"
            case PieceType.Zebra:
                return "Z"
            case PieceType.Antelope:
                return "L"

        return "?"


class Piece:
    def __init__(self, ptype: PieceType, colour: Colour):
        self.ptype = ptype
        self.colour = colour

        dx, dy = self.ptype.value
        self.variants = {
            (dx, dy),
            (dx, -dy),
            (-dx, dy),
            (-dx, -dy),
            (dy, dx),
            (dy, -dx),
            (-dy, dx),
            (-dy, -dx),
        }
