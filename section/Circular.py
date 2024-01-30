import numpy as np
import matplotlib.pyplot as plt
from workhelper.section.Section import Section
from workhelper.section.utils import clear_float_last_zero

class Circular(Section):
    
    def __init__(self, d, centroid=(0, 0)):
        super().__init__(centroid)
        self.d, self.r = d, d / 2

    def __check__(self) -> None:
        if self.d <= 0:
            raise ValueError("d must be positive")

    @property
    def secname(self) -> str:
        return "圆截面"

    @property
    def symbol(self) -> str:
        d = clear_float_last_zero(self.d)
        return f"Φ{d}"

    @property
    def area(self) -> float:
        return np.pi * self.d**2 / 4
    
    @property
    def Ix(self):
        return np.pi * self.d**4 / 64

    Iy = Ix

    @property
    def border(self) -> np.ndarray:
        return np.array((-self.d / 2+ self.centroid[0], self.d / 2+ self.centroid[0],
                         -self.d / 2+ self.centroid[1], self.d / 2+ self.centroid[1]))

    def plot(self, show=True):
        plt.gca().set_aspect("equal")
        theta = np.linspace(0, 2 * np.pi, 200)
        x, y = (
            self.r * np.cos(theta) + self.centroid[0],
            self.r * np.sin(theta) + self.centroid[1],
        )
        plt.plot(x, y, color="black")
        if show:
            plt.show()

if __name__ == "__main__":
    c = Circular(200)
    print(c)
    c.plot()