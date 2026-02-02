import os
from math import log
from py5 import Sketch
import re


class C040_3_TF_IDF(Sketch):
    filenames: list[str] = []
    docs: list[list[str]] = []

    def settings(self):
        self.size(600, 600)

    def setup(self):
        data_path = os.path.join(os.path.dirname(__file__), "data")
        if os.path.exists(data_path):
            self.filenames = [f for f in os.listdir(data_path) if f.endswith(".txt")]
            self.load_docs(data_path)

            for i in range(min(1, len(self.docs))):
                doc = self.docs[i]

                weights = {}
                for word in doc:
                    if word in weights:
                        continue

                    tfidf = self.tf(word, i) * self.idf(word)
                    print(f"{word}: {self.tf(word, i)}")
                    weights[word] = tfidf

                sorted_words = sorted(weights.keys(), key=lambda k: weights[k])
                print(self.filenames[i])
                for k in sorted_words:
                    pass  # print(f"\t{k}: {weights[k]:.9f}")
                print()

    def load_docs(self, data_path: str):
        self.docs = []
        for filename in self.filenames:
            file_path = os.path.join(data_path, filename)
            with open(file_path, "r") as f:
                file_content = f.read()

            words = re.findall(r"\b\w+\b", file_content.lower())
            self.docs.append(words)

    def tf(self, word: str, docidx: int) -> float:
        words = self.docs[docidx]
        count = 0
        for w in words:
            if w == word:
                count += 1
        return float(count)

    def idf(self, word: str) -> float:
        count = 0
        for doc in self.docs:
            contains = word in doc
            if contains:
                count += 1

        return log(len(self.docs) / float(1 + count), 10)

    def draw(self):
        self.background(51)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/tf_idf.jpg")


if __name__ == "__main__":
    sketch = C040_3_TF_IDF()
    sketch.run_sketch()
