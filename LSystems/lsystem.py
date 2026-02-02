from abc import ABC, abstractmethod
from py5 import Sketch


class LSystem(ABC):
    def __init__(self, axiom: str, rules: dict[str, str]):
        self.current_state = axiom
        self.rules = rules
        self.n = 0

    def produce(self):
        new_state = ""
        for i in range(len(self.current_state)):
            c = self.current_state[i]

            found = False
            for k in self.rules.keys():
                if c == k:
                    new_state += self.rules[k]
                    found = True
                    break
            if not found:
                new_state += c

        self.current_state = new_state
        self.n += 1

    @abstractmethod
    def set_matrix(self, sketch: Sketch):
        pass

    @abstractmethod
    def interpretate(self, k: str, sketch: Sketch):
        pass
