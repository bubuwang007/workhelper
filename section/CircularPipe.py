import numpy as np
import matplotlib.pyplot as plt
from workhelper.section.Section import Section
from workhelper.section.utils import clear_float_last_zero as cflz

class CircularPipe(Section):

    def __init__(self, d, t, centroid=(0, 0)):
        super().__init__(centroid)
        self.d, self.t, self.r = d, t, d / 2
        self.__check__()

    def __check__(self) -> None:
        if self.d <= 0 or self.t <= 0:
            raise ValueError("d and t must be positive")
        elif self.t > self.d / 2:
            raise ValueError("t must be less than d/2")

    @property
    def secname(self) -> str:
        return "圆管截面"

    @property
    def symbol(self) -> str:
        d,t = map(cflz, (self.d, self.t))
        return f"Φ{d}×{t}"

    @property
    def area(self) -> float:
        return np.pi * (self.r**2 - (self.r - self.t) ** 2)

    @property
    def Ix(self) -> float:
        d, t = self.d, self.t
        return (np.pi * d**4) / 64 * (1 - ((d - 2 * t) / d) ** 4)

    Iy = Ix

    @property
    def border(self) -> np.ndarray:
        return np.array((-self.d / 2+ self.centroid[0], self.d / 2+ self.centroid[0],
                         -self.d / 2+ self.centroid[1], self.d / 2+ self.centroid[1]))

    def plot(self, show=True):
        centroid = self.centroid
        plt.gca().set_aspect("equal")
        theta = np.linspace(0, 2 * np.pi, 200)
        x, y = (
            self.r * np.cos(theta) + centroid[0],
            self.r * np.sin(theta) + centroid[1],
        )
        x1, y1 = (self.r - self.t) * np.cos(theta) + centroid[0], (
            self.r - self.t
        ) * np.sin(theta) + centroid[1]
        plt.plot(x, y, color="black")
        plt.plot(x1, y1, color="black")
        if show:
            plt.show()

if __name__ == "__main__":
    c = CircularPipe(200, 20)
    print(c)
    c.plot()