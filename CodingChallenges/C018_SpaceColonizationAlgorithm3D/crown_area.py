from math import sqrt


class CrownArea:
    MIN_HEIGHT = 0.25

    @staticmethod
    def max_dis(y: float) -> float:
        return 1 - y

    @staticmethod
    def in_area(scx: float, scy: float, scz: float) -> bool:
        if scx == 0 and scz == 0:
            return True
        if scy < CrownArea.MIN_HEIGHT:
            return False
        return sqrt(scx * scx + scz * scz) <= CrownArea.max_dis(scy)
