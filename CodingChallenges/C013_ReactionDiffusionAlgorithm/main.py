import os
import numpy as np
from scipy.signal import convolve2d
from py5 import Sketch


DA = 1.0
DB = 0.5
FEED = 0.055
KILL = 0.062
DT = 1.0
UPF = 5  # updates per frame

# Laplacian kernel: center -1, adjacent .2, diagonals .05
LAPLACE_KERNEL = np.array([[0.05, 0.2, 0.05], [0.2, -1.0, 0.2], [0.05, 0.2, 0.05]])


class C013_ReactionDiffusionAlgorithm(Sketch):
    def settings(self):
        self.size(300, 300)
        self.pixel_density(1)

    def setup(self):
        # Initialize as 2D numpy arrays: a and b channels
        self.a = np.ones((self.height, self.width), dtype=np.float32)
        self.b = np.zeros((self.height, self.width), dtype=np.float32)

        # Seed with random circles
        for i in range(10):
            cx = int(np.random.random() * (self.width - 10))
            cy = int(np.random.random() * (self.height - 10))
            self.b[cy : cy + 10, cx : cx + 10] = 1.0

    def draw(self):
        # Update reaction-diffusion
        for i in range(UPF):
            lap_a = convolve2d(self.a, LAPLACE_KERNEL, mode="same", boundary="wrap")
            lap_b = convolve2d(self.b, LAPLACE_KERNEL, mode="same", boundary="wrap")

            # Vectorized reaction-diffusion update
            ab2 = self.a * self.b * self.b
            self.a += (DA * lap_a - ab2 + FEED * (1 - self.a)) * DT
            self.b += (DB * lap_b + ab2 - (KILL + FEED) * self.b) * DT

            # Clamp values
            np.clip(self.a, 0, 1, out=self.a)
            np.clip(self.b, 0, 1, out=self.b)

        # Draw
        self.load_np_pixels()
        gray = np.clip((self.a - self.b) * 255, 0, 255).astype(np.uint8)
        self.np_pixels[:, :, 0] = gray
        self.np_pixels[:, :, 1] = gray
        self.np_pixels[:, :, 2] = gray
        self.np_pixels[:, :, 3] = 255
        self.update_np_pixels()

    def key_pressed(self, e):
        if e.get_key() == "s":
            self.save(os.path.dirname(__file__) + "/reaction_diffusion.jpg")


if __name__ == "__main__":
    sketch = C013_ReactionDiffusionAlgorithm()
    sketch.run_sketch()
