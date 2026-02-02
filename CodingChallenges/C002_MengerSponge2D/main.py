import os
from py5 import Sketch
from box_class import Box


class C002_MengerSponge2D(Sketch):
    boxes: list[Box] = []

    def settings(self):
        self.size(400, 400)

    def setup(self):
        self.background(0)

        self.rect_mode(self.CENTER)
        self.fill(128, 0, 0)
        self.no_stroke()

        self.boxes = []
        self.boxes.append(Box(self.width / 2, self.height / 2, 300))

    def draw(self):
        self.background(0)
        for b in self.boxes:
            b.display(self)

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/menger_sponge_2d.jpg")
            return

        newboxes = []
        for b in self.boxes:
            newboxes.extend(b.split())
        self.boxes = newboxes


if __name__ == "__main__":
    sketch = C002_MengerSponge2D()
    sketch.run_sketch()
