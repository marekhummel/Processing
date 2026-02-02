import os
from math import pi, cos, sin
from py5 import Sketch


FILENAME = "data/eclipse.txt"


class C040_1_WordCounter(Sketch):
    counter: dict[str, int] = {}
    keys_sorted: list[str] = []

    def settings(self):
        self.size(700, 600)

    def setup(self):
        file_path = os.path.join(os.path.dirname(__file__), FILENAME)
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                file_content = f.read()

            # Split into words
            import re

            words = re.findall(r"\b\w+\b", file_content.lower())
            self.counter = self.count_words(words)

            # Sort by value
            self.keys_sorted = sorted(self.counter.keys(), key=lambda k: self.counter[k])
        else:
            self.counter = {}
            self.keys_sorted = []

    def draw(self):
        self.background(51)

        self.no_stroke()
        self.fill(255)
        self.text_size(14)
        self.text(FILENAME, 10, 20)

        if len(self.keys_sorted) == 0:
            return

        wordcount = len(self.keys_sorted)
        ts = (self.height - 20) / wordcount

        self.stroke_weight(ts / 3.0)
        self.text_size(ts)
        maxwidth = self.max_text_width(self.keys_sorted)
        self.translate(self.width - maxwidth, self.height - 5)

        max_value = max(self.counter.values())

        for i in range(wordcount):
            y = -i * ts

            self.no_fill()
            self.stroke(255)
            end = pi + self.HALF_PI * (self.counter[self.keys_sorted[i]] / (max_value * 1.03))
            r = i * ts + ts / 4
            self.arc(-15, 0, 2 * r, 2 * r, pi, end)

            self.fill(255)
            self.no_stroke()
            self.text(self.keys_sorted[i], -10, y)

            end += pi / (r / 2)
            self.text(
                str(self.counter[self.keys_sorted[i]]), -15 + r * cos(end) - ts / 2, r * sin(end)
            )

    def count_words(self, words: list[str]) -> dict[str, int]:
        counter = {}
        for w in words:
            if w not in counter:
                counter[w] = 0
            counter[w] += 1
        return counter

    def max_text_width(self, texts: list[str]) -> float:
        max_w = 0
        for t in texts:
            tw = self.text_width(t)
            if tw > max_w:
                max_w = tw
        return max_w

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/word_counter.jpg")


if __name__ == "__main__":
    sketch = C040_1_WordCounter()
    sketch.run_sketch()
