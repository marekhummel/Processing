class LSystem:
    current_state: str
    rules: dict[str, str]
    n: int

    def __init__(self, axiom: str, rules_: dict[str, str]):
        self.current_state = axiom
        self.rules = rules_
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
