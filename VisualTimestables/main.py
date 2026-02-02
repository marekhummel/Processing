import os
from py5 import Sketch
import math

MAX_FACTOR = 10
ALLOW_FLOATING_FACTOR = True


class VisualTimestables(Sketch):
    factor: float = 2.0
    modulus: int = 200
    circlerad: float = 0.0

    def settings(self):
        self.size(500, 500)

    def setup(self):
        self.color_mode(self.HSB)
        self.circlerad = 0.45 * min(self.width, self.height)

    def draw(self):
        self.background(255)
        self.translate(self.width / 2, self.height / 2)
        self.rotate(self.PI)  # so the point in the west is fixed rather than the one in the east

        # Catch mouse
        self.modulus = int(
            self.constrain(self.remap(self.mouse_x, 0, 0.8 * self.width, 2, 200), 2, 200)
        )
        self.factor = float(self.remap(self.mouse_y, 0, self.height, 2, MAX_FACTOR))
        self.factor = self.factor if ALLOW_FLOATING_FACTOR else int(self.factor)

        # Draw circle itself (the perimeter)
        self.no_fill()
        self.stroke_weight(1)
        self.stroke(127, 127, 127)
        self.ellipse(0, 0, 2 * self.circlerad, 2 * self.circlerad)

        hue = int(self.remap(self.factor, 2, MAX_FACTOR, 0, 255))
        sat = int(self.remap(self.modulus, 2, 200, 200, 255))

        # Draw points on perimeter
        self.no_stroke()
        self.fill(hue, sat, 255)
        angle = 0
        while angle < math.tau:
            self.ellipse(math.cos(angle) * self.circlerad, math.sin(angle) * self.circlerad, 5, 5)
            angle += math.tau / self.modulus

        # Draw lines
        self.stroke_weight(1)
        self.stroke(hue, sat, 255)
        self.no_fill()
        for i in range(self.modulus):
            start_x, start_y = self.angle_to_point(
                float(self.remap(i, 0, self.modulus, 0, math.tau))
            )
            end_x, end_y = self.angle_to_point(
                float(self.remap((i * self.factor) % self.modulus, 0, self.modulus, 0, math.tau))
            )

            self.line(start_x, start_y, end_x, end_y)

        # Plot text
        self.reset_matrix()
        self.no_stroke()
        self.fill(0)
        self.text_size(13)
        self.text_align(self.RIGHT, self.TOP)
        self.text(str(self.factor), self.width - 5, 0)
        self.text(str(self.modulus), self.width - 5, 15)

    def angle_to_point(self, angle: float) -> tuple[float, float]:
        return (math.cos(angle) * self.circlerad, math.sin(angle) * self.circlerad)

    def key_typed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/visual_timestables.jpg")


if __name__ == "__main__":
    sketch = VisualTimestables()
    sketch.run_sketch()
