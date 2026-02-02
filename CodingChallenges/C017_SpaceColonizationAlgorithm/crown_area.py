from math import pow, fabs


class CrownArea:
    MIN_HEIGHT = 0.25

    @staticmethod
    def max_dis(y: float) -> float:
        return (pow(2 * y, 4) - 2.9 * pow(2 * y, 3) + pow(2 * y, 2) + 2 * (2 * y)) / 2

    @staticmethod
    def in_area(scx: float, scy: float, off: float) -> bool:
        if scx == 0:
            return True
        if scy < CrownArea.MIN_HEIGHT:
            return False
        return fabs(scx) + off <= CrownArea.max_dis(scy)
